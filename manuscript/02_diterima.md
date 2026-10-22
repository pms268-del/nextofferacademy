# Cara Diterima {#bab2}

Setiap jalur punya "pintu masuk" yang berbeda. Bab ini menjelaskan apa yang terjadi di setiap tahap, apa yang ditanyakan, cara menyiapkannya, seperti apa jawaban yang kuat, dan kesalahan yang paling sering membuat kandidat gagal.

Di bab ini ada dua jenis pertanyaan:

- **Dilaporkan kandidat:** pertanyaan yang diceritakan pelamar di Reddit, Glassdoor, atau Trustpilot. Pertanyaan Anda bisa berbeda, karena banyak wawancara disesuaikan dengan CV masing-masing.
- **Latihan:** pertanyaan buatan Next Offer Academy yang meniru pola tersebut. Ini bukan soal asli.

## A. AI Training & Evaluation

### Tahapan umum

::: {.flow}
1. Daftar & lengkapi profil (CV, bidang keahlian)
2. Tes skill singkat sesuai bidang
3. AI interview (rekaman video/suara)
4. Assessment proyek atau domain
5. Verifikasi identitas & pembayaran
6. Onboarding, lalu tugas mulai masuk
:::

Tidak semua platform memakai semua tahap. Ringkasannya:

