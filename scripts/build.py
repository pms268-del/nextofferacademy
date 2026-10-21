# -*- coding: utf-8 -*-
"""Build all deliverables for the Remote Work Playbook.

Outputs (repo root):
  REMOTE_WORK_DIRECTORY.csv, RESEARCH_EVIDENCE.csv,
  REMOTE_WORK_PLAYBOOK_ID.md, REMOTE_WORK_PLAYBOOK_ID.pdf
Run: python3 scripts/build.py
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

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import directory_data as D  # noqa: E402
import evidence_data as E  # noqa: E402

BUILD = os.path.join(ROOT, "build")
MANUSCRIPT = os.path.join(ROOT, "manuscript")
TITLE = "Remote Work Playbook 2026"
SUBTITLE = "Panduan Mendapatkan Pekerjaan Remote & Freelance Internasional dari Indonesia"
CHAPTERS = ["00_front.md", "01_bab1.md", "02_bab2.md", "03_bab3.md", "04_bab4.md",
            "05_bab5.md", "06_bab6.md", "07_lampiran.md"]
CHAPTER_IDS = {"bab1": 1, "bab2": 2, "bab3": 3, "bab4": 4, "bab5": 5, "bab6": 6}


# ----------------------------------------------------------------- CSV
def write_csvs(directory, evidence):
    with open(os.path.join(ROOT, "REMOTE_WORK_DIRECTORY.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=D.FIELDS)
        w.writeheader()
        w.writerows(directory)
    with open(os.path.join(ROOT, "RESEARCH_EVIDENCE.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=E.FIELDS)
        w.writeheader()
        w.writerows(evidence)


# ----------------------------------------------------------------- Markdown helpers
def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def directory_table(rows, cat_prefix):
    sel = [r for r in rows if r["kategori"].startswith(cat_prefix)]
    # Freelance platforms rarely advertise pay, so show fees instead.
    money_key, money_label = (("biaya_pembayaran", "Biaya platform & pembayaran") if cat_prefix == "B."
                              else ("bayaran_diiklankan", "Bayaran diiklankan"))
    # Dash counts set pandoc's relative column widths.
    out = [f"| # | Platform | Jenis pekerjaan | Indonesia? | {money_label} | Bukti |",
           "|--|-----------|--------------------|--------|---------------------------|-----|"]
    for r in sel:
        out.append("| {id} | [{p}]({u}) | {j} | **{e}** | {b} | {k} |".format(
            id=r["id"].replace("RW", ""), p=cell(r["platform"]), u=r["url"],
            j=cell(r["jenis_pekerjaan"]), e=cell(r["eligible_indonesia"]),
            b=cell(r[money_key]), k=cell(r["kekuatan_bukti"])))
    out.append("")
    out.append(f"*{len(sel)} platform. Proses seleksi, biaya/pembayaran, cakupan, dan sumber lengkap ada di Lampiran A.*")
    return "\n".join(out)


def directory_cards(rows):
    parts = []
    current = None
    for r in rows:
        if r["kategori"] != current:
            current = r["kategori"]
            parts.append(f"## {current} {{.unnumbered}}\n")
        srcs = " · ".join(f"[{i + 1}]({u.strip()})" for i, u in enumerate(r["sumber"].split("|")))
        fields = [
            ("Kategori", f"{r['kategori']} — {r['subkategori']}"),
            ("Website/URL", f"<{r['url']}>"),
            ("Jenis pekerjaan", r["jenis_pekerjaan"]),
            ("Skill dibutuhkan", r["skill_dibutuhkan"]),
            ("Indonesia eligible?", f"**{r['eligible_indonesia']}**"),
            ("Cakupan", r["cakupan"]),
            ("Tipe akses", r["tipe_akses"]),
            ("Bayaran diiklankan", r["bayaran_diiklankan"]),
            ("Proses seleksi", r["proses_seleksi"]),
            ("Biaya/Pembayaran", r["biaya_pembayaran"]),
            ("Diverifikasi", f"{r['tanggal_verifikasi']} · {r['metode_verifikasi']} · Bukti: {r['kekuatan_bukti']}"),
            ("Sumber", srcs),
        ]
        if r["catatan"]:
            fields.append(("Catatan", r["catatan"]))
        body = "\n".join(f"- **{k}:** {v}" for k, v in fields)
        parts.append(f"::: {{.card}}\n**{r['id']} · {r['platform']}**\n\n{body}\n:::\n")
    return "\n".join(parts)


def evidence_table(rows):
    out = ["| ID | Topik | Klaim | Jenis | Kekuatan | Sumber |",
           "|----|--------|-------------------------------|------|-----|----|"]
    for r in rows:
        out.append(f"| {r['id']} | {cell(r['topik'])} | {cell(r['klaim'])} | {r['jenis_bukti']} | "
                   f"{r['kekuatan']} | [tautan]({r['sumber']}) |")
    return "\n".join(out)


def load_prompts():
    text = open(os.path.join(ROOT, "AI_CAREER_PROMPTS.md"), encoding="utf-8").read()
    prompts = {}
    for m in re.finditer(r"^### (P\d\d) — .*?(?=^### P\d\d|^## |^---|\Z)", text, flags=re.S | re.M):
        prompts[m.group(1)] = m.group(0).strip()
    return prompts


def split_five(md):
    """Put each **Label?** line of .five boxes into its own paragraph."""
    def fix(block):
        lines = [ln for ln in block.group(1).strip().split("\n") if ln.strip()]
        return "::: {.five}\n" + "\n\n".join(lines) + "\n:::"
    return re.sub(r"::: \{\.five\}\n(.*?)\n:::", fix, md, flags=re.S)


def assemble_markdown(directory, evidence):
    prompts = load_prompts()
    counts = Counter(r["eligible_indonesia"] for r in directory)
    md = "\n\n".join(open(os.path.join(MANUSCRIPT, c), encoding="utf-8").read() for c in CHAPTERS)
    md = re.sub(r"\{\{COUNT:(.+?)\}\}", lambda m: str(counts.get(m.group(1), 0)), md)
    md = md.replace("{{TOTAL}}", str(len(directory)))
    md = md.replace("{{TABLE:A}}", directory_table(directory, "A."))
    md = md.replace("{{TABLE:B}}", directory_table(directory, "B."))
    md = md.replace("{{TABLE:C}}", directory_table(directory, "C."))
    md = md.replace("{{CARDS}}", directory_cards(directory))
    md = md.replace("{{EVIDENCE}}", evidence_table(evidence))

    def prompt_sub(m):
        key = m.group(1)
        if key not in prompts:
            raise KeyError(f"Prompt {key} not found in AI_CAREER_PROMPTS.md")
        return prompts[key]
    md = re.sub(r"\{\{PROMPT:(P\d\d)\}\}", prompt_sub, md)
    md = split_five(md)
    leftovers = re.findall(r"\{\{[A-Z]+[:A-Za-z0-9 –]*\}\}", md)
    if leftovers:
        raise ValueError(f"Unresolved placeholders: {leftovers}")
    header = (f"---\ntitle: \"{TITLE}\"\nsubtitle: \"{SUBTITLE}\"\nlang: id\n"
              f"date: \"Edisi Oktober 2026 — data diverifikasi 21 Oktober 2026\"\n---\n\n")
    return header + md


# ----------------------------------------------------------------- HTML
def md_to_html_fragment(md_path):
    return subprocess.run(
        ["pandoc", md_path, "-f", "markdown+fenced_divs+pipe_tables+task_lists+autolink_bare_uris",
         "-t", "html5", "--wrap=none"],
        check=True, capture_output=True, text=True).stdout


def decorate(fragment):
    soup = BeautifulSoup(fragment, "html.parser")
    # Chapter labels + page breaks
    for h1 in soup.find_all("h1"):
        cls = h1.get("class", [])
        num = CHAPTER_IDS.get(h1.get("id"))
        wrapper = soup.new_tag("div", attrs={"class": "chapter-start"})
        h1.insert_before(wrapper)
        if num:
            label = soup.new_tag("div", attrs={"class": "chapter-label"})
            label.string = f"BAB {num}"
            wrapper.append(label)
        wrapper.append(h1.extract())
        if "unnumbered" in cls:
            wrapper["class"] = wrapper["class"] + ["front"] if isinstance(wrapper["class"], list) else ["chapter-start", "front"]
    # Prompt headings: mark following code block
    for pre in soup.find_all("pre"):
        pre["class"] = pre.get("class", []) + ["prompt"]
    # External links open in new tab (PDF ignores, HTML preview benefits)
    for a in soup.find_all("a", href=True):
        if a["href"].startswith("http"):
            a["rel"] = "noopener"
    return soup


def build_toc(soup, pages=None):
    items = []
    for h in soup.find_all(["h1", "h2"]):
        hid = h.get("id")
        if not hid:
            continue
        if h.find_parent("div", class_="card"):
            continue
        # skip h2 inside appendix A (category headings) and front matter
        level = 1 if h.name == "h1" else 2
        parent_h1 = h.find_previous("h1") if level == 2 else h
        p1id = parent_h1.get("id") if parent_h1 else ""
        if level == 2 and p1id in ("pendahuluan", "lampiran-a", "lampiran-b", "lampiran-c", "tentang"):
            continue
        text = h.get_text(" ", strip=True)
        num = CHAPTER_IDS.get(hid)
        if num:
            text = f"Bab {num} — {text}"
        pg = (pages or {}).get(hid, "000")
        items.append((level, hid, text, pg))
    lis = []
    for level, hid, text, pg in items:
        lis.append(f'<li class="toc-l{level}"><a href="#{hid}"><span class="toc-text">{html.escape(text)}</span>'
                   f'<span class="toc-dots"></span><span class="toc-page">{pg}</span></a></li>')
    return ('<nav class="toc" id="daftar-isi"><h1 class="toc-title">Daftar Isi</h1><ul>'
            + "".join(lis) + "</ul></nav>"), [i[1] for i in items]


def page_html(body, toc_html):
    css = open(os.path.join(ROOT, "scripts", "style.css"), encoding="utf-8").read()
    return f"""<!doctype html>
