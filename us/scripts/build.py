# -*- coding: utf-8 -*-
"""Build all deliverables for the US Remote Job Playbook (Next Software Academy).

Outputs (us/):
  OPPORTUNITY_DIRECTORY.csv, WORKER_SUCCESS_RESEARCH.csv,
  PLAYBOOK.md, US_REMOTE_JOB_PLAYBOOK.pdf, ACTION_WORKBOOK.md, ACTION_WORKBOOK.pdf
Run: python3 us/scripts/build.py
"""
import csv
import html
import os
import re
import subprocess
import sys
from collections import Counter

from bs4 import BeautifulSoup
from pypdf import PdfReader, PdfWriter

US = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(US, "scripts")
sys.path.insert(0, SCRIPTS)
import directory_data as D  # noqa: E402
import evidence_data as E  # noqa: E402

BUILD = os.path.join(US, "build")
MANUSCRIPT = os.path.join(US, "manuscript")
BRAND = "Next Software Academy"
TITLE = "US Remote Job Playbook"
SUBTITLE = "Find legitimate remote work, get accepted, and start earning: AI training, freelance marketplaces, and remote jobs"
EDITION = "October 2026 Edition · Data verified October 22, 2026"
CHAPTERS = ["00_front.md"] + [f"{i:02d}_ch{i}.md" for i in range(1, 13)] + ["13_appendix.md"]
CHAPTER_IDS = {f"ch{i}": i for i in range(1, 13)}
TOC_SKIP_H2 = ("start", "appendix-a", "appendix-b", "appendix-c")
STATUS_CLASS = {D.APPLY: "badge-apply", D.EXPLORE: "badge-explore",
                D.CAUTION: "badge-caution", D.UNAVAILABLE: "badge-unavailable"}
PANDOC_FMT = "markdown+fenced_divs+pipe_tables+task_lists+autolink_bare_uris"


# ----------------------------------------------------------------- CSV
def write_csv(path, fields, rows):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


# ----------------------------------------------------------------- Markdown helpers
def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def short(text, n=150):
    text = str(text)
    return text if len(text) <= n else text[:n].rsplit(" ", 1)[0] + "…"


def directory_table(rows, cat_prefix):
    sel = [r for r in rows if r["category"].startswith(cat_prefix)]
    money = ("payment_and_fees", "Fees / payment") if cat_prefix == "B." else ("published_pay", "Published pay")
    # Dash counts set pandoc's relative column widths.
    out = [f"| Platform | Status | Roles & tasks | Beginner? | {money[1]} | Evidence |",
           "|-----------|------|------------------|------|--------------------|----|"]
    for r in sel:
        out.append("| [{p}]({u}) | **{s}** | {j} | {b} | {m} | {e} |".format(
            p=cell(r["platform"]), u=r["apply_link"], s=r["status"],
            j=cell(short(r["roles_and_tasks"], 120)), b=cell(short(r["beginner_friendly"], 40)),
            m=cell(short(r[money[0]], 170)), e=r["evidence_strength"]))
    out.append("")
    out.append(f"*{len(sel)} entries. Click a platform name to open its application page. Full profiles (steps, payment, "
               f"evidence, challenges, strategies, sources) are in Appendix A.*")
    return "\n".join(out)


def priority_table(rows):
    sel = [r for r in rows if r["status"] == D.APPLY]
    out = ["| Platform | Category | Who it fits | Published pay (as reported) | First step |",
           "|-----------|------|------------|--------------------|-------------|"]
    for r in sel:
        first = r["application_steps"].split("→")[0].strip()
        out.append("| **[{p}]({u})** | {c} | {b} | {m} | {f} |".format(
            p=cell(r["platform"]), u=r["apply_link"], c=r["category"][0],
            b=cell(short(r["beginner_friendly"], 90)), m=cell(short(r["published_pay"], 170)),
            f=cell(short(first, 70))))
    out.append("")
    out.append("*Category: A = AI training & AI startups · B = freelance & project marketplaces · C = other remote jobs. "
               "Click the platform name to open the application page.*")
    return "\n".join(out)


