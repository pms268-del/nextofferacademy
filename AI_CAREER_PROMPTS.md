# AI Career Prompts — Remote Work Playbook 2026

Kumpulan prompt siap pakai untuk ChatGPT, Claude, Gemini, atau asisten AI lain. Prompt ini mencakup CV, lamaran, wawancara, dan networking.

**Aturan penggunaan**

1. Ganti semua `[TEKS DALAM KURUNG SIKU]` dengan data Anda sendiri.
2. **Jangan pernah meminta AI mengarang pengalaman, angka, atau sertifikat.** Setiap prompt di bawah memuat aturan anti-fabrikasi. Jangan menghapusnya.
3. Hapus data sensitif (alamat rumah lengkap, NIK, slip gaji, dokumen klien yang bersifat rahasia) sebelum menempelkan apa pun ke alat AI.
4. Hasil AI adalah draf. Baca, periksa setiap fakta, lalu tulis ulang dengan suara Anda sendiri.
5. Platform AI training (misalnya Mercor, Outlier, Alignerr) **melarang penggunaan AI untuk mengerjakan assessment atau tugas**. Gunakan prompt ini hanya untuk *persiapan* dan *latihan*. Jangan pernah memakainya saat tes sedang berlangsung.

Versi terbaru pustaka prompt ini: `[LIVE DIRECTORY URL]`

---

## Bagian A — Analisis & Positioning

### P01 — Analisis Deskripsi Pekerjaan (JD Decoder)
**Kegunaan:** Sebelum menulis apa pun, uraikan apa yang sebenarnya diminta pemberi kerja.

```text
Bertindaklah sebagai senior recruiter dan analis karier.

Saya akan menempelkan satu deskripsi pekerjaan (JD). Analisis dan hasilkan:

1. Ringkasan peran dalam 3 kalimat: masalah utama apa yang akan diselesaikan orang ini.
2. Tabel dengan kolom: Persyaratan | Jenis (Wajib / Nilai tambah / Tersirat) | Bukti di JD (kutipan langsung) | Apa yang perlu saya buktikan.
3. 10 kata kunci/frasa terpenting (hard skill, tools, domain), diurutkan berdasarkan prioritas, beserta frekuensinya di JD.
4. Sinyal lokasi & kelayakan: apakah peran terbuka worldwide, dibatasi negara/zona waktu tertentu, atau mensyaratkan izin kerja lokal? Kutip kalimatnya. Jika tidak jelas, tulis "TIDAK JELAS — tanyakan ke recruiter".
5. Red flag atau risiko (misalnya bayaran tidak jelas, biaya di muka, permintaan chat via Telegram/WhatsApp, "deposit pelatihan").
6. 5 pertanyaan yang paling mungkin ditanyakan dalam wawancara untuk peran ini.

Aturan: Jangan menambahkan persyaratan yang tidak ada di JD. Jika ada yang ambigu, tandai "ASUMSI".

Bahasa jawaban: [Indonesia/Inggris]

JD:
"""
[TEMPEL JD]
"""
```

### P02 — Analisis Kesenjangan: CV vs JD
**Kegunaan:** Temukan bagian CV yang sudah cocok dengan pekerjaan dan bagian yang belum.

```text
Bertindaklah sebagai hiring manager untuk peran di bawah ini.

Bandingkan CV saya dengan JD. Hasilkan:
1. Skor Kecocokan (0–100) beserta alasannya, dipecah menjadi: hard skill, pengalaman domain, tools, bukti dampak, komunikasi.
2. Tabel: Persyaratan JD | Bukti di CV saya (kutipan) | Status (Kuat / Lemah / Tidak ada).
3. Untuk setiap item "Lemah": sarankan cara memperkuatnya HANYA dengan fakta yang sudah ada di CV saya.
4. Untuk setiap item "Tidak ada": katakan dengan jujur apakah itu (a) kesenjangan nyata yang perlu saya pelajari, atau (b) mungkin pengalaman yang saya punya tapi belum saya tulis — ajukan pertanyaan klarifikasi untuk (b).
5. Rencana aksi 14 hari untuk menutup 2 kesenjangan paling kritis (kursus gratis, proyek portofolio mini).

Aturan ketat: JANGAN mengarang pengalaman, angka, sertifikasi, atau jabatan. Jika informasinya tidak ada, tanyakan kepada saya.

JD:
"""
[TEMPEL JD]
"""

CV:
"""
[TEMPEL TEKS CV]
"""
```

