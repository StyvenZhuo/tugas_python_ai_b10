# 📘 RAG Parameter Exploration Assignment

Pada tugas ini kamu akan bereksperimen dengan **6 parameter utama Retrieval-Augmented Generation (RAG)** menggunakan **RAG Playground**.

### 🎯 Tujuan Pembelajaran

Kamu akan:

✅ Memahami **apa fungsi** masing-masing parameter RAG

✅ Mengamati **pengaruh** tuning terhadap kualitas jawaban vs kecepatan

✅ Belajar **trade-off** antara retrieval & generation

✅ Menulis **insight praktis** dari eksperimen yang kamu lakukan

> **Tools sudah disediakan.** Kamu **tidak perlu ngoding**, hanya ubah nilai parameter di file `app.py` & restart server.

### ⚠️ Notes Penting

- **Ikuti video di LMS jika kamu kebingungan.**
- **Sediakan penyimpanan at least 2GB**, akan ada download model yang cukup besar ke laptopmu.
- **Hapus proyek ini kalau sudah selesai**, biar laptop-mu tidak tercekik.
- **Ketika proyek ini sudah diisi & dikerjakan di bawah, upload ke GitHub.**

---

## ⚙️ Parameter yang Diuji

Semua parameter berikut dapat ditemukan di file `app.py`:

```python
# Buka app.py, cari bagian KONFIGURASI INTI
CHUNK_SIZE = 300
TOP_K_INITIAL = 20
FINAL_TOP_M = 5
USE_RERANKER = True
TEMPERATURE = 0.2
GROQ_MODEL = "llama-3.1-8b-instant"
```

---

### 📏 1. CHUNK_SIZE

```python
CHUNK_SIZE = 300  # ubah angka ini
```

**Apa itu CHUNK_SIZE?**

Saat dokumen PDF diupload, teksnya dipotong-potong menjadi bagian kecil (chunk) agar bisa diproses dan dicari. `CHUNK_SIZE` menentukan berapa banyak **kata** per potongan.

**Fungsi:** _(Jelaskan dengan kata-katamu sendiri apa fungsi dari CHUNK_SIZE)_

> Jawab: CHUNK_SIZE berfungsi mengatur panjang potongan teks dokumen yang dijadikan basis pencarian, sehingga mempengaruhi seberapa banyak konteks yang dibawa tiap chunk saat sistem mencari dan menyusun jawaban

**Pengaruhnya:**

| Range Nilai                         | Efek                                                                                                                                                                                                                       |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Kecil (100–200)**                 | _(Chunk jadi lebih pendek dan spesifik, jadi pencarian bisa lebih presisi ke topik tertentu, tapi sering kurang lengkap konteksnya karena kalimat yang berhubungan kebagi ke beberapa chunk terpisah.)_                    |
| **Sedang (250–400)** ⭐ Recommended | _(Ukuran ini dapat dikatakan pas karena chunk cukup panjang buat bawa konteks yang utuh (satu paragrafan), tapi masih cukup kecil sehingga sistem bisa milih bagian yang relevan tanpa kebanyakan teks yang tidak perlu.)_ |
| **Besar (500–1000)**                | _(Chunk berisi banyak teks, jadi konteks yang dibawa lebih lengkap, tapi pencariannya bisa jadi kurang tajam karena satu chunk memuat beberapa topik sekaligus dan proses retrieval bisa sedikit lebih berat.)_            |

**Pertanyaan Refleksi:**

- Chunk besar atau kecil yang lebih tepat untuk dokumen yang kamu tes? Mengapa?

  > Jawab: Buat dokumen yang aku pakai, chunk ukuran sedang cenderung lebih pas. Kalau terlalu kecil (100–200), jawabannya kadang jadi kepotong dan nggak bawa konteks penuh paragraf. Kalau terlalu besar (500+), konteks memang lengkap tapi rasanya jadi kurang spesifik dan sistem suka ngambil bagian yang agak melenceng

- Apa yang terjadi kalau jawaban terasa "terpotong" atau kurang konteks? Parameter mana yang harus diubah?

  > Jawab: Kalau jawaban mulai terasa kepotong atau kurang konteks, yang pertama aku sentuh biasanya CHUNK_SIZE (dinaikkan biar satu chunk bawa konteks lebih banyak), dan bisa juga naikin FINAL_TOP_M supaya LLM dapat lebih banyak potongan relevan sebagai konteks

