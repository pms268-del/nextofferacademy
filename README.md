# Next Offer Academy — Remote Work Playbook 2026

Panduan karier praktis dalam Bahasa Indonesia untuk mendapatkan pekerjaan remote dan freelance internasional dari Indonesia.

## File untuk pembaca

| File | Isi |
|---|---|
| `REMOTE_WORK_PLAYBOOK_ID.pdf` / `.docx` | Panduan karier (PDF siap terbit + Word yang bisa diedit) |
| `ACTION_WORKBOOK.pdf` / `.docx` | Workbook: roadmap 7 hari, tracker 30 hari, tracker lamaran/networking, kartu anti-penipuan |
| `AI_CAREER_PROMPTS.md` | Semua prompt (workflow lamaran, freelance, wawancara, networking) |
| `REMOTE_WORK_DIRECTORY.csv` | Database lengkap 157 platform (kolom `kelompok` = pengelompokan di Bab 1) untuk spreadsheet & website |

## File internal (akurasi editorial)

`internal/` berisi log riset, catatan sumber (`RESEARCH_EVIDENCE.csv`), laporan fact-check versi pertama, dan catatan editorial revisi.

## Mengedit & membangun ulang

- Teks panduan: `manuscript/00_…08_*.md` · Workbook: `manuscript/workbook.md`
- Prompt: `AI_CAREER_PROMPTS.md` (disisipkan lewat penanda `{{PROMPT:W1}}` dan sejenisnya)
- Data direktori: `scripts/directory_data.py` · Desain: `scripts/style.css`
- Domain website: konstanta `WEBSITE` di `scripts/build.py`

```bash
python3 scripts/build.py   # menghasilkan PDF, DOCX, MD gabungan, dan CSV
```

Kebutuhan: Python 3 (`beautifulsoup4`, `pypdf`, `pikepdf`, `python-docx`), `pandoc`, Node.js dengan Playwright + Chromium.
