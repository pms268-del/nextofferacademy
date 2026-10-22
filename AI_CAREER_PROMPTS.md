# Prompt Karier AI — Next Offer Academy

Kumpulan prompt dari *Remote Work Playbook 2026*. Prompt ini bisa dipakai di ChatGPT, Claude, Gemini, atau asisten AI lain.

**Aturan singkat**

- Ganti semua `[TEKS DALAM KURUNG SIKU]` dengan data Anda.
- Jangan minta AI menambahkan pengalaman, angka, atau sertifikat yang tidak Anda miliki.
- Hapus data pribadi sensitif (NIK, alamat lengkap, dokumen rahasia klien) sebelum menempelkan CV.
- Platform AI training melarang penggunaan AI saat assessment dan saat mengerjakan tugas. Gunakan prompt ini hanya untuk persiapan.

---

## Workflow Lamaran (CV + Lowongan → Lamaran Siap Kirim)

### W1 — Instruksi Asisten Lamaran (pasang sekali)
Simpan sebagai instruksi tetap di fitur *Projects* (ChatGPT/Claude) atau *Gems* (Gemini) jika tersedia di akun Anda. Jika tidak tersedia, tempel di awal setiap percakapan baru.

```text
Kamu adalah asisten lamaran kerja saya untuk pekerjaan remote internasional.

Tentang saya:
- Saya tinggal di Indonesia (WIB/UTC+7).
- Master CV saya ada di bawah. Ini satu-satunya sumber fakta tentang saya.

Aturan kerja:
1. Jangan pernah menambahkan pengalaman, angka, tools, jabatan, atau sertifikat yang tidak ada di master CV. Jika butuh data tambahan, tanyakan kepada saya.
2. Tulis dalam bahasa yang sama dengan lowongan (biasanya bahasa Inggris), kecuali saya minta lain.
3. Gunakan bahasa yang lugas dan profesional, tanpa klise seperti "passionate" atau "hardworking".
4. Format CV: satu kolom, teks polos, judul bagian standar (SUMMARY, SKILLS, EXPERIENCE, PROJECTS, EDUCATION, LANGUAGES).
5. Setiap kali saya menempelkan lowongan baru, jalankan langkah W2 terlebih dahulu.

Master CV:
"""
[TEMPEL MASTER CV LENGKAP]
"""
```

### W2 — Analisis Lowongan & Kecocokan
```text
Berikut lowongan yang ingin saya lamar. Analisis dan berikan:

1. Ringkasan peran dalam 2 kalimat.
2. 5 persyaratan terpenting, masing-masing ditandai [WAJIB] atau [NILAI TAMBAH].
3. Untuk setiap persyaratan: bukti yang sudah ada di CV saya (kutip), atau tulis "BELUM ADA".
4. 8–10 kata kunci dari lowongan yang perlu muncul di CV saya, hanya jika saya memang punya pengalamannya.
5. Kelayakan lokasi: apakah lowongan terbuka untuk kandidat di Indonesia? Kutip kalimat yang relevan. Jika tidak jelas, tulis "Tanyakan ke recruiter".
6. Tanda bahaya, jika ada (biaya pendaftaran, rekrutmen via Telegram/WhatsApp, bayaran tidak jelas).
7. Penilaian akhir: "Layak dilamar", "Layak dengan catatan", atau "Lewati", disertai satu kalimat alasan.

Lowongan:
"""
[TEMPEL DESKRIPSI LOWONGAN]
"""
```

### W3 — CV yang Disesuaikan
```text
Buat CV yang disesuaikan untuk lowongan ini dari master CV saya.

- Pilih pengalaman dan bullet yang paling relevan. Urutkan dari yang paling relevan.
- Tulis ulang bullet dengan pola: kata kerja aksi + apa yang dikerjakan + hasil/angka (angka hanya jika ada di master CV).
- Jika sebuah bullet akan lebih kuat dengan angka yang tidak saya miliki, beri tanda [PERLU ANGKA] dan ajukan satu pertanyaan kepada saya.
- Buat ringkasan (SUMMARY) 2–3 kalimat yang menjawab kebutuhan utama lowongan.
- Maksimal 1 halaman untuk pengalaman di bawah 5 tahun, maksimal 2 halaman untuk yang lebih lama.
- Setelah CV, tampilkan daftar singkat "Yang saya ubah dan alasannya".
```

