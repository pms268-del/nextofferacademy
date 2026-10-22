# -*- coding: utf-8 -*-
"""Build all Next Offer Academy deliverables.

Reader-facing outputs (repo root):
  REMOTE_WORK_PLAYBOOK_ID.pdf / .docx / .md   — career guide
  ACTION_WORKBOOK.pdf / .docx / .md           — workbook
  REMOTE_WORK_DIRECTORY.csv                   — full platform database (for the website)
Internal output:
  internal/RESEARCH_EVIDENCE.csv              — source records for editorial accuracy
Run: python3 scripts/build.py
"""
import csv
import html
import os
import re
import subprocess
import sys

from bs4 import BeautifulSoup
from docx import Document
from docx.shared import Pt, RGBColor
from pypdf import PdfReader, PdfWriter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import directory_data as D  # noqa: E402
import evidence_data as E  # noqa: E402

BUILD = os.path.join(ROOT, "build")
MANUSCRIPT = os.path.join(ROOT, "manuscript")
BRAND = "Next Offer Academy"
WEBSITE = "nextoveracademy.id"
TITLE = "Remote Work Playbook 2026"
SUBTITLE = "Panduan Mendapatkan Pekerjaan Remote & Freelance Internasional dari Indonesia"
GUIDE_CHAPTERS = ["00_pendahuluan.md", "01_peluang.md", "02_diterima.md", "03_workflow_cv.md",
                  "04_wawancara.md", "05_networking.md", "06_rencana.md", "07_keamanan.md",
                  "08_penutup.md"]
CHAPTER_IDS = {f"bab{i}": i for i in range(1, 8)}
NAVY = RGBColor(0x0B, 0x25, 0x45)


