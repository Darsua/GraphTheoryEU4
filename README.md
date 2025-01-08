# Model Graf Provinsi Europa Universalis IV

Proyek ini bertujuan untuk memodelkan hubungan antar provinsi dalam permainan *Europa Universalis IV* (EU4) menggunakan teori graf. Graf ini digunakan untuk menentukan jalur terpendek antar provinsi dan memvisualisasikan peta dunia berdasarkan hubungan antar provinsi.

## Fitur

- **Pembuatan Daftar Kedekatan**: Membangun graf yang menggambarkan hubungan antar provinsi.
- **Perhitungan Jalur Terpendek**: Menggunakan algoritma Dijkstra untuk menemukan jalur terpendek antara dua provinsi.
- **Visualisasi**: Menampilkan graf dengan menggunakan `matplotlib` dan `networkx`.

## Persyaratan

- Python 3.x
- Library yang dibutuhkan:
  - `PIL` (Python Imaging Library)
  - `networkx`
  - `matplotlib`
  - `csv`
  - `re`

## Fungsi Utama

Fungsi utama proyek ini terdapat pada file `map.py`, yang bertanggung jawab untuk pembuatan graf hubungan antar provinsi.
