# Fact-Check Report — Remote Work Playbook 2026

**Tanggal verifikasi:** 21 Oktober 2026
**Cakupan:** `REMOTE_WORK_PLAYBOOK_ID.pdf/.md`, `REMOTE_WORK_DIRECTORY.csv` (102 baris), `RESEARCH_EVIDENCE.csv` (87 baris), `AI_CAREER_PROMPTS.md`, `ACTION_WORKBOOK.md`
**Log riset mentah:** `research/00_RESEARCH_LOG.md` (catatan per sumber, ±90 pencarian)

---

## 1. Metode & keterbatasan (wajib dibaca)

| Aspek | Yang dilakukan | Keterbatasan |
|---|---|---|
| Pengumpulan sumber | ±90 pencarian web terarah (halaman resmi, help center, papan lowongan Lever/Greenhouse, media, agregator, Reddit/Glassdoor/Trustpilot/Blind/Upwork Community) | — |
| Akses halaman | **Lingkungan riset memblokir pengunduhan halaman secara langsung** (curl ditolak proxy; fetch gagal DNS). Verifikasi dilakukan lewat **indeks dan cuplikan mesin pencari**, bukan dengan membuka halaman secara langsung | Isi halaman bisa sudah berubah sejak diindeks. Status "Apply" di listing **tidak** dicek secara langsung |
| Pengecekan tautan | Setiap URL di naskah ditelusuri ke log riset/data secara otomatis (327 URL unik; 0 yang tidak tertelusur setelah perbaikan) | Tidak ada pengecekan HTTP status. Tautan bisa mati atau dialihkan setelah tanggal riset |
| Kolom "Website/URL" direktori | Deep link hanya dipakai jika muncul di hasil pencarian. Selain itu dipakai domain utama platform | 15 deep link tebakan diganti dengan domain utama atau tautan bersumber saat fact-check |
| Reddit | Beberapa thread ditemukan lewat situs mirror (redlib dan sejenisnya). Naskah mengutip path kanonis reddit.com dengan ID post yang sama | Isi thread bisa sudah dihapus atau disunting |
| Tanggal verifikasi | Kolom `tanggal_verifikasi` = tanggal pengecekan (2026-10-21), **bukan** tanggal listing dibuat. Tanggal listing dicatat di kolom catatan atau bukti bila diketahui | Beberapa listing berasal dari 2024–2025 dan mungkin sudah ditutup |

## 2. Aturan editorial yang dipatuhi

- [x] Tidak ada lowongan, testimoni, angka gaji, URL, atau pertanyaan wawancara yang dikarang. Semua contoh soal, contoh jawaban, proposal, dan sebelum/sesudah **diberi label buatan editorial/fiktif**.
- [x] Informasi yang tidak terkonfirmasi ditulis **"Belum terverifikasi"** (43 baris direktori memakai label ini untuk kelayakan Indonesia).
- [x] Fakta resmi, pengalaman individu, dan rekomendasi editorial dibedakan dengan label di naskah dan kolom `jenis_bukti` di CSV.
- [x] Anekdot tidak disajikan sebagai tingkat keberhasilan. Angka "acceptance rate" hanya dikutip jika dinyatakan resmi oleh platform (Toptal <3%, Codeable ±2%, Lemon.io 1,2%) dan diberi atribusi.
- [x] Tidak ada materi assessment bocoran atau saran curang. Ada peringatan eksplisit tentang larangan memakai AI dalam assessment/tugas.
- [x] Materi Harvard/Stanford hanya dirujuk sebagai metode, dengan tautan. Tidak ada teks atau branding yang disalin.
- [x] Tidak ada klaim bahwa optimasi ATS menjamin diterima.

## 3. Klaim kunci yang diverifikasi (sampel prioritas tinggi)

