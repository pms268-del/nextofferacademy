# -*- coding: utf-8 -*-
"""Build the Mercor guide in Bahasa Indonesia and English (MD, PDF, DOCX).

Reuses the Next Offer Academy pipeline in scripts/build.py.
Run: python3 mercor/build_mercor.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import build as B  # noqa: E402

EDITIONS = [
    {
        "src": "mercor_guide_id.md", "name": "PANDUAN_MERCOR_2026_ID", "chapters": 15,
        "title": "Cara Diterima di Mercor AI 2026",
        "subtitle": "Panduan Lengkap untuk Pelamar Indonesia dan Internasional",
        "cover_title": "Cara Diterima<br>di Mercor AI 2026", "kicker": "PANDUAN REKRUTMEN",
        "facts": [("15", "bab praktis"), ("6", "pilar strategi"),
                  ("1", "prompt pencocokan CV"), ("Harian", "rutinitas & tracker")],
        "labels": {"lang": "id", "chapter": "BAB", "toc_chapter": "Bab", "toc_title": "Daftar Isi",
                   "edition": "EDISI NOVEMBER 2026", "date": "Edisi November 2026"},
    },
    {
        "src": "mercor_guide_en.md", "name": "MERCOR_GUIDE_2026_EN", "chapters": 16,
        "title": "How to Get Hired at Mercor AI in 2026",
        "subtitle": "The Complete Guide for Indonesian and International Applicants",
        "cover_title": "How to Get Hired<br>at Mercor AI in 2026", "kicker": "RECRUITMENT GUIDE",
        "facts": [("15", "community-tested tactics"), ("16", "practical chapters"),
                  ("1", "CV-matching prompt"), ("Daily", "operating plan & tracker")],
        "labels": {"lang": "en", "chapter": "CHAPTER", "toc_chapter": "Chapter", "toc_title": "Contents",
                   "edition": "NOVEMBER 2026 EDITION", "date": "November 2026 edition"},
    },
]


def build_edition(e):
    B.CHAPTER_IDS = {f"m{i}": i for i in range(1, e["chapters"] + 1)}
    B.TOC_SUBSECTIONS = set()
    B.TITLE = e["title"]
    B.LABELS = e["labels"]
    src = os.path.join(ROOT, "mercor", "manuscript", e["src"])
    md = B.front_matter(e["title"], e["subtitle"]) + B.resolve(open(src, encoding="utf-8").read())
    md_path = os.path.join(ROOT, "mercor", f"{e['name']}.md")
    open(md_path, "w", encoding="utf-8").write(md)
    cover = B.cover_html(e["kicker"], e["cover_title"], e["subtitle"], e["facts"])
    B.build_pdf(md_path, e["name"], cover, toc_levels=1,
                footer=f"{B.BRAND} · {e['title']} · {B.WEBSITE}")
    B.build_docx(md_path, e["name"], toc=True)
    for ext in ("pdf", "docx"):
        os.replace(os.path.join(ROOT, f"{e['name']}.{ext}"), os.path.join(ROOT, "mercor", f"{e['name']}.{ext}"))


def main():
    os.makedirs(B.BUILD, exist_ok=True)
    for e in EDITIONS:
        build_edition(e)


if __name__ == "__main__":
    main()
