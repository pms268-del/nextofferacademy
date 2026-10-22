# Workflow CV & Lamaran dengan AI {#bab3}

Dengan workflow ini, satu lamaran yang benar-benar disesuaikan butuh sekitar 20–30 menit, bukan 2 jam. Hasil akhirnya: CV khusus lowongan, cover letter, pesan untuk recruiter, dan PDF yang siap diunggah.

::: {.flow}
1. Unggah CV + tempel lowongan
2. AI menganalisis kebutuhan & kecocokan
3. CV yang disesuaikan
4. Cover letter & pesan singkat
5. Review akhir
6. Ekspor PDF & catat di tracker
:::

**Prinsip yang tidak bisa ditawar:** AI hanya boleh menyusun ulang dan mempertajam fakta yang memang Anda miliki. AI tidak boleh menambah pengalaman, angka, atau sertifikat. Pewawancara dan AI interviewer akan menggali isi CV Anda.

## Alat yang dipakai

| Alat | Peran dalam workflow | Catatan |
|---|---|---|
| **ChatGPT** | Analisis lowongan, CV, cover letter, simulasi wawancara (bisa dengan suara) | Versi gratis cukup untuk workflow ini |
| **Claude** | Sangat baik untuk dokumen panjang (CV + lowongan) dan review | Versi gratis memiliki batas pemakaian harian |
| **Gemini** | Alternatif untuk analisis; Gemini Live untuk latihan bicara | Integrasi langsung di Google Docs memerlukan paket berbayar |
| **Google Docs** | Menyusun CV satu kolom dan ekspor PDF | Gratis |
| **Canva** | Portofolio dan studi kasus visual | Untuk CV utama, pilih template satu kolom yang sederhana |

Cukup pakai **satu** asisten AI secara konsisten. Fitur *Projects* (ChatGPT/Claude) atau *Gems* (Gemini) memudahkan Anda karena instruksi dan master CV cukup disimpan sekali.

## Persiapan sekali saja: master CV

Buat satu dokumen **master CV** (boleh 3–4 halaman) berisi semua pengalaman, proyek, tools, angka, dan pencapaian Anda. Dokumen ini tidak pernah dikirim ke siapa pun. Semua CV yang Anda kirim diambil dari sini.

Untuk setiap pengalaman, tulis:

- Apa masalah atau tugasnya?
- Apa yang **Anda** kerjakan, termasuk tools yang dipakai?
- Apa hasilnya? Angka (waktu, jumlah, persen, rupiah) jika ada.

## Langkah 1 — Pasang asisten lamaran

Tempel prompt ini sekali di Project/Gem, atau di awal percakapan baru.

{{PROMPT:W1}}

## Langkah 2 — Analisis lowongan

{{PROMPT:W2}}

## Contoh nyata: dari lowongan sampai lamaran

Contoh di bawah menunjukkan hasil yang dihasilkan asisten AI ketika workflow ini dijalankan. CV dan lowongan di contoh ini **fiktif**, dibuat untuk ilustrasi.

::: {.sample}
**Input — potongan master CV (Rina, analis data, 3 tahun pengalaman)**

> **Data Analyst, PT Niaga Digital (e-commerce), Jakarta, 2023–sekarang**
>
> - Bikin laporan penjualan mingguan dari 3 spreadsheet regional; persiapan sekitar 6 jam, setelah pakai BigQuery + Looker Studio jadi sekitar 1 jam
> - Menulis dan me-review query SQL untuk tim marketing, sekitar 50 query/bulan
> - Bikin checklist review query, keluhan salah data dari tim sales berkurang
> - Presentasi insight bulanan ke manajer regional (bahasa Inggris)
>
> Tools: SQL, BigQuery, Looker Studio, Python (pandas), Google Sheets. Bahasa: Indonesia (native), Inggris (IELTS 7.0)

**Input — potongan lowongan**

> *Remote Data Analyst (APAC) — Series B fintech, fully remote.* You'll own weekly business reporting, build self-serve dashboards, and partner with Growth on experiment analysis. Requirements: 2+ years SQL, BI tools (Looker/Tableau), stakeholder communication in English. Nice to have: Python, A/B testing. Location: Remote – APAC (UTC+7 to UTC+10).
:::

::: {.sample}
**Output Langkah 2 — analisis AI**

> **Ringkasan peran:** Analis yang memegang laporan bisnis mingguan dan membuat dashboard swalayan untuk tim, serta membantu tim Growth menganalisis eksperimen.
>
> | Persyaratan | Bukti di CV | Status |
> |---|---|---|
> | [WAJIB] 2+ tahun SQL | "Menulis dan me-review query SQL… 50 query/bulan" (3 tahun) | Kuat |
> | [WAJIB] BI tools | Looker Studio | Kuat (sebut "Looker Studio", jangan diklaim Looker) |
> | [WAJIB] Komunikasi stakeholder (Inggris) | Presentasi bulanan ke manajer regional, IELTS 7.0 | Kuat |
> | [NILAI TAMBAH] Python | pandas | Sedang |
> | [NILAI TAMBAH] A/B testing | BELUM ADA | Tanyakan: pernah menganalisis kampanye/eksperimen? |
>
> **Kata kunci:** weekly business reporting, self-serve dashboards, SQL, BigQuery, Looker Studio, stakeholder communication, Python, data quality.
> **Lokasi:** "Remote – APAC (UTC+7 to UTC+10)" → Indonesia (UTC+7) memenuhi syarat.
> **Tanda bahaya:** tidak ada.
> **Penilaian:** Layak dilamar. Kebutuhan utama (laporan mingguan + dashboard) sama persis dengan pengalaman Rina.
:::