<html lang="id"><head><meta charset="utf-8">
<title>{TITLE}</title>
<meta name="author" content="Remote Work Playbook Indonesia">
<meta name="description" content="{SUBTITLE}">
<style>{css}</style></head>
<body>
{toc_html}
<main>{body}</main>
</body></html>"""


def cover_html(total):
    css = open(os.path.join(ROOT, "scripts", "style.css"), encoding="utf-8").read()
    return f"""<!doctype html><html lang="id"><head><meta charset="utf-8"><title>{TITLE}</title>
<style>{css}</style></head><body class="cover-body">
<section class="cover">
  <div class="cover-top">EDISI OKTOBER 2026 · DATA DIVERIFIKASI 21 OKTOBER 2026</div>
  <div class="cover-main">
    <div class="cover-kicker">PANDUAN KARIER</div>
    <h1 class="cover-title">Remote Work<br>Playbook 2026</h1>
    <div class="cover-rule"></div>
    <p class="cover-sub">{SUBTITLE}</p>
    <ul class="cover-facts">
      <li><b>{total}</b> platform terverifikasi</li>
      <li><b>18</b> prompt AI siap pakai</li>
      <li><b>44</b> soal latihan wawancara</li>
      <li><b>30</b> hari rencana aksi</li>
    </ul>
  </div>
  <div class="cover-bottom">
    <div>AI Training &amp; Evaluation · Project-Based Freelancing · International Remote Jobs</div>
    <div class="cover-url">Direktori hidup: [LIVE DIRECTORY URL]</div>
  </div>