def directory_cards(rows):
    parts, current = [], None
    for r in rows:
        if r["category"] != current:
            current = r["category"]
            parts.append(f"## {current} {{.unnumbered}}\n")
        srcs = " · ".join(f"[{i + 1}]({u.strip()})" for i, u in enumerate(r["sources"].split("|")))
        fields = [
            ("Status", f"**{r['status']}** · {r['subcategory']}"),
            ("Apply", f"<{r['apply_link']}>"),
            ("Roles & tasks", r["roles_and_tasks"]),
            ("Beginner-friendly", r["beginner_friendly"]),
            ("US eligibility", r["us_eligibility"]),
            ("Requirements", r["requirements"]),
            ("Evidence strength", r["evidence_strength"]),
            ("Published pay", f"{r['published_pay']} *(source: {r['pay_source']})*"),
            ("Application steps", r["application_steps"]),
            ("Payment & fees", r["payment_and_fees"]),
            ("Worker outcomes", r["worker_outcome_evidence"]),
            ("Challenges", r["common_challenges"]),
            ("Success strategies", r["success_strategies"]),
            ("Verified", f"{r['verified_date']} · Sources: {srcs}"),
        ]
        body = "\n".join(f"- **{k}:** {v}" for k, v in fields)
        parts.append(f"::: {{.card}}\n**{r['id']} · {r['platform']}**\n\n{body}\n:::\n")
    return "\n".join(parts)


def evidence_table(rows):
    out = ["| ID | Platform | Type | Pattern | What happened | Lesson | Src |",
           "|----|------|-----|----|------------------------------|--------------|--|"]
    for r in rows:
        out.append(f"| {r['id']} | {cell(r['platform'])} | {r['evidence_type']} | {r['pattern']} | "
                   f"{cell(r['what_happened'])} | {cell(r['lesson'])} | [link]({r['source_url']}) |")
    return "\n".join(out)


def load_prompts():
    text = open(os.path.join(US, "AI_CAREER_PROMPTS.md"), encoding="utf-8").read()
    prompts = {}
    for m in re.finditer(r"^### (P\d\d) — .*?(?=^### P\d\d|^## |^---|\Z)", text, flags=re.S | re.M):
        prompts[m.group(1)] = m.group(0).strip().replace("### ", "#### ", 1)
    return prompts


def split_five(md):
    """Put each **Label:** line of .five boxes into its own paragraph."""
    def fix(block):
        lines = [ln for ln in block.group(1).strip().split("\n") if ln.strip()]
        return "::: {.five}\n" + "\n\n".join(lines) + "\n:::"
    return re.sub(r"::: \{\.five\}\n(.*?)\n:::", fix, md, flags=re.S)


def check_leftovers(md):
    leftovers = re.findall(r"\{\{[A-Z]+[:A-Za-z0-9 –]*\}\}", md)
    if leftovers:
        raise ValueError(f"Unresolved placeholders: {leftovers}")


def assemble_markdown(directory, evidence):
    prompts = load_prompts()
    counts = Counter(r["status"] for r in directory)
    md = "\n\n".join(open(os.path.join(MANUSCRIPT, c), encoding="utf-8").read() for c in CHAPTERS)
    md = re.sub(r"\{\{COUNT:(.+?)\}\}", lambda m: str(counts.get(m.group(1), 0)), md)
    md = md.replace("{{TOTAL}}", str(len(directory)))
    md = md.replace("{{EVCOUNT}}", str(len(evidence)))
    md = md.replace("{{PRIORITY}}", priority_table(directory))
    for cat in "ABC":
        md = md.replace(f"{{{{TABLE:{cat}}}}}", directory_table(directory, f"{cat}."))
    md = md.replace("{{CARDS}}", directory_cards(directory))
    md = md.replace("{{EVIDENCE}}", evidence_table(evidence))

    def prompt_sub(m):
        if m.group(1) not in prompts:
            raise KeyError(f"Prompt {m.group(1)} not found in AI_CAREER_PROMPTS.md")
        return prompts[m.group(1)]
    md = re.sub(r"\{\{PROMPT:(P\d\d)\}\}", prompt_sub, md)
    md = split_five(md)
    check_leftovers(md)
    header = (f"---\ntitle: \"{TITLE}\"\nsubtitle: \"{SUBTITLE}\"\nauthor: \"{BRAND}\"\nlang: en-US\n"
              f"date: \"{EDITION}\"\n---\n\n")
    return header + md


# ----------------------------------------------------------------- HTML
def md_to_html_fragment(md_path):
    return subprocess.run(["pandoc", md_path, "-f", PANDOC_FMT, "-t", "html5", "--wrap=none"],
                          check=True, capture_output=True, text=True).stdout


