# Remote Work Playbook 2026 (Indonesia)

*Panduan Mendapatkan Pekerjaan Remote & Freelance Internasional dari Indonesia*. Sebuah panduan karier berbasis riset dalam Bahasa Indonesia.

## Deliverables

| File | Isi |
|---|---|
| `REMOTE_WORK_PLAYBOOK_ID.pdf` | Panduan lengkap siap terbit (A4, daftar isi yang bisa diklik, bookmark PDF, tautan sumber aktif) |
| `REMOTE_WORK_PLAYBOOK_ID.md` | Naskah gabungan yang bisa diedit (dihasilkan dari `manuscript/`) |
| `REMOTE_WORK_DIRECTORY.csv` | Basis data 102 platform terverifikasi (siap dipakai untuk situs web) |
| `RESEARCH_EVIDENCE.csv` | 87 klaim dengan jenis bukti, kekuatan, tanggal, dan sumber |
| `AI_CAREER_PROMPTS.md` | 18 prompt CV, lamaran, wawancara, dan networking |
| `ACTION_WORKBOOK.md` | Checklist & tracker (lamaran, networking, pendapatan, review mingguan) |
| `FACT_CHECK.md` | Laporan verifikasi, koreksi, dan celah riset |
| `research/00_RESEARCH_LOG.md` | Catatan riset mentah per sumber |

## Cara mengedit & membangun ulang

Sumber kebenaran:
- Teks bab: `manuscript/*.md`
- Data direktori: `scripts/directory_data.py`
- Data bukti: `scripts/evidence_data.py`
- Prompt: `AI_CAREER_PROMPTS.md` (disisipkan ke bab lewat penanda `{{PROMPT:Pxx}}`)
- Desain: `scripts/style.css`

```bash
python3 scripts/build.py   # menghasilkan CSV, MD gabungan, dan PDF
```

Kebutuhan: Python 3 (`beautifulsoup4`, `pypdf`), `pandoc`, Node.js dengan Playwright + Chromium.

Ganti `[LIVE DIRECTORY URL]` setelah situs direktori siap, lalu jalankan build ulang.