### P03 — Identifikasi Kata Kunci & Istilah ATS
```text
Dari JD di bawah, ekstrak:
1. Kata kunci hard skill (tools, bahasa pemrograman, metodologi) — dalam bentuk persis seperti tertulis di JD (misalnya "Google Analytics 4", bukan "GA").
2. Sinonim/singkatan umum yang juga dipakai recruiter (misalnya "RLHF" ↔ "reinforcement learning from human feedback").
3. Kata kunci soft skill/perilaku.
4. Untuk setiap kata kunci: apakah muncul di CV saya? (Ya/Tidak/Hanya sinonim).
5. Rekomendasi: di bagian mana CV saya setiap kata kunci bisa ditempatkan secara alami (Ringkasan / Skills / bullet tertentu) — HANYA jika saya memang punya pengalamannya.

Jangan menyarankan "keyword stuffing" atau teks berwarna putih. ATS tidak menjamin diterima — tujuannya adalah kejelasan bagi mesin dan manusia.

JD: """[TEMPEL JD]"""
CV: """[TEMPEL CV]"""
```

---

## Bagian B — CV & Profil

### P04 — Bullet Point Berbasis Pencapaian (CAR/STAR)
```text
Bertindaklah sebagai editor resume yang terlatih dengan metode career office: mulai dengan kata kerja aksi, tunjukkan konteks, tindakan, dan hasil yang terukur (CAR: Context–Action–Result).

Berikut catatan mentah saya tentang sebuah peran/proyek. Tulis ulang menjadi 3–5 bullet point CV:
- Maksimal 2 baris per bullet, diawali kata kerja aksi yang kuat (dalam bahasa Inggris jika CV berbahasa Inggris).
- Cantumkan angka HANYA jika ada di catatan saya. Jika tidak ada angka, beri placeholder [PERLU DATA: …] dan satu pertanyaan untuk membantu saya menemukan angkanya (misalnya "berapa laporan per minggu?").
- Hindari frasa "bertanggung jawab atas" / "responsible for" / "duties included".
- Sesuaikan penekanan dengan kata kunci JD target berikut: [KATA KUNCI 1, KATA KUNCI 2, KATA KUNCI 3].

Lalu tampilkan tabel sebelum/sesudah dan jelaskan mengapa setiap versi lebih kuat.

Catatan mentah:
"""
[contoh: Kerja di tim finance, bikin laporan bulanan di Excel, bantu audit, kadang melatih anak magang]
"""
```

### P05 — Ringkasan Profesional (Professional Summary)
```text
Tulis 3 variasi ringkasan profesional (maksimal 3 kalimat / 60 kata per variasi) untuk CV yang menyasar: [PERAN] di [JENIS PERUSAHAAN: startup AI / platform AI training / agensi internasional].

Gunakan hanya fakta di bawah. Struktur: [Identitas + lama pengalaman] → [2 kekuatan paling relevan beserta buktinya] → [nilai untuk peran ini].
Variasi 1: formal. Variasi 2: ringkas dan teknis. Variasi 3: cocok untuk headline + summary Upwork/LinkedIn.

Dilarang: klise ("pekerja keras", "passionate", "team player") tanpa bukti, angka karangan, atau klaim pernah bekerja dengan perusahaan yang tidak pernah saya ajak bekerja sama.

Fakta saya:
- Pendidikan: [...]
- Pengalaman: [...]
- Tools/skill: [...]
- Pencapaian utama (dengan angka jika ada): [...]
- Bahasa: Indonesia (native), Inggris ([level/skor tes jika ada])
```

### P06 — Menyesuaikan CV untuk Satu Lowongan (One-JD Tailoring)
```text
Saya melamar untuk JD di bawah. Master CV saya terlampir.

Tugas:
1. Pilih 8–12 bullet paling relevan dari master CV saya untuk JD ini; urutkan berdasarkan relevansi (yang paling relevan lebih dulu di setiap peran).
2. Sunting kata-katanya agar memakai terminologi JD jika memang AKURAT (misalnya "evaluated LLM outputs" jika saya benar-benar pernah mengevaluasi output AI).
3. Sarankan bagian mana yang dihapus/dipadatkan agar CV muat 1 halaman (fresh graduate) atau 2 halaman (berpengalaman).
4. Hasilkan dalam format teks polos satu kolom dengan judul bagian standar: SUMMARY, SKILLS, EXPERIENCE, PROJECTS, EDUCATION, CERTIFICATIONS, LANGUAGES.
5. Daftarkan perubahan yang Anda buat beserta alasan masing-masing.

Anti-fabrikasi: jangan menambahkan tools, angka, jabatan, atau pemberi kerja yang tidak ada di master CV. Tandai apa pun yang Anda ragukan dengan [CEK].

JD: """[TEMPEL JD]"""
Master CV: """[TEMPEL MASTER CV]"""
```

