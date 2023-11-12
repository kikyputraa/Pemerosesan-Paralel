# 1. Clone Repositori dan install paket-paket ini :
- Clone repositori yang berisi gambar-gambar yang akan disatukan. Anda telah menggunakan repositori ini: [https://github.com/kaliadi/image-Stiching](https://github.com/kaliadi/image-Stiching).

### pip install opencv-python

### pip install imutils

### pip install imutils numpy opencv-python requests

### sudo apt-get install xvfb

### pip install matplotlib

### sudo apt-get install feh


# 2. Buat Script Image Stitching:
- Gunakan script berikut untuk melakukan image stitching. Simpan script ini sebagai `image_stitching.py`.


# 3. Jalankan Script dengan xvfb-run:
- Gunakan `xvfb-run` untuk menjalankan script tanpa tampilan GUI.
### xvfb-run -s "-screen 0 1920x1200x24" python3 image_stitching.py
- Script ini akan menghasilkan file `output.png`.


# 4. Memindahkan File ke Pengguna Lain:
- Jika perlu, Anda dapat memindahkan file ke pengguna lain dengan perintah `sudo cp` atau `sudo mv`. Pastikan untuk mengganti pengguna_lain dengan nama pengguna yang sesuai.
### sudo cp output.png /home/pengguna_lain/


# 5. Memberikan Izin pada Pengguna Lain:
- Atur kepemilikan file agar pengguna lain dapat membacanya atau memanipulasinya sesuai kebutuhan.
### sudo chown pengguna_lain:pengguna_lain /home/pengguna_lain/output.png


