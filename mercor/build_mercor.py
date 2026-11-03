# -*- coding: utf-8 -*-
"""Build the Mercor guide (Bahasa Indonesia) as MD, PDF, and DOCX.

Reuses the Next Offer Academy pipeline in scripts/build.py.
Run: python3 mercor/build_mercor.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import build as B  # noqa: E402

TITLE = "Cara Diterima di Mercor AI 2026"
SUBTITLE = "Panduan Lengkap untuk Pelamar Indonesia dan Internasional"
NAME = "PANDUAN_MERCOR_2026_ID"


def main():
    os.makedirs(B.BUILD, exist_ok=True)
    # Chapter ids in the Mercor manuscript are m1..m15.
    B.CHAPTER_IDS = {f"m{i}": i for i in range(1, 16)}
    B.TOC_SUBSECTIONS = set()
    B.TITLE = TITLE
    src = os.path.join(ROOT, "mercor", "manuscript", "mercor_guide_id.md")
    md = B.front_matter(TITLE, SUBTITLE) + B.resolve(open(src, encoding="utf-8").read())
    md_path = os.path.join(ROOT, "mercor", f"{NAME}.md")
    open(md_path, "w", encoding="utf-8").write(md)
    cover = B.cover_html("PANDUAN REKRUTMEN", "Cara Diterima<br>di Mercor AI 2026", SUBTITLE,
                         [("15", "bab praktis"), ("6", "pilar strategi"),
                          ("1", "prompt pencocokan CV"), ("Harian", "rutinitas & tracker")])
    B.build_pdf(md_path, NAME, cover, toc_levels=1,
                footer=f"{B.BRAND} · {TITLE} · {B.WEBSITE}")
    os.replace(os.path.join(ROOT, f"{NAME}.pdf"), os.path.join(ROOT, "mercor", f"{NAME}.pdf"))
    B.build_docx(md_path, NAME, toc=True)
    os.replace(os.path.join(ROOT, f"{NAME}.docx"), os.path.join(ROOT, "mercor", f"{NAME}.docx"))


if __name__ == "__main__":
    main()