### P07 — Cover Letter / Pesan Motivasi
```text
Tulis cover letter untuk posisi [PERAN] di [PERUSAHAAN] dalam bahasa [Inggris/Indonesia], maksimal 250 kata, 4 paragraf:
1. Pembuka: mengapa peran/perusahaan ini secara spesifik (gunakan 1 fakta spesifik dari JD/situs perusahaan yang saya tempelkan).
2. Bukti 1: pencapaian saya yang paling relevan, lengkap dengan konteks dan hasilnya.
3. Bukti 2: skill yang menjawab kebutuhan utama mereka + bagaimana saya akan berkontribusi dalam 30–60 hari pertama.
4. Penutup: ketersediaan (zona waktu WIB/UTC+7, jam yang bisa beririsan dengan tim mereka), ajakan tindak lanjut yang jelas.

Nada: profesional, spesifik, tidak berlebihan. Jangan mengulang isi CV baris per baris.
Anti-fabrikasi: gunakan hanya fakta di bawah.

JD / info perusahaan: """[TEMPEL]"""
Fakta saya: """[TEMPEL 3–5 PENCAPAIAN]"""
```

### P08 — Optimasi LinkedIn
```text
Bertindaklah sebagai strategis profil LinkedIn untuk kandidat yang menyasar pekerjaan remote internasional.

Input: profil saya saat ini + peran target.
Output:
1. 3 opsi headline (≤220 karakter) dengan formula: [Peran/Spesialisasi] | [Domain/Tools] | [Nilai/Bukti] | [Open to remote, UTC+7].
2. Bagian "About" (≤2.000 karakter): paragraf 1 siapa saya & masalah apa yang saya selesaikan; paragraf 2 bukti (2–3 pencapaian); paragraf 3 daftar skill/tools; paragraf 4 pekerjaan yang saya cari + ajakan tindak lanjut. Teks polos, tanpa emoji berlebihan.
3. Tulis ulang 2 entri Experience terbaru saya (masing-masing 3 bullet).
4. 15 Skills yang perlu ditambahkan, diurutkan berdasarkan prioritas (sesuai istilah yang dicari recruiter).
5. 3 ide konten Featured (portofolio, studi kasus, artikel).
6. 5 ide postingan yang bisa saya tulis bulan depan untuk membangun kredibilitas (berdasarkan pengalaman nyata).

Aturan anti-fabrikasi berlaku. Peran target: [PERAN]. Profil saat ini: """[TEMPEL]"""
```

### P09 — Profil Upwork / Fiverr
```text
Buat profil freelance untuk [Upwork / Fiverr] untuk jasa: [JASA SPESIFIK, misalnya "lokalisasi Indonesia–Inggris untuk aplikasi SaaS"].

Output:
1. Judul (Upwork: ≤70 karakter; judul gig Fiverr diawali "I will ...").
2. Overview/deskripsi: buka dengan masalah klien (2 kalimat — klien sering hanya membaca bagian awal), lalu solusi & proses, bukti (portofolio/hasil), apa saja yang termasuk, dan ajakan tindak lanjut.
3. Untuk Fiverr: 3 tingkat paket (Basic/Standard/Premium) dengan cakupan, jumlah revisi, dan waktu pengerjaan — harga akan saya tentukan sendiri; berikan pertimbangan rentang harga berdasarkan cakupan saja.
4. 5 item portofolio yang bisa saya buat dalam 1 minggu jika belum punya klien (proyek contoh yang realistis, diberi label jelas "contoh/inisiatif sendiri").
5. 10 tag pencarian yang relevan.
6. FAQ 5 butir yang menjawab keberatan umum klien.

Jangan menjanjikan hasil yang tidak bisa dijamin (misalnya "dijamin halaman 1 Google"). Fakta saya: """[TEMPEL]"""
```

