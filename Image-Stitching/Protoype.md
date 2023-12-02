Proses image stitching tidak menyatukan gambar secara acak. Sebaliknya, ia mencoba untuk menyusun gambar-gambar tersebut secara logis dan koheren berdasarkan fitur-fitur yang ada di dalam gambar. Prosesnya melibatkan:

1. Deteksi Fitur: Setiap gambar dianalisis untuk mendeteksi fitur-fitur khusus seperti sudut, tepi, atau titik-titik unik lainnya.

2. Pencocokan Fitur: Fitur-fitur tersebut kemudian dicocokkan antara dua gambar (atau lebih) untuk menemukan transformasi yang sesuai di antara mereka.

3. Perhitungan Transformasi Perspektif: Berdasarkan pencocokan fitur, dilakukan perhitungan untuk menentukan transformasi perspektif yang memetakan satu gambar ke gambar lainnya.

4. Warping dan Stitching: Gambar-gambar tersebut kemudian "ditarik" atau "diwarp" sesuai dengan transformasi perspektif yang telah dihitung, dan kemudian digabungkan untuk membentuk gambar akhir yang lebih besar.

Proses ini memastikan bahwa gambar-gambar dijahit bersama dengan cara yang logis dan benar secara perspektif. Sehingga, hasil akhirnya terlihat seperti satu gambar yang konsisten, bukan gabungan acak dari beberapa gambar.

# 1. Clone Repositori dan install paket-paket ini :
- Clone repositori yang berisi gambar-gambar yang akan disatukan. Anda telah menggunakan repositori ini: [https://github.com/kaliadi/image-Stiching](https://github.com/kaliadi/image-Stiching).

### pip install opencv-python

### pip install opencv-contrib-python

### pip install imutils

### pip install imutils numpy opencv-python requests

### sudo apt-get install xvfb

### pip install matplotlib

### sudo apt-get install feh

### pip install numpy

### pip install yapf

### pip install pylint

### pip install yapf

<img width="646" alt="image" src="https://github.com/kikyputraa/Rizki-Putra-Ramadhan_09011182126024_PP_SK5B/assets/150577938/2b07d2bc-9b8c-456a-a8de-a42c7617d83e">

# 2. Siapkan MPI dan Buatlah Folder bersama :
<img width="386" alt="image" src="https://github.com/kikyputraa/Rizki-Putra-Ramadhan_09011182126024_PP_SK5B/assets/150577938/a95e3391-f410-4532-8459-8e2adf51c40b">

- Folder yang berisi Video dan Gambar untuk proses Stitching

<img width="284" alt="image" src="https://github.com/kikyputraa/Rizki-Putra-Ramadhan_09011182126024_PP_SK5B/assets/150577938/7c3bc7b7-9ccb-447d-bfe4-9ded16dde247">

<img width="502" alt="image" src="https://github.com/kikyputraa/Rizki-Putra-Ramadhan_09011182126024_PP_SK5B/assets/150577938/d4a1889e-0c6b-4fcc-8c28-aae328462fa7">

# 3. Buat Script Image Stitching:
- Gunakan script berikut untuk melakukan kode python stitching. Simpan script ini sebagai `image_stitching.py`.

<img width="286" alt="image" src="https://github.com/kikyputraa/Rizki-Putra-Ramadhan_09011182126024_PP_SK5B/assets/150577938/c257ac60-be3b-4bd9-8384-38dd9706d320">

<img width="568" alt="image" src="https://github.com/kikyputraa/Rizki-Putra-Ramadhan_09011182126024_PP_SK5B/assets/150577938/9d73c616-2021-498d-abc0-ce1a5a5dda5d">

# 4. Jalankan Script secara individu dengan xvfb-run:
- Gunakan `xvfb-run` untuk menjalankan script tanpa tampilan GUI.
### xvfb-run -s "-screen 0 1920x1200x24" python3 image_stitching.py
- Script ini akan menghasilkan file `output.png`.


# 4. Memindahkan File ke Pengguna Lain:
- Jika perlu, Anda dapat memindahkan file ke pengguna lain dengan perintah `sudo cp` atau `sudo mv`. Pastikan untuk mengganti pengguna_lain dengan nama pengguna yang sesuai.
### sudo cp output.png /home/pengguna_lain/


# 5. Memberikan Izin pada Pengguna Lain:
- Atur kepemilikan file agar pengguna lain dapat membacanya atau memanipulasinya sesuai kebutuhan.
### sudo chown pengguna_lain:pengguna_lain /home/pengguna_lain/output.png