---

### 🔍 2. TOP_K_INITIAL

```python
TOP_K_INITIAL = 20
```

**Apa itu TOP_K_INITIAL?**

Setelah pertanyaan diubah jadi vektor, sistem mencari chunk yang paling mirip. `TOP_K_INITIAL` menentukan berapa banyak **kandidat awal** yang diambil dari hasil pencarian vektor sebelum di-filter/rerank.

**Fungsi:** _(Jelaskan dengan kata-katamu sendiri apa fungsi dari TOP_K_INITIAL)_

> Jawab: TOP_K_INITIAL untuk mengatur jumlah kandidat chunk awal yang diambil dari vector search sebelum difilter lagi, jadi makin besar nilainya, maka makin banyak juga potongan dokumen yang ikut dipertimbangkan di tahap awal retrieval

**Pengaruhnya:**

| Range Nilai                       | Efek                                                                                                                                                                                                                          |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Kecil (5–10)**                  | _(Sistem cuma ambil sedikit kandidat awal, jadi prosesnya lebih cepat, tapi risiko ada chunk penting yang kelewat jadi recall‑nya bisa turun, terutama kalau dokumennya panjang atau topiknya nyebar.)_                       |
| **Sedang (15–25)** ⭐ Recommended | _(Di range ini balance‑nya enak: kandidat yang diambil cukup banyak buat nangkep konteks penting, tapi belum terlalu berat, jadi recall oke dan kecepatan masih nyaman dipakai interaktif.)_                                  |
| **Besar (30–50)**                 | _(Sistem ambil banyak banget kandidat awal, sehingga recall bisa naik (lebih kecil kemungkinan informasi penting kelewat), tapi waktu proses dan beban reranker juga jadi lebih besar, jadi respon bisa terasa lebih lambat)_ |

> 💡 **Catatan:** Nilai ini hanya berpengaruh signifikan jika `USE_RERANKER = True`. Tanpa reranker, yang dipakai langsung hanya `FINAL_TOP_M` teratas.

**Pertanyaan Refleksi:**

- Apakah top-k kecil (5–10) cukup untuk dataset kamu? Jelaskan alasannya.

  > Jawab: Di dataset yang aku pakai, top‑k kecil (5–10) masih terbilan cukup kalau pertanyaannya simpel dan infonya terfokus di satu bagian dokumen. Tapi untuk pertanyaan yang butuh konteks lebih luas, aku merasa 5–10 itu agak riskan karena beberapa chunk penting bisa nggak ikut ke kandidat awal, jadi jawabannya bisa miss detail

- Apa hubungan antara `TOP_K_INITIAL` dan `USE_RERANKER`?

  > Jawab: TOP_K_INITIAL itu untuk ngatur seberapa banyak kandidat awal yang dikasih ke reranker. Kalau USE_RERANKER = True, nilai top‑k ini penting karena reranker butuh cukup banyak kandidat buat milih mana yang paling relevan. Kalau USE_RERANKER = False, sistem langsung pakai beberapa teratas saja (FINAL_TOP_M), jadi efek top‑k tidak terlalu terasa

---

### 📋 3. FINAL_TOP_M

```python
FINAL_TOP_M = 5
```

**Apa itu FINAL_TOP_M?**

Dari sekian banyak kandidat yang ditemukan, hanya **M teratas** (setelah reranking) yang dikirim ke LLM sebagai konteks untuk menjawab pertanyaan.

**Fungsi:** _(Jelaskan dengan kata-katamu sendiri apa fungsi dari FINAL_TOP_M)_

> Jawab: FINAL_TOP_M itu ngatur berapa banyak chunk terbaik yang akhirnya dikirim ke LLM sebagai konteks. Jadi setelah sistem nyari dan (kalau ada) ngererank semua kandidat, cuma M chunk teratas inilah yang dipakai pas model nyusun jawaban

**Pengaruhnya:**