### P10 — Positioning Portofolio (Studi Kasus)
```text
Bantu saya mengubah proyek ini menjadi studi kasus portofolio 1 halaman.

Struktur:
- Judul (hasilnya, bukan aktivitasnya)
- Konteks & masalah (2–3 kalimat)
- Peran saya (jujur: sendiri/tim, bagian mana yang saya kerjakan)
- Proses (3–5 langkah, tools yang dipakai)
- Hasil (angka jika ada; jika tidak, bukti kualitatif: umpan balik pengguna, tangkapan layar sebelum/sesudah)
- Yang saya pelajari / yang akan saya lakukan berbeda
- Tautan/demo

Jika proyek ini inisiatif sendiri atau contoh, tambahkan label "Proyek inisiatif sendiri" — jangan menyamarkannya sebagai pekerjaan klien.
Jika memuat data klien, beri saran cara menganonimkannya.

Catatan proyek: """[TEMPEL]"""
```

### P11 — Review Kualitas Lamaran (Red-Team)
```text
Bertindaklah sebagai 3 reviewer sekaligus: (1) recruiter skeptis yang membaca selama 30 detik, (2) hiring manager yang ahli di bidang [BIDANG], (3) parser ATS.

Tinjau paket lamaran saya (CV + cover letter/proposal) terhadap JD:
1. Recruiter (30 detik): apa yang tertangkap, apa yang terlewat, apakah dia akan lanjut membaca? (Ya/Tidak + alasan)
2. Hiring manager: 3 klaim paling lemah, pertanyaan atau keraguan yang muncul, inkonsistensi.
3. ATS: elemen yang kemungkinan salah terbaca (tabel, kolom, ikon, header/footer, nama bagian yang tidak lazim).
4. Bahasa: tata bahasa, konsistensi tenses, campuran Indonesia-Inggris yang tidak pas.
5. Daftar perbaikan berdasarkan prioritas (maks. 10), masing-masing dengan contoh konkret.
6. Skor akhir 1–10 dan "siap dikirim?" (Ya / Belum).

Jangan menulis ulang semuanya — berikan perbaikan yang terarah.
JD: """[...]""" CV: """[...]""" Surat/proposal: """[...]"""
```

### P12 — Proposal Proyek Freelance (Upwork / Freelancer / Sribu)
```text
Tulis proposal untuk posting pekerjaan di bawah. Maksimal 150–200 kata.

Struktur:
1. Dua kalimat pertama: tunjukkan saya memahami masalah spesifik klien (kutip/parafrasekan satu detail dari posting) + solusi singkat saya.
2. Bukti relevan: 1 proyek serupa/contoh portofolio (placeholder tautan [LINK]).
3. Rencana mini 3 langkah + estimasi waktu.
4. 1 pertanyaan klarifikasi cerdas yang menunjukkan keahlian.
5. Jawab pertanyaan screening klien, jika ada (akan saya tempelkan).
6. Penutup singkat; jangan memohon, jangan menyebut "saya masih baru".

Dilarang: template generik, klaim pengalaman yang tidak saya miliki, harga yang tidak masuk akal untuk cakupannya.
Posting pekerjaan: """[TEMPEL]"""  Bukti relevan saya: """[TEMPEL]"""
```

---

## Bagian C — Wawancara

### P13 — Simulator Wawancara AI (Adaptif, Dua Bahasa)
**Kegunaan:** Latihan wawancara lengkap. Paling baik dipakai dengan mode suara ChatGPT atau Gemini Live untuk latihan berbicara, atau lewat teks.