</section></body></html>"""


def render(html_path, pdf_path, footer=True):
    env = dict(os.environ, NODE_PATH="/opt/node22/lib/node_modules")
    args = ["node", os.path.join(ROOT, "scripts", "render_pdf.js"), html_path, pdf_path]
    args += ["--footer", f"{TITLE} · Panduan Remote & Freelance Internasional dari Indonesia"] if footer else ["--no-footer"]
    subprocess.run(args, check=True, env=env)


def heading_pages(pdf_path, toc_ids):
    """Map heading id -> 1-based page number using the TOC link annotations."""
    reader = PdfReader(pdf_path)
    page_index = {p.indirect_reference.idnum: i for i, p in enumerate(reader.pages)}
    found = []
    for pno, page in enumerate(reader.pages[:6]):
        for annot in page.get("/Annots", []) or []:
            a = annot.get_object()
            if a.get("/Subtype") != "/Link":
                continue
            dest = a.get("/Dest")
            if dest is None and "/A" in a:
                act = a["/A"].get_object()
                dest = act.get("/D")
            if dest is None:
                continue
            if isinstance(dest, (str, bytes)) or hasattr(dest, "startswith"):
                d = reader.named_destinations.get(str(dest))
                if d is None:
                    continue
                target = reader.get_destination_page_number(d)
            else:
                ref = dest[0]
                target = page_index.get(ref.idnum)
            if target is None:
                continue
            rect = [float(x) for x in a["/Rect"]]
            found.append((pno, -rect[3], target + 1))
    found.sort()
    pages = {}
    for hid, (_, _, pg) in zip(toc_ids, found):
        pages[hid] = pg
    return pages, len(found)


def main():
    os.makedirs(BUILD, exist_ok=True)
    directory = D.rows_as_dicts()
    evidence = E.rows_as_dicts()
    write_csvs(directory, evidence)

    md = assemble_markdown(directory, evidence)
    md_out = os.path.join(ROOT, "REMOTE_WORK_PLAYBOOK_ID.md")
    with open(md_out, "w", encoding="utf-8") as f:
        f.write(md)

    soup = decorate(md_to_html_fragment(md_out))
    body = str(soup)

    # Pass 1: placeholder page numbers
    toc1, ids = build_toc(soup)
    p1_html = os.path.join(BUILD, "pass1.html")
    p1_pdf = os.path.join(BUILD, "pass1.pdf")
    open(p1_html, "w", encoding="utf-8").write(page_html(body, toc1))
    render(p1_html, p1_pdf)
    pages, nlinks = heading_pages(p1_pdf, ids)
    print(f"TOC entries: {len(ids)}, TOC links found: {nlinks}")
    if nlinks != len(ids):
        print("WARNING: TOC link count mismatch; page numbers may be off", file=sys.stderr)

    # Pass 2: real page numbers
    toc2, _ = build_toc(soup, pages)
    body_html = os.path.join(BUILD, "playbook.html")
    body_pdf = os.path.join(BUILD, "body.pdf")
    open(body_html, "w", encoding="utf-8").write(page_html(body, toc2))
    render(body_html, body_pdf)

    cover_path = os.path.join(BUILD, "cover.html")
    cover_pdf = os.path.join(BUILD, "cover.pdf")
    open(cover_path, "w", encoding="utf-8").write(cover_html(len(directory)))
    render(cover_path, cover_pdf, footer=False)

    writer = PdfWriter(clone_from=body_pdf)
    writer.insert_page(PdfReader(cover_pdf).pages[0], 0)
    writer.add_metadata({"/Title": f"{TITLE}: {SUBTITLE}", "/Author": "Remote Work Playbook Indonesia",
                         "/Subject": "Panduan karier remote & freelance internasional", "/Lang": "id"})
    out = os.path.join(ROOT, "REMOTE_WORK_PLAYBOOK_ID.pdf")
    with open(out, "wb") as f:
        writer.write(f)
    print(f"Pages: {len(PdfReader(out).pages)} -> {out}")


if __name__ == "__main__":
    main()
