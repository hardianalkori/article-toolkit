# article-toolkit
Article Toolkit adalah sebuah aplikasi berbasis web yang memiliki beberapa fitur seperti deteksi tema pada artikel, perangkuman artikel, dan error correction untuk mendeteksi typo.

Article Toolkit mengimplementasikan beberapa metode text processing dan machine learning klasik seperti:
1. Deteksi Tema (TF-IDF, Random Forest)
2. Perangkuman Artikel (TF-IDF)
3. Error Correction / Deteksi Typo (Levenshtein Distance)

# Penggunaan
1. buka command prompt kemudian pindah ke direktori article-toolkit
2. install paket yang dibutuhkan dengan cara mengetik pip install -r requirements.txt
3. jalankan perintah streamlit run "Halaman Utama.py"

# Issue
masih ada issue untuk error correction dikarenakan untuk melakukan koreksi typo harus dikembangkan lagi karena tidak cukup hanya menghitung cost yang dihasilkan oleh perhitungan levenshtein distance.
ada metode yang harus dilakukan seperti memeriksa grammar agar hasil dari perbaikan typo nya lebih baik.
