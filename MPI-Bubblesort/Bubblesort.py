rom mpi4py import MPI
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

# Membuat 10 array acak
array_list = [random.sample(range(1, 1000), 10) for _ in range(10)]

# Menampilkan data mentah dan data yang sudah diurutkan
for i, arr in enumerate(array_list):
    print(f"Data mentah array {i + 1}: {arr}")
    
    # Mengukur waktu eksekusi Bubble Sort dan mengurutkan array
    start_time = time.time()
    bubble_sort(arr)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Data yang sudah diurutkan array {i + 1}: {arr}")
    print(f"Waktu eksekusi: {elapsed_time:.6f} detik\n")

# Menampilkan array yang belum terurutkan
unsorted_arrays = [unsorted_arrays[i] for i, arr in enumerate(array_list) if arr != sorted(arr)]
print(f"Jumlah array yang belum terurutkan: {len(unsorted_arrays)}")