# ----------------------------------------------------------------- data
def write_csvs():
    with open(os.path.join(ROOT, "REMOTE_WORK_DIRECTORY.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=D.FIELDS)
        w.writeheader()
        w.writerows(D.rows_as_dicts())
    with open(os.path.join(ROOT, "internal", "RESEARCH_EVIDENCE.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=E.FIELDS)
        w.writeheader()
        w.writerows(E.rows_as_dicts())


def load_prompts():
    text = open(os.path.join(ROOT, "AI_CAREER_PROMPTS.md"), encoding="utf-8").read()
    prompts = {}
    for m in re.finditer(r"^### ([A-Z]\d) — .*?(?=^### [A-Z]\d|^## |^---|\Z)", text, flags=re.S | re.M):
        prompts[m.group(1)] = m.group(0).strip()
    return prompts


def resolve(md):
    prompts = load_prompts()

    def prompt_sub(m):
        if m.group(1) not in prompts:
            raise KeyError(f"Prompt {m.group(1)} not found in AI_CAREER_PROMPTS.md")
        return prompts[m.group(1)]
    md = re.sub(r"\{\{PROMPT:([A-Z]\d)\}\}", prompt_sub, md)
    md = md.replace("{{WEBSITE}}", WEBSITE)
    left = re.findall(r"\{\{[A-Z]+[:A-Z0-9]*\}\}", md)
    if left:
        raise ValueError(f"Unresolved placeholders: {left}")
    return md


def front_matter(title, subtitle):
    return (f"---\ntitle: \"{title}\"\nsubtitle: \"{subtitle}\"\nauthor: \"{BRAND}\"\n"
            f"lang: id\ndate: \"Edisi Oktober 2026\"\n---\n\n")


# ----------------------------------------------------------------- HTML / PDF
def md_to_html_fragment(md_path):
    return subprocess.run(
        ["pandoc", md_path, "-f", "markdown+fenced_divs+pipe_tables+task_lists",
         "-t", "html5", "--wrap=none"],
        check=True, capture_output=True, text=True).stdout


def decorate(fragment):
    soup = BeautifulSoup(fragment, "html.parser")
    for h1 in soup.find_all("h1"):
        num = CHAPTER_IDS.get(h1.get("id"))
        wrapper = soup.new_tag("div", attrs={"class": "chapter-start"})
        h1.insert_before(wrapper)
        if num:
            label = soup.new_tag("div", attrs={"class": "chapter-label"})
            label.string = f"BAB {num}"
            wrapper.append(label)
        wrapper.append(h1.extract())
    for pre in soup.find_all("pre"):
        pre["class"] = pre.get("class", []) + ["prompt"]
    return soup


def build_toc(soup, levels, pages=None):
    items = []
    for h in soup.find_all(["h1", "h2"][:levels]):
        hid = h.get("id")
        if not hid:
            continue
        if h.name == "h2":
            parent = h.find_previous("h1")
            if not parent or parent.get("id") not in CHAPTER_IDS:
                continue
        text = h.get_text(" ", strip=True)
        if hid in CHAPTER_IDS:
            text = f"Bab {CHAPTER_IDS[hid]} — {text}"
        items.append((1 if h.name == "h1" else 2, hid, text, (pages or {}).get(hid, "000")))
    lis = "".join(
        f'<li class="toc-l{lv}"><a href="#{hid}"><span class="toc-text">{html.escape(t)}</span>'
        f'<span class="toc-dots"></span><span class="toc-page">{pg}</span></a></li>'
        for lv, hid, t, pg in items)
    return f'<nav class="toc"><h1 class="toc-title">Daftar Isi</h1><ul>{lis}</ul></nav>', [i[1] for i in items]


def css():
    return open(os.path.join(ROOT, "scripts", "style.css"), encoding="utf-8").read()


def page_html(title, body, toc_html):
    return (f'<!doctype html><html lang="id"><head><meta charset="utf-8"><title>{title}</title>'
            f'<style>{css()}</style></head><body>{toc_html}<main>{body}</main></body></html>')


def cover_html(kicker, title_html, subtitle, facts):
    lis = "".join(f"<li><b>{n}</b>{t}</li>" for n, t in facts)
    return f"""<!doctype html><html lang="id"><head><meta charset="utf-8"><title>{BRAND}</title>
<style>{css()}</style></head><body class="cover-body"><section class="cover">
  <div class="cover-top"><span class="cover-brand">{BRAND.upper()}</span><span>EDISI OKTOBER 2026</span></div>
  <div class="cover-main">
    <div class="cover-kicker">{kicker}</div>
    <h1 class="cover-title">{title_html}</h1>
    <div class="cover-rule"></div>
    <p class="cover-sub">{subtitle}</p>
    <ul class="cover-facts">{lis}</ul>
  </div>
  <div class="cover-bottom"><div class="cover-url">{WEBSITE}</div></div>
</section></body></html>"""


def render(html_path, pdf_path, footer_text=None):
    env = dict(os.environ, NODE_PATH="/opt/node22/lib/node_modules")
    args = ["node", os.path.join(ROOT, "scripts", "render_pdf.js"), html_path, pdf_path]
    args += ["--footer", footer_text] if footer_text else ["--no-footer"]
    subprocess.run(args, check=True, env=env)


def heading_pages(pdf_path, toc_ids):
    """Map heading id -> page number by reading the TOC link annotations."""
    reader = PdfReader(pdf_path)
    page_index = {p.indirect_reference.idnum: i for i, p in enumerate(reader.pages)}
    found = []
    for pno, page in enumerate(reader.pages[:4]):
        for annot in page.get("/Annots", []) or []:
            a = annot.get_object()
            if a.get("/Subtype") != "/Link" or ("/A" in a and a["/A"].get("/URI")):
                continue
            dest = a.get("/Dest")
            if dest is None and "/A" in a:
                dest = a["/A"].get_object().get("/D")
            if dest is None:
                continue
            if isinstance(dest, str) or not hasattr(dest, "__getitem__"):
                target = reader.get_destination_page_number(reader.named_destinations[str(dest)])
            else:
                target = page_index.get(dest[0].idnum)
            if target is not None:
                found.append((pno, -float(a["/Rect"][3]), target + 1))
    found.sort()
    return {hid: pg for hid, (_, _, pg) in zip(toc_ids, found)}, len(found)


def build_pdf(md_path, name, cover, toc_levels, footer):
    soup = decorate(md_to_html_fragment(md_path))
    body = str(soup)
    toc1, ids = build_toc(soup, toc_levels)
    p1h, p1p = os.path.join(BUILD, f"{name}_pass1.html"), os.path.join(BUILD, f"{name}_pass1.pdf")
    open(p1h, "w", encoding="utf-8").write(page_html(name, body, toc1))
    render(p1h, p1p, footer)
    pages, n = heading_pages(p1p, ids)
    if n != len(ids):
        print(f"WARNING {name}: {n} TOC links for {len(ids)} entries", file=sys.stderr)
    toc2, _ = build_toc(soup, toc_levels, pages)
    bh, bp = os.path.join(BUILD, f"{name}.html"), os.path.join(BUILD, f"{name}_body.pdf")
    open(bh, "w", encoding="utf-8").write(page_html(name, body, toc2))
    render(bh, bp, footer)
    ch, cp = os.path.join(BUILD, f"{name}_cover.html"), os.path.join(BUILD, f"{name}_cover.pdf")
    open(ch, "w", encoding="utf-8").write(cover)
    render(ch, cp)
    writer = PdfWriter(clone_from=bp)
    writer.insert_page(PdfReader(cp).pages[0], 0)
    writer.add_metadata({"/Title": f"{TITLE} — {name.replace('_', ' ').title()}", "/Author": BRAND,
                         "/Subject": SUBTITLE, "/Lang": "id"})
    out = os.path.join(ROOT, f"{name}.pdf")
    with open(out, "wb") as f:
        writer.write(f)
    print(f"{name}.pdf: {len(PdfReader(out).pages)} pages")


# ----------------------------------------------------------------- DOCX
def reference_docx():
    path = os.path.join(BUILD, "reference.docx")
    subprocess.run(["pandoc", "-o", path, "--print-default-data-file", "reference.docx"], check=True)
    doc = Document(path)
    styles = doc.styles
    for name, size, bold, color in [("Normal", 10.5, False, None), ("Body Text", 10.5, False, None),
                                    ("First Paragraph", 10.5, False, None), ("Title", 26, True, NAVY),
                                    ("Subtitle", 14, False, NAVY), ("Heading 1", 18, True, NAVY),
                                    ("Heading 2", 13.5, True, NAVY), ("Heading 3", 11.5, True, NAVY)]:
        st = next((s for s in styles if s.name and s.name.lower() == name.lower()), None)
        if st is None:
            continue
        st.font.name = "Calibri"
        st.font.size = Pt(size)
        st.font.bold = bold
        if color:
            st.font.color.rgb = color
    doc.save(path)
    return path


def build_docx(md_path, name, toc):
    args = ["pandoc", md_path, "-f", "markdown+fenced_divs+pipe_tables+task_lists", "-o",
            os.path.join(ROOT, f"{name}.docx"), "--reference-doc", reference_docx()]
    if toc:
        args += ["--toc", "--toc-depth=2"]
    subprocess.run(args, check=True)
    print(f"{name}.docx written")


# ----------------------------------------------------------------- main
def main():
    os.makedirs(BUILD, exist_ok=True)
    write_csvs()
    footer = f"{BRAND} · {TITLE} · {WEBSITE}"

    guide_md = front_matter(TITLE, SUBTITLE) + resolve("\n\n".join(
        open(os.path.join(MANUSCRIPT, c), encoding="utf-8").read() for c in GUIDE_CHAPTERS))
    guide_path = os.path.join(ROOT, "REMOTE_WORK_PLAYBOOK_ID.md")
    open(guide_path, "w", encoding="utf-8").write(guide_md)
    build_pdf(guide_path, "REMOTE_WORK_PLAYBOOK_ID",
              cover_html("PANDUAN KARIER", "Remote Work<br>Playbook 2026", SUBTITLE,
                         [("3", "jalur peluang kerja"), ("Workflow", "CV & lamaran dengan AI"),
                          ("Bank", "latihan wawancara"), ("7 + 30", "hari rencana aksi")]),
              toc_levels=2, footer=footer)
    build_docx(guide_path, "REMOTE_WORK_PLAYBOOK_ID", toc=True)

    wb_md = front_matter("Action Workbook", f"Pendamping {TITLE}") + resolve(
        open(os.path.join(MANUSCRIPT, "workbook.md"), encoding="utf-8").read())
    wb_path = os.path.join(ROOT, "ACTION_WORKBOOK.md")
    open(wb_path, "w", encoding="utf-8").write(wb_md)
    build_pdf(wb_path, "ACTION_WORKBOOK",
              cover_html("ACTION WORKBOOK", "Rencana Aksi<br>& Tracker", f"Pendamping {TITLE}: {SUBTITLE}",
                         [("7", "hari roadmap"), ("30", "hari tracker progres"),
                          ("5", "tracker siap isi"), ("1", "kartu anti-penipuan")]),
              toc_levels=1, footer=f"{BRAND} · Action Workbook · {WEBSITE}")
    build_docx(wb_path, "ACTION_WORKBOOK", toc=False)


if __name__ == "__main__":
    main()
