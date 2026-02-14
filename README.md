 SIFT Image Forgery Detection

Proyek ini merupakan implementasi Scale-Invariant Feature Transform (SIFT) untuk mendeteksi kemiripan citra dan indikasi pemalsuan gambar (image forgery detection).
Sistem bekerja dengan mengekstraksi fitur lokal (keypoint & descriptor) dari dua citra kemudian mencocokkannya untuk menentukan tingkat kesamaan.

📌 Tujuan

Mendeteksi apakah dua citra berasal dari objek yang sama

Mengidentifikasi kemungkinan manipulasi citra (copy-move, rotasi, crop, dll)

Menganalisis kekuatan dan kelemahan metode SIFT dalam forensik citra digital

🧠 Konsep Utama

Metode yang digunakan:

Keypoint Detection → mencari titik penting pada citra

Descriptor Extraction → merepresentasikan karakteristik lokal

Feature Matching → mencocokkan descript…
 Cara Menjalankan

Masukkan dua gambar ke folder images

Edit nama file di script jika perlu

Jalankan program

python sift_forgery.py
📊 Output Program

Program akan menghasilkan:

Visualisasi keypoint citra pertama

Visualisasi keypoint citra kedua

Visualisasi feature matching

Persentase kemiripan