## Langkah 3 — CV yang disesuaikan

{{PROMPT:W3}}

::: {.sample}
**Output Langkah 3 — bagian CV yang dihasilkan (dalam bahasa Inggris, sesuai lowongan)**

> **SUMMARY**
>
> Data analyst with 3 years in e-commerce, specialising in weekly business reporting and self-serve dashboards (SQL, BigQuery, Looker Studio). Experienced in presenting insights to regional managers in English. Based in Indonesia (UTC+7).
>
> **EXPERIENCE — Data Analyst, PT Niaga Digital (2023–Present)**
>
> - Automated weekly sales reporting across 3 regions by moving spreadsheets into BigQuery and a Looker Studio dashboard, cutting preparation time from ~6 hours to ~1 hour per week.
> - Wrote and reviewed ~50 SQL queries per month for the marketing team; introduced a query-review checklist that reduced data-error complaints from sales. [PERLU ANGKA: berapa keluhan per bulan sebelum dan sesudah?]
> - Presented monthly insights to regional managers in English, turning dashboard trends into recommended actions.
>
> **Yang diubah:** "laporan penjualan" ditulis sebagai *weekly business reporting* (istilah lowongan); dashboard ditonjolkan sebagai *self-serve*; Looker Studio tidak diklaim sebagai Looker; A/B testing tidak ditambahkan karena belum ada buktinya.
:::

Perhatikan bahwa AI meminta data yang belum ada (**[PERLU ANGKA]**) dan tidak mengarangnya. Jawab pertanyaannya, atau hapus klaim tersebut.

## Langkah 4 — Cover letter & pesan singkat

{{PROMPT:W4}}

::: {.sample}
**Output Langkah 4 — versi 80 kata untuk recruiter**

> Hi [Name], I've just applied for the Remote Data Analyst (APAC) role. Your focus on self-serve dashboards matches what I do every week: I moved our regional sales reporting into BigQuery and Looker Studio, cutting prep time from about six hours to one. I'm based in Jakarta (UTC+7), fully within your APAC hours, and comfortable presenting insights in English. I'd welcome the chance to discuss how I could support your Growth team. Thank you!
:::

## Langkah 5 — Review akhir

{{PROMPT:W5}}

Setelah review AI, lakukan **cek manual 2 menit**: semua angka, tanggal, nama tools, dan jabatan harus bisa Anda jelaskan dalam wawancara.

## Langkah 6 — Ekspor PDF yang terbaca sistem

| Lakukan | Hindari |
|---|---|
| Satu kolom, judul bagian standar | Dua kolom, tabel, text box, ikon, grafik "skill bar" |
| Font umum (Arial, Calibri) ukuran 10–12 pt | Teks di dalam gambar, font dekoratif |
| Kontak di bagian atas badan dokumen | Kontak di header/footer, foto (kecuali diminta), NIK |
| Google Docs → *File → Download → PDF* | Hasil scan atau "print to image" |
| Nama file: `Rina-Pratama_Data-Analyst_CV.pdf` | `CV_final_revisi3.pdf` |

**Tes cepat:** buka PDF Anda, tekan Ctrl+A lalu Ctrl+C, dan tempel ke Notepad. Jika teksnya berantakan atau tidak muncul, sistem rekrutmen juga akan kesulitan membacanya.

## Mengulang untuk banyak lamaran

1. **Satu Project/Gem untuk semua lamaran.** Master CV dan aturan tersimpan di sana, jadi Anda cukup menempelkan lowongan baru.
2. **Satu folder per lamaran** di Google Drive: `2026-11_Perusahaan_Peran`, berisi lowongan, CV PDF, dan cover letter.
3. **Gunakan mode cepat (W6)** untuk lowongan yang mirip.
4. **Catat setiap lamaran** di tracker Action Workbook: tanggal, versi CV, dan status.
5. **Setiap minggu,** lihat versi CV mana yang paling banyak mendapat panggilan, lalu jadikan versi itu dasar lamaran berikutnya.

{{PROMPT:W6}}

**Ritme realistis:** 3–5 lamaran yang benar-benar disesuaikan per hari lebih efektif daripada 30 lamaran dengan CV yang sama.

## Profil LinkedIn dalam 15 menit

{{PROMPT:N1}}

Pasang hasilnya di LinkedIn, aktifkan **Open to Work** (pilih "Recruiters only" jika Anda masih bekerja), lalu tambahkan 2–3 contoh kerja di bagian *Featured*.