```text
Anda adalah "Remote Interview Coach", simulator wawancara adaptif. Ikuti protokol ini secara KETAT.

=== TAHAP 0: PERSIAPAN (ajukan satu pertanyaan per giliran, lalu tunggu jawaban saya) ===
Tanyakan berurutan:
1. Bahasa wawancara: Indonesia atau Inggris?
2. Mode: (a) Pemula — pertanyaan ramah, boleh diberi petunjuk; (b) Profesional — realistis, tanpa petunjuk; (c) Expert — follow-up mendalam, studi kasus, tekanan pada penalaran.
3. Jenis wawancara: (1) Umum/perilaku, (2) Teknis/domain, (3) Evaluasi AI/AI training (menilai respons AI, rubrik, pengecekan fakta), (4) Campuran.
4. Minta saya menempelkan CV dan JD. Jika saya tidak punya JD, tanyakan peran targetnya.
5. Jumlah pertanyaan (default 8) dan apakah saya ingin umpan balik setiap selesai menjawab atau hanya di akhir.
Lalu rangkum: "Peran: …, 3 kompetensi kunci yang diuji: …, 2 area risiko dari CV Anda: …". Tanyakan "Siap mulai?".

=== TAHAP 1: WAWANCARA ===
- Ajukan SATU pertanyaan per giliran. Jangan pernah mengajukan dua pertanyaan sekaligus.
- Ambil pertanyaan dari: (a) persyaratan terpenting di JD, (b) klaim spesifik di CV saya (gali lebih dalam: "Anda menulis X — jelaskan bagaimana Anda mengukurnya"), (c) skenario yang relevan dengan kerja remote (komunikasi asinkron, zona waktu, kualitas di bawah tekanan).
- Adaptif: jika jawaban saya kuat, naikkan tingkat kesulitan; jika lemah atau kabur, ajukan satu follow-up penggali ("Bisa beri contoh spesifik?") sebelum lanjut.
- Untuk wawancara evaluasi AI: sesekali berikan prompt singkat + respons AI, lalu minta saya menilainya dengan rubrik (akurasi, kepatuhan instruksi, keamanan, kejelasan) beserta alasannya.
- Pada mode Expert, tambahkan minimal 1 pertanyaan kasus/estimasi dan 1 pertanyaan tentang trade-off.
- Jangan membuka skor selama wawancara kecuali saya memilih umpan balik per pertanyaan.

=== TAHAP 2: PENILAIAN (per jawaban, atau di akhir) ===
Gunakan rubrik 1–5 untuk setiap dimensi:
- Relevansi: apakah menjawab pertanyaan yang diajukan dan terhubung dengan peran?
- Kejelasan & struktur: ada pembuka yang jelas, struktur (STAR/CAR/PREP), dan kesimpulan?
- Penalaran: apakah logika, asumsi, dan trade-off dijelaskan?
- Keahlian domain: akurat secara teknis, terminologi benar, cukup mendalam?
- Komunikasi: ringkas, percaya diri, register sesuai (untuk bahasa Inggris: tata bahasa & kelancaran, tanpa menghukum aksen).
Jangkar skor: 1 = tidak menjawab/salah; 2 = umum tanpa contoh; 3 = cukup, ada contoh tapi tidak terukur; 4 = spesifik, terstruktur, ada bukti; 5 = spesifik, terukur, reflektif, menunjukkan penilaian yang matang.

=== TAHAP 3: LAPORAN AKHIR ===
Berikan:
1. Tabel: Pertanyaan | Skor per dimensi | Rata-rata | Catatan 1 kalimat.
2. 3 kekuatan terbesar (dengan kutipan dari jawaban saya).
3. 3 area perbaikan dengan prioritas tertinggi.
4. Untuk 2 jawaban terlemah: contoh jawaban model ±150 kata yang HANYA memakai fakta dari CV saya (jika faktanya tidak ada, gunakan placeholder [CONTOH ANDA]).
5. Rencana latihan 7 hari (15–30 menit per hari) yang menyasar kelemahan tersebut.
6. Perkiraan kesiapan: "Belum siap / Hampir siap / Siap", beserta alasannya.

Aturan: Jangan mengarang fakta tentang saya. Jangan memberi pujian yang tidak realistis. Jika saya menulis "STOP", akhiri sesi dan berikan laporan akhir.

Mulai dengan TAHAP 0 pertanyaan 1.
```

### P14 — Penyusun Jawaban Perilaku (STAR) dari Pengalaman Nyata
```text
Saya akan menceritakan satu pengalaman nyata dalam beberapa kalimat. Ubah menjadi jawaban STAR (Situation, Task, Action, Result) yang bisa disampaikan dalam 60–90 detik (±150–200 kata).
- Jadikan bagian Action yang paling panjang dan gunakan "saya" (kontribusi saya), bukan hanya "kami".
- Jika bagian Result tidak punya angka, beri saya 2 pertanyaan untuk membantu menemukan ukuran dampaknya.
- Lalu beri 3 pertanyaan follow-up yang mungkin diajukan pewawancara, lengkap dengan petunjuk jawaban singkat.
Pertanyaan yang sedang dilatih: [contoh: "Ceritakan saat Anda menerima kritik yang tajam"]
Pengalaman saya: """[TEMPEL]"""
```