### W4 — Cover Letter / Pesan Lamaran
```text
Tulis cover letter untuk lowongan ini, maksimal 200 kata:
1. Pembuka: mengapa peran ini cocok, dengan menyebut satu hal spesifik dari lowongan atau perusahaan.
2. Bukti utama: satu pencapaian paling relevan dari CV saya.
3. Kontribusi: bagaimana saya membantu dalam 30–60 hari pertama.
4. Penutup: zona waktu saya (UTC+7), jam yang bisa beririsan dengan tim, dan ajakan untuk wawancara.

Buat juga versi singkat 80 kata untuk kolom "Why are you interested?" atau pesan ke recruiter di LinkedIn.
```

### W5 — Review Akhir Sebelum Kirim
```text
Periksa CV dan cover letter final saya sebagai recruiter yang hanya punya 30 detik:
1. Apa 3 hal pertama yang tertangkap? Apakah sudah menjawab kebutuhan utama lowongan?
2. Klaim mana yang paling lemah atau sulit dipertanggungjawabkan dalam wawancara?
3. Kesalahan bahasa, ketidakkonsistenan tanggal/jabatan, atau format yang menyulitkan sistem ATS.
4. Maksimal 5 perbaikan prioritas, masing-masing dengan contoh kalimat perbaikannya.
5. Kesimpulan: "Siap kirim" atau "Perbaiki dulu".

CV final: """[TEMPEL]"""
Cover letter final: """[TEMPEL]"""
```

### W6 — Mode Cepat untuk Banyak Lamaran
Gunakan untuk lowongan yang mirip dengan lowongan yang sudah pernah Anda proses.

```text
Lowongan baru di bawah mirip dengan lowongan sebelumnya. Lakukan sekaligus:
1. Analisis singkat (maksimal 5 baris): kecocokan, kelayakan lokasi, dan tanda bahaya.
2. Hanya bagian CV yang perlu diubah (SUMMARY dan 3–5 bullet), bukan seluruh CV.
3. Pesan lamaran 80 kata.

Lowongan: """[TEMPEL]"""
```

---

## Freelance

### F1 — Profil Upwork / Fiverr
```text
Buat profil freelance untuk [Upwork/Fiverr] dengan jasa: [JASA SPESIFIK].
Fakta tentang saya: [pengalaman, tools, hasil kerja, tautan portofolio].

Berikan:
1. Judul profil (Upwork maks. 70 karakter; Fiverr diawali "I will ...").
2. Deskripsi 150–250 kata yang dibuka dengan masalah klien, lalu solusi, proses kerja, bukti, dan ajakan menghubungi.
3. Untuk Fiverr: 3 paket (Basic/Standard/Premium) berisi cakupan, jumlah revisi, dan waktu pengerjaan. Harga akan saya tentukan sendiri.
4. 3 ide contoh portofolio yang bisa saya buat dalam seminggu, diberi label "proyek contoh".
5. 10 kata kunci pencarian.
Jangan menjanjikan hasil yang tidak bisa dijamin.
```

### F2 — Proposal Proyek
```text
Tulis proposal untuk posting proyek di bawah, maksimal 150 kata:
1. Dua kalimat pertama: tunjukkan bahwa saya memahami masalah spesifik klien (sebut satu detail dari posting).
2. Satu bukti relevan dari pengalaman saya + tautan [LINK].
3. Rencana kerja 3 langkah beserta perkiraan waktu.
4. Satu pertanyaan klarifikasi yang cerdas.
5. Jawaban untuk pertanyaan screening klien (jika ada).
Hindari kalimat pembuka generik dan klaim pengalaman yang tidak saya miliki.

Posting: """[TEMPEL]"""
Pengalaman saya yang relevan: """[TEMPEL]"""
```

---

## Wawancara

### I1 — Simulator Wawancara AI
Bisa dipakai lewat teks, atau lewat mode suara di ChatGPT/Gemini untuk latihan berbicara.