| Klaim di naskah | Status | Sumber |
|---|---|---|
| Mercor membayar via Stripe Connect dan Indonesia ada di daftar negara Stripe | ✅ Resmi | talent.docs.mercor.com/policies/supported-countries |
| Mercor: payout mingguan (Rabu), USD, rekening atas nama sendiri, tanpa dompet digital | ✅ Resmi | talent.docs.mercor.com/how-to/payments |
| Mercor: AI interview ±20 menit, practice gratis, retake ≤3× sebelum submit | ✅ Resmi | talent.docs.mercor.com/how-to/prepare-for-ai-interview |
| Listing Mercor berbahasa Indonesia & tarifnya | ✅ Listing resmi (status aktif tidak dicek langsung) | work.mercor.com/jobs/… |
| Onboarding Outlier 30–90 menit; tahapan umum | ✅ Blog resmi (Agu 2025) | outlier.ai/blog/… |
| Prolific tidak mencakup Indonesia | ✅ Resmi | participant-help.prolific.com |
| Rev hanya 9 negara | ✅ Resmi | freelancer.rev.com |
| User Interviews: daftar negara APAC tanpa Indonesia | ✅ Resmi | userinterviews.com/support/participant-countries |
| Adobe Stock: Payoneer wajib untuk Indonesia, minimum US$25 | ✅ Resmi | helpx.adobe.com |
| Shutterstock: PayPal/Skrill/Payoneer, ambang US$25–2000 | ✅ Resmi | submit.shutterstock.com/help |
| Toptal <3%, tahapan, 3–8 minggu | ✅ Resmi | toptal.com/top-3-percent |
| Codeable 6 tahap, ±2% | ✅ Resmi | help.codeable.io |
| Upwork Freelancer Plus US$19,99/bulan + 100 Connects | ✅ Resmi | upwork.com/resources/is-upwork-free |
| Upwork fee freelancer variabel 0–15% | ⚠️ Pihak ketiga (konsisten di beberapa sumber) | golance.com; jobbers.io |
| RWS & Welo Data: listing Indonesia & tarif | ✅ Listing resmi Lever/iCIMS | jobs.lever.co/rws/…; jobs.lever.co/weloglobal/… |
| Remotasks ditutup di beberapa negara (2024) | ✅ Media kredibel | restofworld.org |
| Kontraktor dikeluarkan karena memakai AI (via Mercor) | ✅ Media (melaporkan 404 Media) | ibtimes.co.uk; aiweekly.co |
| Modus penipuan deposit, Satgas PASTI, kontak pelaporan | ✅ Resmi/media | bisnis.com; investortrust.id; booklet OJK |
| Kewajiban pajak freelancer | ✅ Resmi DJP | pajak.go.id |
| BPS: rata-rata pendapatan pekerja bebas Rp1,68 juta (Agu 2025) | ✅ Data BPS via Databoks | databoks.katadata.co.id |
| LinkedIn #OpenToWork ~40% lebih banyak InMail | ✅ Resmi (data 2020, berpotensi usang) | blog.linkedin.com |
| Jumlah per label kelayakan di naskah | ✅ Dihitung otomatis dari data saat build | scripts/build.py |

## 4. Koreksi yang dilakukan selama fact-check

1. **Test IO dihapus dari direktori.** Sumber yang tersedia hanya menyebutnya sekilas, dan URL sumber yang semula dipakai ternyata halaman Testlio. Direktori berkurang dari 103 menjadi 102 platform.
2. **15 deep link tebakan diganti** dengan domain utama atau tautan bersumber (contoh: halaman karier TELUS, RWS, Lionbridge, Preply, Cambly, Testlio, UserTesting, Uber AI Solutions).
3. **Klaim Wellfound di Temuan #6 diperhalus.** Kalimat diubah dari "memakai wawancara AI" menjadi "memperkenalkan panggilan percakapan terekam yang ikut terkirim bersama lamaran", sesuai sumbernya.
4. **Semua angka jumlah platform dibuat dinamis** (dihitung dari data saat build) agar tidak ada angka yang tidak konsisten antara sampul, pendahuluan, dan Bab 1.
5. **Pustaka prompt ditulis ulang ke Bahasa Indonesia** (draf pertama tidak sengaja ditulis dalam bahasa Inggris).

## 5. Celah riset yang belum terselesaikan

