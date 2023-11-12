from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Data yang akan dihitung
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Bagi data di antara proses
    chunk_size = len(data) // size
    start = rank * chunk_size
    end = (rank + 1) * chunk_size

    if rank == size - 1:
        # Pastikan semua data terhitung jika panjang data tidak habis dibagi oleh jumlah proses
        end = len(data)

    local_sum = sum(data[start:end])

    # Kumpulkan hasil dari semua proses
    total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

    if rank == 0:
        print("Total hasil perhitungan:", total_sum)

if _name_ == '_main_':
    main()