### P15 — Latihan Evaluasi Respons AI (Rubrik Buatan Sendiri)
**Kegunaan:** Melatih kemampuan "rater" untuk pekerjaan AI training, tanpa memakai materi assessment asli.

```text
Buat 5 soal latihan evaluasi respons AI untuk domain: [UMUM / CODING / KEUANGAN / HUKUM / KESEHATAN / BAHASA INDONESIA].
Setiap soal berisi: (1) prompt pengguna dengan instruksi eksplisit (termasuk batasan format/panjang), (2) dua respons AI (A dan B), masing-masing dengan campuran kelebihan dan kekurangan yang berbeda (misalnya A akurat tapi mengabaikan format, B mengikuti format tapi ada kesalahan fakta), (3) jangan berikan kunci jawaban dulu.

Setelah saya menjawab (mana yang lebih baik + skor 1–5 untuk akurasi, kepatuhan instruksi, kebermanfaatan, keamanan, kejelasan + justifikasi 3–5 kalimat), nilailah jawaban saya: apakah saya menemukan semua kesalahan? Apakah justifikasi saya spesifik dan bisa diverifikasi? Apakah saya membiarkan gaya bahasa mengalahkan substansi?

Gunakan materi ORISINAL, bukan salinan dari assessment asli platform mana pun.
```

---

## Bagian D — Networking

### P16 — Personalisasi Pesan Outreach
```text
Bantu saya mempersonalisasi pesan outreach kepada [NAMA/PERAN] di [PERUSAHAAN].
Konteks: tujuan saya adalah [informational interview / bertanya tentang suatu peran / menawarkan jasa freelance].
Info profil mereka yang saya temukan (postingan, artikel, proyek): """[TEMPEL]"""
Latar belakang saya: """[2–3 kalimat]"""

Buat 2 versi:
1. Catatan koneksi LinkedIn (≤300 karakter).
2. Pesan/email lanjutan (≤120 kata): 1 detail personalisasi yang spesifik, mengapa mereka, satu permintaan kecil yang jelas (15 menit, atau pertanyaan asinkron juga boleh), dan cara mudah bagi mereka untuk menolak.
Bahasa: [Indonesia/Inggris]. Jangan memuji berlebihan. Jangan langsung meminta pekerjaan di pesan pertama.
```

### P17 — Persiapan Coffee Chat
```text
Saya akan coffee chat selama 20 menit dengan [PERAN] di [PERUSAHAAN]. Profil mereka: """[TEMPEL]""". Tujuan saya: [TEMPEL].
Siapkan:
1. Perkenalan diri 30 detik (2 versi: Indonesia & Inggris).
2. 8 pertanyaan berdasarkan prioritas (peran/keseharian, bagaimana mereka bisa masuk, proses rekrutmen, skill yang penting, kesalahan yang sering dibuat kandidat, saran untuk pelamar dari Indonesia/zona waktu kita, siapa lagi yang sebaiknya saya ajak bicara). Tandai 3 pertanyaan yang wajib ditanyakan.
3. 3 hal yang TIDAK boleh dikatakan/dilakukan.
4. Template pesan terima kasih yang dikirim dalam 24 jam, menyebut 1 saran spesifik dari mereka.
```

### P18 — Personalisasi Rencana 30 Hari
```text
Berikut profil saya: [latar belakang, jam tersedia per hari, kategori target: AI training / freelance / pekerjaan remote, level bahasa Inggris, portofolio saat ini].
Sesuaikan rencana 30 hari di Remote Work Playbook dengan situasi saya:
- Prioritaskan 3 kategori platform yang paling cocok beserta alasannya (berdasarkan kelayakan dari Indonesia).
- Jadwal harian yang muat dalam [X] jam per hari.
- KPI mingguan (jumlah lamaran berkualitas, proposal, pesan outreach, simulasi wawancara).
- Aturan "berhenti/lanjut" setelah hari ke-30 berdasarkan data di tracker saya.
Jangan menjanjikan penghasilan atau penerimaan.
```

---

*Alat AI berubah cepat (model, batas pemakaian gratis, fitur). Periksa halaman harga resmi setiap alat sebelum berlangganan paket berbayar.*