| # | Celah | Dampak | Tindakan yang disarankan |
|---|---|---|---|
| 1 | **Halluminate:** tidak ditemukan program kontributor/AI training yang terbuka untuk Indonesia; yang ditemukan hanya lowongan full-time di SF | Bab 2 tidak memuat alur seleksi Halluminate | Hubungi Halluminate atau pantau halaman karier mereka |
| 2 | **DataAnnotation:** daftar negara resmi tidak dipublikasikan; label "Tidak" berdasar beberapa sumber pihak ketiga | Kemungkinan kecil salah klasifikasi | Cek dropdown negara di halaman pendaftaran resmi |
| 3 | **Outlier:** daftar negara resmi & tarif terkini untuk Indonesia; metode pembayaran hanya dari pihak ketiga | Tarif di naskah berasal dari listing 2024–2025 | Cek dashboard/help center Outlier |
| 4 | **Alignerr & micro1:** kelayakan Indonesia dan metode pembayaran untuk Indonesia | Label "Belum terverifikasi" | Tanyakan saat onboarding; cek FAQ pembayaran Labelbox |
| 5 | **Mindrift/Toloka, Clickworker, DataForce, LXT, Defined.ai, Pareto, Surge, iMerit, Rex.zone, Lionbridge:** kelayakan Indonesia | Label "Belum terverifikasi" | Uji lewat form pendaftaran (tanpa VPN) |
| 6 | **Remotasks:** status di Indonesia setelah penutupan 2024 di beberapa negara | Ditandai berhati-hati | Pantau pemberitaan/pengumuman resmi |
| 7 | **Fee platform yang saling bertentangan:** PeoplePerHour, Fastwork, Guru, Braintrust (fee talenta), Contra (Pro), 99designs/DesignCrowd (data 2021) | Angka di tabel biaya bisa usang | Cek halaman harga resmi masing-masing |
| 8 | **Komisi Sribu** tidak ditemukan; **fee Projects.co.id** dari artikel lama | Kolom biaya "Belum terverifikasi"/data lama | Cek syarat & ketentuan situs |
| 9 | **Alat AI (ChatGPT/Claude/Gemini):** model default dan batas akun gratis, karena sumber 2026 saling bertentangan | Naskah sengaja tidak menyebut nama model/batas spesifik | Cek halaman harga resmi saat membaca |
| 10 | **Yoodli:** harga Pro (US$8 vs US$15) dan dukungan bahasa | Ditulis sebagai "sumber bertentangan" | Cek yoodli.ai/pricing |
| 11 | **Google Interview Warmup & Gemini Live (bahasa Indonesia):** status 2026 | Sumber utama berasal dari 2022/2024 | Uji langsung |
| 12 | **Pajak:** klaim perubahan jalur PPh Final 0,5% untuk pekerja bebas (PP 20/2026) hanya dari satu sumber non-resmi | Ditulis "Belum terverifikasi" | Cek peraturan.go.id / pajak.go.id |
| 13 | **Panduan resmi LinkedIn tentang Boolean search** tidak ditemukan; dipakai sumber pihak ketiga | Detail operator bisa berbeda per jenis akun | Uji langsung di LinkedIn |
| 14 | **Panduan karier resmi HBS** dan **panduan informational interview Stanford CareerEd** tidak muncul di pencarian; dipakai materi kantor Harvard lain (FAS, GSE, HMS) dan Stanford Alumni/GSB/CDC | Rujukan metodologis tetap dari Harvard/Stanford, tetapi dari unit yang berbeda | Opsional: tambahkan rujukan langsung bila tersedia |
| 15 | **Status aktif setiap listing** (tombol Apply) tidak dicek langsung karena keterbatasan akses | Sebagian listing mungkin sudah ditutup | Jalankan pengecekan tautan dari jaringan tanpa pembatasan sebelum publikasi web |
| 16 | **Respondent, Test IO, TranscribeMe, Userlytics:** daftar negara untuk kontributor | Belum terverifikasi / dihapus | Cek halaman pendaftaran |

## 6. Rekomendasi sebelum publikasi

1. Jalankan pengecek tautan otomatis (misalnya `lychee` atau skrip `requests`) dari jaringan tanpa pembatasan, lalu perbarui baris yang tautannya mati.
2. Isi `[LIVE DIRECTORY URL]` di naskah (`manuscript/*.md`, `scripts/build.py`) setelah situs siap, lalu jalankan `python3 scripts/build.py`.
3. Jadwalkan pembaruan direktori setiap bulan. Kolom `tanggal_verifikasi` dan `kekuatan_bukti` di CSV dirancang untuk itu.
4. Mintalah satu pembaca dengan latar konsultan pajak untuk meninjau Bab 6 bagian pajak.