| Platform | Yang perlu Anda ketahui |
|----------|------------------------------------------|
| **Mercor** | Lamar per lowongan. AI interview umumnya sekitar 20 menit, dengan pertanyaan berdasarkan CV Anda. Mercor menyediakan *practice interview* gratis, dan AI interview bisa diulang hingga 3 kali sebelum lamaran dikirim ([panduan resmi](https://talent.docs.mercor.com/how-to/prepare-for-ai-interview)). Bayaran mingguan dalam USD ke rekening bank atas nama sendiri. |
| **Outlier** | Buat akun, pilih bidang, kerjakan tes skill, lalu verifikasi identitas. Setelah itu ada onboarding khusus proyek. Lolos tes tidak berarti langsung mendapat tugas; menunggu beberapa hari sampai beberapa minggu itu umum. |
| **Alignerr** | Upload CV, verifikasi ID, AI interview dengan "Zara" (untuk sebagian peran), lalu assessment bidang keahlian. Proyek bergantung pada kebutuhan klien. |
| **micro1** | AI interview dengan "Zara" selama 30–60 menit dengan kamera, mikrofon, dan berbagi layar. Untuk peran teknis ada tantangan coding; untuk annotator ada latihan data ([panduan resmi](https://www.micro1.ai/ai-interview-guide)). Setelah itu biasanya ada percakapan dengan HR dan spesialis. |
| **RWS, Welo Data, TELUS, Appen** | Lamar lowongan bahasa, lalu ikuti tes bahasa dan ujian kualifikasi pedoman penilaian. Ujiannya bisa panjang; pelajari pedomannya dengan serius. |

### Yang ditanyakan

**Dilaporkan kandidat:**

- **AI interview Mercor** dibangun dari CV. Kandidat melaporkan bahwa AI menggali hal yang hanya disebut satu baris di CV. Misalnya, jika menulis Node.js, Anda bisa ditanya tentang *event-driven architecture* ([Glassdoor](https://fr.glassdoor.ca/Entretien/Mercor-Entretien-E9031572-RVW100314407.htm)). Untuk peran engineering, tahap berikutnya bisa berupa review kode secara langsung dan pertanyaan system design ([TechInterview](https://www.techinterview.org/companies/mercor-interview-guide/)).
- **Zara di Alignerr** bertanya tentang CV dan pengalaman Anda. Seorang kandidat menyebutnya "pertanyaan wawancara standar" ([Reddit r/alignerr](https://www.reddit.com/r/alignerr/comments/1hbjc2d/ai_interview_with_zara/)). Kandidat lain melaporkan pertanyaan dasar bahasa dan pendalaman setiap baris CV ([Glassdoor](https://fr.glassdoor.ch/Entretien/Alignerr-Entretien-E10042963-RVW104708502.htm)).
- **micro1:** kandidat data analyst ditanya cara menangani data duplikat, outlier, kualitas data, dan menentukan KPI. Kandidat annotator ditanya tentang pengalaman anotasi data. Kandidat Python mendapat soal *merge overlapping intervals* dan pertanyaan tentang cache ([Glassdoor](https://www.glassdoor.co.uk/Interview/Micro1-Interview-E7558526-RVW105064622.htm)).
- **Tes skill Outlier** umumnya berisi menilai jawaban AI, membandingkan dua jawaban, menemukan kesalahan fakta, dan menuliskan alasan penilaian ([Remotestack](https://remotestack.in/blog/how-to-pass-outlier-ai-assessment-2026)).

**Latihan:**

1. "Walk me through the most relevant project on your CV. What exactly was your contribution?"
2. "You wrote that you improved report accuracy. How did you measure it?"
3. "Response A is longer and more polite but contains a factual error. Response B is short and correct. Which is better, and why?"
4. "The guidelines change halfway through the week, and you've already submitted 40 tasks. What do you do?"
5. "Translate this sentence and explain any nuance an AI might miss: *'Rapat diundur ke Senin depan.'*"

### Cara menyiapkan

::: {.checklist}
- [ ] Baca ulang CV Anda. Siapkan 1–2 kalimat penjelasan untuk **setiap** baris yang Anda tulis.
- [ ] Siapkan 3 cerita proyek: masalahnya, apa yang Anda kerjakan, dan hasilnya (prompt I2 di Bab 4).
- [ ] Ikuti *practice interview* jika platform menyediakannya.
- [ ] Latih menilai jawaban AI 3× per minggu (prompt I3 di Bab 4).
- [ ] Uji kamera, mikrofon, cahaya, dan koneksi. Siapkan hotspot cadangan.
- [ ] Saat berbagi layar, gunakan mode terang dan ukuran huruf yang cukup besar.
- [ ] Sediakan waktu tanpa gangguan, minimal 1,5× perkiraan durasi tes.
:::

### Contoh jawaban yang kuat

> **Pertanyaan:** "You wrote that you automated weekly sales reporting. Tell me more."
>
> **Jawaban kuat:** "Our sales team spent about six hours every Monday combining three regional spreadsheets. I moved the data into BigQuery and built a Looker Studio dashboard that refreshes automatically. I also added a data-quality tab that flags duplicate or missing rows. Preparation time dropped to about one hour, and the regional managers now check the dashboard directly instead of waiting for my email."
>
> *Mengapa kuat:* menjelaskan masalah, tindakan pribadi, tools, dan hasil yang terukur dalam kurang dari satu menit.

> **Latihan menilai AI:** *"Jelaskan fotosintesis untuk anak kelas 3 SD dalam maksimal 3 kalimat."* Jawaban A akurat tetapi 6 kalimat dan memakai istilah "klorofil" dan "glukosa". Jawaban B 3 kalimat sederhana dan akurat.
>
> **Alasan yang kuat:** "B lebih baik. A melanggar dua instruksi eksplisit, yaitu batas 3 kalimat dan bahasa untuk anak kelas 3 SD, meskipun isinya benar. B memenuhi semua instruksi dan isinya akurat. Saya sudah memeriksa bahwa analogi 'tumbuhan memasak makanan dengan sinar matahari' tidak menyesatkan."

### Kesalahan umum

| Kesalahan | Akibat | Lakukan ini |
|---|---|---|
| Memakai ChatGPT, Grammarly, atau penerjemah otomatis saat tes atau tugas | Kontraktor pernah dikeluarkan dari proyek karena hal ini | Kerjakan sendiri. Latihan dengan AI hanya sebelum tes |
| Memilih jawaban AI yang "terdengar bagus", bukan yang mengikuti instruksi | Gagal assessment | Periksa setiap instruksi di prompt satu per satu |
| Tidak bisa menjelaskan isi CV sendiri | Gagal AI interview | Latih penjelasan setiap baris CV |
| Mengerjakan tes terburu-buru atau terputus-putus | Kualitas turun | Sisihkan blok waktu khusus |
| Menganggap lolos onboarding = penghasilan rutin | Kecewa saat tugas kosong | Daftar di 2–3 platform sekaligus |
| Kualitas menurun setelah diterima | Dikeluarkan dari proyek | Tetap baca pembaruan pedoman dan forum proyek |

## B. Freelancing

### 1. Profil yang menjual

Profil yang baik menjawab tiga pertanyaan klien dalam 10 detik: *Apakah orang ini mengerti masalah saya? Apakah dia pernah mengerjakan hal serupa? Apakah komunikasinya mudah?*

- **Judul:** jasa spesifik + untuk siapa. Contoh: *"Indonesian–English Localization for SaaS & Fintech Apps"*.
- **Paragraf pertama:** masalah klien, bukan riwayat hidup Anda.
- **Foto:** wajah jelas dan latar polos.
- **Portofolio:** 3 contoh terbaik, masing-masing dengan konteks singkat dan hasilnya.

{{PROMPT:F1}}

### 2. Portofolio tanpa klien

Jika belum punya klien, buat **proyek contoh** yang realistis dan beri label jujur:

| Jasa | Contoh proyek yang bisa dibuat dalam seminggu |
|---|---|
| Desain | Rebranding fiktif untuk kedai kopi lokal: logo, feed Instagram, dan menu |
| Analisis data | Dashboard dari dataset publik (BPS, Kaggle) dengan 3 insight |
| Penulisan/SEO | 3 artikel blog untuk produk SaaS, lengkap dengan riset kata kunci |
| Penerjemahan | Lokalisasi halaman onboarding aplikasi populer (Inggris → Indonesia) beserta glosarium |
| Virtual assistant | Template SOP, contoh pengelolaan inbox, dan kalender mingguan |

### 3. Proposal yang dibaca

Klien sering hanya membaca dua kalimat pertama. Struktur yang terbukti efektif:

1. **Dua kalimat tentang masalah klien.** Sebut detail dari postingannya.
2. **Satu bukti** yang paling relevan dan tautannya.
3. **Rencana 3 langkah** dan perkiraan waktu.
4. **Satu pertanyaan cerdas** yang menunjukkan keahlian.

{{PROMPT:F2}}

::: {.sample}
**Contoh proposal (Upwork, data dashboard)**

*Posting:* "Looking for someone to build a Looker Studio dashboard from our Google Sheets sales data. 3 regions, monthly KPIs."

> Hi [Name], it sounds like your team spends time every month combining three regional sheets before anyone can see the KPIs. I'd connect them into one Looker Studio dashboard that refreshes automatically.
>
> Similar work: a retail KPI dashboard (revenue, average order value, repeat rate by region) built from a public dataset: [LINK]. It includes a data-quality tab that flags missing or duplicate rows.
>
> Plan: (1) Review the three sheets and agree on KPI definitions — 1 day; (2) Build the combined data source and dashboard with region and month filters — 2–3 days; (3) A 30-minute walkthrough plus a 1-page guide for your team.
>
> Quick question: do the three sheets use the same column format, or do currencies and date formats differ?
:::

::: {.sample}
**Contoh proposal (Sribu/Projects.co.id, konten media sosial)**

*Posting:* "Butuh desainer untuk 12 konten Instagram per bulan untuk klinik gigi, termasuk caption singkat."

> Halo [Nama], untuk klinik gigi tantangannya adalah membuat konten edukatif yang ramah tanpa terkesan menakutkan, dan tetap sesuai etika promosi layanan kesehatan. Saya bisa menyiapkan 12 konten per bulan dengan alur yang jelas.
>
> Contoh: seri 6 konten edukasi kesehatan gigi (proyek contoh) di [LINK], lengkap dengan template Canva yang bisa diedit tim Anda.
>
> Rencana: minggu 1 kalender konten untuk disetujui; minggu 2–3 desain dan caption dengan 2 kali revisi; minggu 4 file final dan jadwal unggah.
>
> Apakah klinik sudah punya panduan warna dan logo, dan layanan apa yang ingin diprioritaskan bulan ini?
:::

### 4. Komunikasi dengan klien

- **Balas dalam beberapa jam** pada jam kerja klien. Kecepatan respons sering menjadi pembeda.
- **Konfirmasi cakupan secara tertulis** sebelum mulai: hasil akhir, jumlah revisi, tenggat, dan harga.
- **Kirim update singkat** di tengah proyek, tanpa menunggu ditanya.
- **Simpan semua komunikasi dan pembayaran di dalam platform.** Ini perlindungan Anda jika terjadi sengketa.

### 5. Memenangkan proyek pertama

- Pilih klien dengan **metode pembayaran terverifikasi** dan deskripsi proyek yang jelas.
- Lamar proyek yang **proposalnya masih sedikit** dan baru dipasang.
- Mulai dengan **proyek kecil** yang bisa diselesaikan dengan sangat baik, lalu minta ulasan.
- Gunakan **platform lokal** (Sribu, Projects.co.id) untuk ulasan pertama jika Upwork masih sepi.
- Ukur hasil Anda. Jika 30 proposal tidak mendapat balasan sama sekali, perbaiki profil atau niche. Jangan langsung menurunkan harga.

### Yang ditanyakan klien (latihan)

| Pertanyaan klien | Jawaban yang kuat | Hindari |
|---|---|---|
| "Have you done something similar?" | Tunjukkan satu contoh paling mirip, jelaskan hasilnya, dan apa yang akan Anda lakukan berbeda untuk mereka | "Yes, many times" tanpa contoh |
| "How long will it take?" | Rincian per tahap + asumsi ("3 hari kerja setelah saya menerima akses data") | Janji terlalu cepat |
| "Can you do it cheaper?" | Tawarkan cakupan yang lebih kecil, bukan pekerjaan yang sama dengan harga lebih murah | Langsung memotong harga |
| "What do you need from me?" | Daftar input yang jelas: akses, contoh, brand guide, kontak | "Nanti saya kabari" |

### Kesalahan umum freelancer baru

- Profil generalis ("I can do anything").
- Proposal template yang dikirim ke semua proyek.
- Banting harga sebagai satu-satunya strategi.
- Menerima pembayaran di luar platform sebelum ada kepercayaan.
- Berhenti setelah 2 minggu. Mendapatkan klien pertama sering butuh waktu lebih lama.

## C. Pekerjaan Remote (Karyawan & Kontrak Bulanan)

### Tahapan umum

::: {.flow}
1. Lamaran (CV + pesan singkat)
2. Screening recruiter (15–30 menit)
3. Tes keterampilan / take-home task
4. Wawancara hiring manager & perilaku
5. Wawancara akhir / tim
6. Tawaran (kontraktor atau melalui EOR)
:::

**EOR (Employer of Record)** seperti Deel, Remote, atau Oyster sering dipakai perusahaan asing untuk mempekerjakan orang di Indonesia secara legal. Jika recruiter menyebut nama-nama ini, itu hal yang normal.

### Yang ditanyakan

**Dilaporkan kandidat** (dari laman wawancara Glassdoor untuk peran remote support):

- "Tell me about a time you handled an angry customer."
- "What would you say to an angry customer who called for tech support?"
- Skenario dari wawancara customer support di sebuah perusahaan website builder: pertanyaan pelanggan tidak terjawab setelah ia berinteraksi buruk dengan rekan kerja Anda. Langkah apa yang Anda ambil untuk memperbaiki hubungan dengan pelanggan dan berbicara dengan rekan tersebut? ([Glassdoor](https://static.glassdoor.it/Interview/remote-support-interview-questions-SRCH_KO0,14_IP30.htm))

**Latihan (screening recruiter):**

1. "Walk me through your background."
2. "Why remote, and why our company?"
3. "We're in [time zone]. How much overlap can you offer?"
4. "Are you able to work as a contractor? Do you have a stable internet setup?"
5. "What are your salary expectations?"

### Cara menyiapkan

- **Sesuaikan CV untuk setiap lowongan** dengan workflow di Bab 3.
- **Siapkan 5 cerita STAR:** keberhasilan, kegagalan, konflik, tenggat ketat, dan belajar cepat.
- **Riset gaji** dari lowongan sejenis yang mencantumkan kisaran gaji (Wellfound, Himalayas, Remote OK sering mencantumkannya).
- **Hitung jam overlap Anda.** Contoh: jam 09.00 di New York (UTC−4) adalah jam 20.00 WIB.
- **Kirim pesan singkat ke hiring manager** setelah melamar (Bab 5).

### Contoh jawaban yang kuat

> **"Tell me about a time you handled an angry customer."**
>
> "A customer emailed in capital letters because a refund had been delayed for ten days. First I acknowledged the frustration and apologised for the wait. Then I checked the payment log and found the refund was stuck because of a mismatched bank code. I escalated it to finance with the exact details, gave the customer a realistic timeline of two working days, and updated them the next morning before they had to ask. The refund arrived on day two, and the customer rated the ticket five stars. Afterwards I added a check for bank codes to our refund macro, so the same issue wouldn't repeat."

### Kesalahan umum

- Melamar lowongan "Remote (US only)" atau tidak mengecek lokasi.
- Satu CV dikirim ke semua lowongan.
- Tidak siap menjawab soal gaji dan jam kerja.
- Jawaban perilaku tanpa contoh nyata atau tanpa hasil.
- Tidak menindaklanjuti setelah wawancara. Kirim ucapan terima kasih dalam 24 jam.
