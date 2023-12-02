import numpy as np
import glob
import cv2
import time

def add_watermark(image, watermark_text):
    # Tentukan font, skala, dan ketebalan teks
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 1.2  # Menyesuaikan skala font
    thickness = 2  # Menyesuaikan ketebalan teks

    # Tentukan posisi watermark (kanan bawah)
    position = (10, image.shape[0] - 10)

    # Tentukan warna dan ukuran font
    color = (255, 255, 255)  # Putih

    # Tambahkan teks sebagai watermark
    cv2.putText(image, watermark_text, position, font, scale, color, thickness, cv2.LINE_AA)

    return image

def stitch_images(image_paths, output_path, watermark_text):
    # Baca gambar-gambar
    images = [cv2.imread(img) for img in image_paths]

    # Inisialisasi jahitan (stitcher)
    stitcher = cv2.Stitcher_create()

    # Inisialisasi detektor SIFT
    sift = cv2.SIFT_create()

    # Deteksi fitur kunci dan deskriptor untuk setiap gambar
    keypoints = [sift.detectAndCompute(img, None) for img in images]

    # Jahit gambar-gambar
    status, panorama = stitcher.stitch(images)

    # Periksa apakah jahitan sukses
    if status == cv2.Stitcher_OK:
        # Tambahkan watermark pada hasil jahitan
        panorama_with_watermark = add_watermark(panorama, watermark_text)

        # Simpan hasil jahitan dengan watermark
        cv2.imwrite(output_path, panorama_with_watermark)
        print(f"Jahitan dengan watermark berhasil disimpan di: {output_path}")
    else:
        print("Jahitan gagal.")

# Contoh pemanggilan fungsi dengan waktu pengerjaan
image_paths = glob.glob("Gambar/*.jpeg")
output_path = "hasil.jpg"
watermark_text = "-3.2196917214319014, 104.65155520427352"

start_time = time.time()  # Waktu mulai eksekusi

stitch_images(image_paths, output_path, watermark_text)

end_time = time.time()  # Waktu selesai eksekusi
execution_time = end_time - start_time  # Waktu total eksekusi

print(f"Total waktu yang dibutuhkan: {execution_time:.2f} detik")