| Range Nilai                     | Efek                                                                                                                                                                                                                                                     |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sedikit (2–3)**               | _(Output atau Jawaban biasanya lebih fokus karena LLM cuma lihat sedikit chunk yang sangat relevan, tapi risiko ada konteks penting yang nggak ikut kebawa jadi lebih tinggi, terutama kalau informasi jawabannya tersebar di beberapa bagian dokumen.)_ |
| **Sedang (4–6)** ⭐ Recommended | _(Jumlah konteks masih cukup sedikit buat tetap ringkas dan cepat, tapi sudah lumayan aman buat ngumpulin potongan informasi yang saling melengkapi. Makanya range ini enak sebagai balance antara fokus, kelengkapan, dan kecepatan.)_                  |
| **Banyak (7–10)**               | _(LLM dapat lebih banyak konteks, jadi jawabannya bisa lebih lengkap, tapi prompt jadi lebih panjang, respon bisa makin lambat, dan ada risiko model agak bingung kalau isi chunk‑chunk tersebut bercampur beberapa topik sekaligus.)_                   |

> 💡 **Catatan:** Semakin banyak konteks = semakin banyak token yang dikirim ke LLM = latency lebih tinggi. Jaga agar tetap efisien.

**Pertanyaan Refleksi:**

- Benarkah "semakin banyak konteks semakin bagus"? Jelaskan berdasarkan eksperimenmu.

  > Jawab: Menurut hasil testing ku, nggak selalu makin banyak konteks makin bagus. Kalau konteksnya terlalu banyak, jawabannya memang bisa lebih panjang, tapi kadang jadi bertele‑tele dan nggak fokus. Di beberapa kasus, M yang sedang (4–6) malah ngasih jawaban yang lebih jelas dan tepat sasaran dibanding M besar karena model cuma lihat bagian yang benar‑benar relevan

- Apa yang terjadi kalau konteks yang dikirim ke LLM saling bertentangan?

  > Jawab: Kalau konteks yang masuk ke LLM isinya saling bertentangan, model bisa bingung dan hasilnya jadi campuran: kadang jawabannya tidak konsisten, atau dia pilih salah satu konteks yang nggak sesuai pertanyaan. Ini biasanya kejadian kalau FINAL_TOP_M terlalu besar dan banyak chunk yang topiknya beda‑beda ikut kebawa

---

### 🎯 4. USE_RERANKER

```python
USE_RERANKER = True  # atau False
```

**Apa itu Reranker?**

Reranker adalah model tambahan (Cross-Encoder) yang mengevaluasi ulang pasangan `[pertanyaan, chunk]` untuk mengurutkan relevansi lebih akurat daripada hanya cosine similarity biasa.

**Fungsi:** _(Jelaskan dengan kata-katamu sendiri apa fungsi dari USE_RERANKER)_

> Jawab: USE_RERANKER dipakai buat ngatur apakah sistem bakal pakai model tambahan buat ngecek ulang pasangan [pertanyaan, chunk]. Kalau di‑set True, reranker ini ngerjain ‘filter tahap dua’ supaya urutan chunk yang dikasih ke LLM lebih akurat dibanding cuma ngandelin skor cosine similarity dari vector search

**Pengaruhnya:**

| Mode    | Efek                                                                                                                                                                                                                                    |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `True`  | _(Presisi dan relevansi konteks biasanya naik karena setiap kandidat dicek ulang langsung terhadap pertanyaan, tapi ada biaya waktu tambahan: respons jadi sedikit lebih lambat karena ada satu model lagi yang harus jalan.)_          |
| `False` | _(Sistem cuma mengurutkan chunk pakai cosine similarity dari vector search. Proses jadi lebih cepat dan ringan, tapi kadang urutan konteks kurang akurat, apalagi untuk pertanyaan yang ambigu atau mirip ke beberapa bagian dokumen.)_ |

> 💡 **Catatan:** Untuk dokumen teknis atau pertanyaan yang ambigu, reranker sangat membantu. Untuk kecepatan maksimal, matikan.

**Pertanyaan Refleksi:**

- Pada query jenis apa reranker paling terasa manfaatnya? Berikan contoh.

  > Jawab: Reranker paling kerasa manfaatnya waktu pertanyaannya agak panjang atau ambigu, misalnya yang butuh penjelasan konsep tertentu yang muncul di beberapa bagian dokumen. Di kasus begitu, reranker bantu milih chunk yang bener‑bener nyambung sama maksud pertanyaannya, bukan cuma yang mirip secara kata‑kata.