```text
Bertindaklah sebagai pewawancara untuk lowongan di bawah. Gunakan CV saya sebagai dasar pertanyaan.

Sebelum mulai, tanyakan kepada saya:
1. Bahasa wawancara: Inggris atau Indonesia?
2. Tingkat kesulitan: Dasar, Menengah, atau Sulit?
3. Jenis wawancara: AI training, klien freelance, atau pekerjaan remote (recruiter/hiring manager)?

Aturan:
- Ajukan satu pertanyaan per giliran, lalu tunggu jawaban saya.
- Total 8 pertanyaan: campuran pertanyaan tentang CV saya, kebutuhan lowongan, situasi kerja remote, dan satu pertanyaan yang lebih menantang.
- Jika jawaban saya kabur, ajukan satu pertanyaan lanjutan ("Bisa beri contoh spesifik?").
- Untuk wawancara AI training: sertakan satu latihan menilai dua jawaban AI dan minta saya menjelaskan alasannya.
- Setelah setiap jawaban, berikan umpan balik singkat:
  • Yang sudah bagus (1 poin)
  • Yang perlu diperbaiki (1–2 poin)
  • Versi jawaban yang lebih kuat, hanya memakai fakta dari CV saya
- Untuk wawancara berbahasa Inggris: koreksi maksimal 2 kesalahan bahasa yang paling penting per jawaban.
- Setelah pertanyaan ke-8, berikan ringkasan: 3 kekuatan, 3 hal yang perlu dilatih, dan 3 pertanyaan yang sebaiknya saya latih lagi.

Lowongan: """[TEMPEL]"""
CV: """[TEMPEL]"""
```

### I2 — Menyusun Cerita Pengalaman (STAR)
```text
Ubah pengalaman saya di bawah menjadi jawaban wawancara 60–90 detik dalam bahasa [Inggris/Indonesia] dengan struktur: Situasi → Tugas → Tindakan saya → Hasil.
Fokuskan pada tindakan saya, bukan tim. Jika hasilnya belum terukur, beri 2 pertanyaan untuk membantu saya menemukan angkanya.
Pertanyaan yang dilatih: [contoh: "Tell me about a time you handled a difficult customer"]
Pengalaman saya: """[TEMPEL]"""
```

### I3 — Latihan Menilai Jawaban AI
```text
Buat 5 soal latihan menilai jawaban AI untuk bidang [UMUM/CODING/KEUANGAN/BAHASA INDONESIA].
Setiap soal berisi satu instruksi pengguna dan dua jawaban AI (A dan B) dengan kelebihan dan kekurangan yang berbeda, misalnya satu akurat tetapi melanggar format, satu lagi rapi tetapi ada kesalahan fakta.
Jangan beri kunci jawaban dulu. Setelah saya memilih dan menjelaskan alasan saya, beri tahu apakah saya melewatkan kesalahan dan apakah alasan saya cukup spesifik.
Gunakan soal orisinal, bukan salinan soal asli platform mana pun.
```

---

## LinkedIn & Networking

### N1 — Optimasi Profil LinkedIn
```text
Berdasarkan CV saya dan target peran [PERAN], buat:
1. 3 pilihan headline (maks. 220 karakter): Peran | Bidang/Tools | Bukti | Open to remote (UTC+7).
2. Bagian About (maks. 1.500 karakter): masalah yang saya selesaikan, 2–3 bukti, skill utama, dan jenis pekerjaan yang saya cari.
3. 10 skill yang perlu dicantumkan, sesuai istilah yang biasa dicari recruiter.
Hanya gunakan fakta dari CV saya.
CV: """[TEMPEL]"""
```

### N2 — Pesan Outreach yang Dipersonalisasi
```text
Tulis pesan LinkedIn untuk [NAMA, PERAN, PERUSAHAAN].
Konteks: [saya baru melamar posisi X / ingin bertanya tentang tim mereka / menawarkan jasa].
Info tentang mereka: [postingan, proyek, latar belakang yang sama].
Buat 2 versi: catatan koneksi (maks. 300 karakter) dan pesan lanjutan (maks. 100 kata) dengan satu permintaan kecil yang jelas.
Bahasa: [Inggris/Indonesia]. Jangan meminta pekerjaan secara langsung.
```