def decorate(fragment, chapter_label=True):
    soup = BeautifulSoup(fragment, "html.parser")
    for h1 in soup.find_all("h1"):
        cls = h1.get("class", [])
        num = CHAPTER_IDS.get(h1.get("id")) if chapter_label else None
        wrapper = soup.new_tag("div", attrs={"class": "chapter-start"})
        h1.insert_before(wrapper)
        if num:
            label = soup.new_tag("div", attrs={"class": "chapter-label"})
            label.string = f"CHAPTER {num}"
            wrapper.append(label)
        wrapper.append(h1.extract())
        if "unnumbered" in cls:
            wrapper["class"] = ["chapter-start", "front"]
    for pre in soup.find_all("pre"):
        pre["class"] = pre.get("class", []) + ["prompt"]
    # Status labels become colored badges.
    for strong in soup.find_all("strong"):
        cls = STATUS_CLASS.get(strong.get_text(strip=True))
        if cls:
            strong["class"] = ["badge", cls]
    for a in soup.find_all("a", href=True):
        if a["href"].startswith("http"):
            a["rel"] = "noopener"
    return soup


def build_toc(soup, title, pages=None):
    items = []
    for h in soup.find_all(["h1", "h2"]):
        hid = h.get("id")
        if not hid or h.find_parent("div", class_="card"):
            continue
        level = 1 if h.name == "h1" else 2
        parent_h1 = h.find_previous("h1") if level == 2 else h
        if level == 2 and parent_h1 is not None and (parent_h1.get("id") in TOC_SKIP_H2
                                                     or parent_h1.get("id", "").startswith("wb")):
            continue
        text = h.get_text(" ", strip=True)
        num = CHAPTER_IDS.get(hid)
        if num:
            text = f"{num}. {text}"
        items.append((level, hid, text, (pages or {}).get(hid, "000")))
    lis = [f'<li class="toc-l{lv}"><a href="#{hid}"><span class="toc-text">{html.escape(t)}</span>'
           f'<span class="toc-dots"></span><span class="toc-page">{pg}</span></a></li>'
           for lv, hid, t, pg in items]
    return (f'<nav class="toc" id="contents"><h1 class="toc-title">{title}</h1><ul>' + "".join(lis)
            + "</ul></nav>"), [i[1] for i in items]


def css():
    return open(os.path.join(SCRIPTS, "style.css"), encoding="utf-8").read()


def page_html(body, toc_html, body_class=""):
    return f"""<!doctype html>
<html lang="en-US"><head><meta charset="utf-8">
<title>{TITLE}</title>
<meta name="author" content="{BRAND}">
<meta name="description" content="{SUBTITLE}">
<style>{css()}</style></head>
<body class="{body_class}">
{toc_html}
<main>{body}</main>
</body></html>"""


def cover_html(title_html, sub, facts, bottom):
    lis = "".join(f"<li><b>{v}</b> {k}</li>" for v, k in facts)
    return f"""<!doctype html><html lang="en-US"><head><meta charset="utf-8"><title>{TITLE}</title>
<style>{css()}</style></head><body class="cover-body">
<section class="cover">
  <div class="cover-top">{EDITION.upper()}</div>
  <div class="cover-main">
    <div class="cover-brand">{BRAND.upper()}</div>
    <div class="cover-kicker">CAREER GUIDE &amp; WORKBOOK</div>
    <h1 class="cover-title">{title_html}</h1>
    <div class="cover-rule"></div>
    <p class="cover-sub">{sub}</p>
    <ul class="cover-facts">{lis}</ul>
  </div>
  <div class="cover-bottom"><div>{bottom}</div>
  <div class="cover-url">No promises of employment or earnings. Verify every listing before you rely on it.</div></div>
</section></body></html>"""


def render(html_path, pdf_path, footer_text=None):
    env = dict(os.environ, NODE_PATH="/opt/node22/lib/node_modules")
    args = ["node", os.path.join(SCRIPTS, "render_pdf.js"), html_path, pdf_path]
    args += ["--footer", footer_text] if footer_text else ["--no-footer"]
    subprocess.run(args, check=True, env=env)


def heading_pages(pdf_path, toc_ids):
    """Map heading id -> 1-based page number using the TOC link annotations."""
    reader = PdfReader(pdf_path)
    page_index = {p.indirect_reference.idnum: i for i, p in enumerate(reader.pages)}
    found = []
    for pno, page in enumerate(reader.pages[:8]):
        for annot in page.get("/Annots", []) or []:
            a = annot.get_object()
            if a.get("/Subtype") != "/Link":
                continue
            dest = a.get("/Dest")
            if dest is None and "/A" in a:
                dest = a["/A"].get_object().get("/D")
            if dest is None:
                continue
            if isinstance(dest, (str, bytes)) or hasattr(dest, "startswith"):
                d = reader.named_destinations.get(str(dest))
                if d is None:
                    continue
                target = reader.get_destination_page_number(d)
            else:
                target = page_index.get(dest[0].idnum)
            if target is None:
                continue
            rect = [float(x) for x in a["/Rect"]]
            found.append((pno, -rect[3], target + 1))
    found.sort()
    return {hid: pg for hid, (_, _, pg) in zip(toc_ids, found)}, len(found)