- Berapa kira-kira tambahan latency saat reranker dinyalakan di eksperimenmu?

  > Jawab: Dari hasil testing ku, waktu reranker dinyalakan respons memang terasa sedikit lebih lambat dibanding tanpa reranker, tapi masih dalam batas wajar buat dipakai interaktif. Jadi ada trade‑off kecil antara kecepatan dan kualitas jawaban

---

### 🌡️ 5. TEMPERATURE

```python
TEMPERATURE = 0.2  # range: 0.0 - 1.0
```

**Apa itu Temperature?**

Temperature mengatur distribusi probabilitas saat LLM memilih kata berikutnya. Semakin rendah, semakin "pasti" dan konsisten jawabannya.

**Fungsi:** _(Jelaskan dengan kata-katamu sendiri apa fungsi dari TEMPERATURE)_

> Jawab: TEMPERATURE ngatur seberapa ‘acak’ atau ‘pasti’ model milih kata berikutnya. Kalau nilainya kecil, model cenderung ambil kata yang paling aman dan konsisten; kalau nilainya besar, model jadi lebih bebas dan kreatif, tapi resiko jawabannya ngaco juga makin tinggi.

**Pengaruhnya:**

| Range Nilai                          | Efek                                                                                                                                                                                                   |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **0.0–0.2** ⭐ Recommended untuk RAG | _(Jawaban cenderung sangat konsisten, lebih faktual, dan nempel ke konteks dokumen. Risiko halusinasi lebih kecil, tapi gaya bahasanya agak kaku dan kurang variasi.)_                                 |
| **0.3–0.5**                          | _(Jawaban mulai sedikit lebih variatif dan enak dibaca, tapi masih cukup aman dan tetap mengikuti isi dokumen. Cocok kalau pengen jawaban nggak terlalu kaku tapi tetap akurat.)_                      |
| **0.6–0.8**                          | _(Model jadi lebih kreatif dan eksploratif. Jawaban bisa lebih panjang, pakai kata‑kata yang bervariasi, tapi mulai sering keluar dari dokumen dan berpotensi nambahin hal yang nggak ada di konteks)_ |
| **0.9–1.0**                          | _(Jawaban sangat acak dan kreatif, cocok buat brainstorming, tapi untuk RAG/QA berbasis dokumen risiko halusinasi tinggi dan jawaban sering tidak konsisten dengan isi dokumen.)_                      |

> ⚠️ **Catatan:** Untuk RAG (jawaban berdasarkan dokumen), gunakan temperature rendah (0.1–0.3) agar jawaban tetap _grounded_ pada konteks yang diberikan.

**Pertanyaan Refleksi:**

- Untuk QA berbasis dokumen perusahaan, temperatur ideal berapa? Jelaskan alasannya.

  > Jawab: Buat QA yang basisnya dokumen perusahaan, menurutku temperature ideal di kisaran 0.1–0.3. Di range ini jawaban tetap jelas dan konsisten sama isi dokumen, jadi lebih aman dipakai buat informasi formal dan mengurangi resiko model halu

- Apa yang terjadi pada jawaban saat kamu naikkan temperature ke 0.9?

  > Jawab: Waktu aku naikin temperature ke 0.9, jawaban memang jadi lebih kreatif dan variatif, tapi sering keluar topik dan kadang nambahin informasi yang nggak ada di dokumen. Untuk RAG di tugas ini, setting setinggi itu kerasa kurang cocok karena akurasinya turun

---

### 🤖 6. GROQ_MODEL

```python
GROQ_MODEL = "llama-3.1-8b-instant"  # model default
```

**Model lain yang bisa dicoba:**

```python
# Ganti value GROQ_MODEL ke salah satu di bawah:
GROQ_MODEL = "openai/gpt-oss-120b"
GROQ_MODEL = "llama-3.3-70b-versatile"
```

**Apa bedanya tiap model?**

Setiap model punya ukuran parameter dan kemampuan yang berbeda. Isi tabel di bawah berdasarkan eksperimenmu:

| Model                            | Ukuran         | Pengaruh terhadap Kecepatan & Kualitas                                                                                                                                                                                                                         |
| -------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `llama-3.1-8b-instant` (Default) | 8B parameter   | _(Paling cepat dan ringan, jawaban sudah cukup bagus untuk pertanyaan standar dan testing fitur. Cocok dipakai saat development, eksplorasi awal, atau use‑case yang butuh respon sangat cepat)_                                                               |
| `openai/gpt-oss-120b`            | 120B parameter | _(Jauh lebih besar dan lebih kuat di reasoning, penjelasan panjang, dan kasus yang kompleks, tapi respon terasa lebih lambat dan konsumsi token lebih boros. Cocok dipakai kalau butuh akurasi tinggi dan penalaran dalam, misalnya analisis teks yang berat)_ |
| `llama-3.3-70b-versatile`        | 70B parameter  | _(Kualitas jawaban di atas 8B dan sering mendekati model sangat besar, dengan kecepatan yang masih cukup oke (terutama di Groq). Enak dipakai kalau ingin kombinasi antara kualitas bagus dan performa yang masih layak untuk interaktif)_                     |

> 💡 **Tips:** Mulai dengan `llama-3.1-8b-instant` untuk development. Saat butuh akurasi tinggi, switch ke `llama-3.3-70b-versatile` atau `openai/gpt-oss-120b`.

**Pertanyaan Refleksi:**

- Apakah peningkatan kualitas jawaban dari model besar sebanding dengan penambahan waktu? Jelaskan.

  > Jawab: Dari eksperimenku, model besar memang ngasih jawaban yang lebih detail dan rapi, terutama untuk pertanyaan yang butuh reasoning. Tapi nggak selalu sebanding dengan penambahan waktu; untuk pertanyaan sederhana, llama-3.1-8b-instant sudah cukup dan jauh lebih responsif. Model besar baru kerasa worth it kalau tugasnya lebih sulit atau butuh akurasi tinggi

- Model mana yang paling cocok untuk use-case dokumenmu? Mengapa?

  > Jawab: Untuk use‑case dokumen yang aku pakai di tugas ini, menurutku yang paling cocok llama-3.3-70b-versatile (atau tetap di 8B kalau benar‑benar butuh cepat). Alasannya karena kualitas jawabannya lebih stabil dan detail dibanding 8B, tapi masih cukup cepat untuk dipakai interaktif, jadi seimbang antara kecepatan dan akurasi.

---

## ⚙️ Parameter Tambahan (Non-Tunable)

Parameter ini sudah di-set optimal. Ubah hanya jika paham dampaknya.

```python
CHUNK_OVERLAP = 60     # overlap antar chunk (kata)
SCORE_THRESHOLD = 0.30 # skor minimum cosine similarity
```

**Penjelasan:**

| Parameter         | Nilai Default | Fungsi                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CHUNK_OVERLAP`   | 60            | _(Dipakai buat ngatur seberapa banyak kata yang “numpang lewat” dari chunk sebelumnya ke chunk berikutnya. Overlap ini bantu jaga supaya konteks di batas antar chunk nggak putus. Kalau terlalu kecil, informasi di peralihan paragraf bisa hilang; kalau terlalu besar, banyak teks yang ketarik berulang‑ulang sehingga index jadi lebih berat dan kadang bikin konteks yang dikirim ke LLM jadi terlalu redundant)_ |
| `SCORE_THRESHOLD` | 0.30          | _(Ini adalah batas minimum skor kemiripan (cosine similarity) antara query dan chunk. Hanya chunk dengan skor di atas threshold yang dipakai sebagai kandidat konteks. Kalau threshold dinaikkan, hasil retrieval jadi lebih presisi tapi berisiko tidak menemukan apa‑apa untuk pertanyaan yang sulit; kalau diturunkan, sistem lebih toleran dan recall naik, tapi bisa masuk chunk yang kurang relevan)_             |

---

## 📝 Tips Eksperimen

- Pakai PDF minimal 1 halaman, maksimal 10 halaman, biar gak berat
- Coba berbagai jenis pertanyaan: **definisi**, **konteks**, dan **reasoning**
- Catat kapan sistem salah & mengapa
- Ubah **satu parameter pada satu waktu** agar bisa melihat pengaruhnya secara jelas
- Prioritaskan kualitas insight dalam laporan

---

## 🔗 Referensi

- Dokumentasi lengkap parameter: buka `docs.html` di browser atau akses via menu **📖 Dokumentasi** di RAG Playground
- Source code: `app.py` — semua parameter ada di bagian `KONFIGURASI INTI`