def build_pdf(md_path, out_pdf, name, toc_title, cover, footer, body_class="", chapter_label=True):
    soup = decorate(md_to_html_fragment(md_path), chapter_label)
    body = str(soup)
    toc1, ids = build_toc(soup, toc_title)
    p1_html, p1_pdf = os.path.join(BUILD, f"{name}_pass1.html"), os.path.join(BUILD, f"{name}_pass1.pdf")
    open(p1_html, "w", encoding="utf-8").write(page_html(body, toc1, body_class))
    render(p1_html, p1_pdf, footer)
    pages, nlinks = heading_pages(p1_pdf, ids)
    print(f"[{name}] TOC entries: {len(ids)}, TOC links found: {nlinks}")
    if nlinks != len(ids):
        print(f"WARNING [{name}]: TOC link count mismatch; page numbers may be off", file=sys.stderr)
    # Page numbers in the TOC count the cover as page 1 offset, matching the footer numbering of the body PDF.
    toc2, _ = build_toc(soup, toc_title, pages)
    b_html, b_pdf = os.path.join(BUILD, f"{name}.html"), os.path.join(BUILD, f"{name}_body.pdf")
    open(b_html, "w", encoding="utf-8").write(page_html(body, toc2, body_class))
    render(b_html, b_pdf, footer)
    c_html, c_pdf = os.path.join(BUILD, f"{name}_cover.html"), os.path.join(BUILD, f"{name}_cover.pdf")
    open(c_html, "w", encoding="utf-8").write(cover)
    render(c_html, c_pdf)
    writer = PdfWriter(clone_from=b_pdf)
    writer.insert_page(PdfReader(c_pdf).pages[0], 0)
    writer.add_metadata({"/Title": f"{toc_title if name == 'workbook' else TITLE}: {BRAND}", "/Author": BRAND,
                         "/Subject": SUBTITLE, "/Lang": "en-US"})
    with open(out_pdf, "wb") as f:
        writer.write(f)
    n = len(PdfReader(out_pdf).pages)
    print(f"[{name}] Pages: {n} -> {out_pdf}")
    return n


def main():
    os.makedirs(BUILD, exist_ok=True)
    directory = D.rows_as_dicts()
    evidence = E.rows_as_dicts()
    write_csv(os.path.join(US, "OPPORTUNITY_DIRECTORY.csv"), D.FIELDS, directory)
    write_csv(os.path.join(US, "WORKER_SUCCESS_RESEARCH.csv"), E.FIELDS, evidence)

    md = assemble_markdown(directory, evidence)
    md_out = os.path.join(US, "PLAYBOOK.md")
    open(md_out, "w", encoding="utf-8").write(md)
    counts = Counter(r["status"] for r in directory)
    cover = cover_html(
        "US Remote Job<br>Playbook", SUBTITLE,
        [(len(directory), "opportunities with direct links"), (counts[D.APPLY], "rated Apply Now"),
         (len(evidence), "documented worker outcomes"), ("21", "copy-paste AI career prompts")],
        "AI Training &amp; AI Startups · Freelance Marketplaces · Remote Jobs · AI Resume &amp; Interview Workflows")
    build_pdf(md_out, os.path.join(US, "US_REMOTE_JOB_PLAYBOOK.pdf"), "playbook", "Contents", cover,
              f"{TITLE} · {BRAND} · October 2026")

    wb_src = open(os.path.join(MANUSCRIPT, "workbook.md"), encoding="utf-8").read()
    check_leftovers(wb_src)
    wb_md = (f"---\ntitle: \"Action Workbook\"\nsubtitle: \"Companion to the {TITLE}\"\nauthor: \"{BRAND}\"\n"
             f"lang: en-US\n---\n\n" + wb_src)
    wb_out = os.path.join(US, "ACTION_WORKBOOK.md")
    open(wb_out, "w", encoding="utf-8").write(wb_md)
    wb_cover = cover_html(
        "Action<br>Workbook", f"Templates, exercises and 7-day / 30-day trackers. Companion to the {TITLE}.",
        [("6", "exercises"), ("5", "trackers"), ("3", "worksheets & templates"), ("7 + 30", "day plans")],
        "Print it or copy the tables into Google Sheets")
    build_pdf(wb_out, os.path.join(US, "ACTION_WORKBOOK.pdf"), "workbook", "Action Workbook", wb_cover,
              f"Action Workbook · {TITLE} · {BRAND}", body_class="workbook", chapter_label=False)


if __name__ == "__main__":
    main()
