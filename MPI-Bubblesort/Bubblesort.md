# MPI-Bubblesort menggunakan Python
Tugas Pemrosesan Paralel MPI Numerik

# Menyiapkan Ubuntu Server dan Linux Mint
## 1.	Pastikan sudah dalam satu jaringan yang sama untu setiap (Master , Worker, Worker1 dan Worker2)
## 2.	Melakukan upgrade OS 

$ sudo apt update && sudo apt upgrade
![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/1683ced5-0a9c-4077-aa76-a5ce2ae5ed66)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/1ef7cba4-fc36-40b1-ba90-5ad5008b0c63)

## 3.	Melakukan penginstalan berikut: net-tools untuk ngecek IP, vim untuk teks editor.

$ sudo apt install net-tools vim
![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/c9c78c35-c6ed-4268-8a7a-dd7c05254cde)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/defeae98-ebfb-41fa-93ca-32750ace1317)

## 4.	Melakukan pengecekan IP dengan perintah berikut:

$ Ifconfig
| NAMA    | Master        | Worker        | Worker2       | Worker3       |
|---------|---------------|---------------|---------------|---------------|
| IP      | 172.20.10.13  | 172.20.10.12  | 172.20.10.10  | 172.20.10.14  |

# Membuat MPI Cluster
## 1.	Konfigurasi hosts file /etc/hosts
- Pada Master
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/4acbd13b-9697-4e43-ad14-85901d8a4491)

- Pada Worker
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/dd4bfc66-d170-4d08-bb36-b6cb57363a88)

- Pada Worker2
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/742e7d3c-8432-43d8-87d8-4e56ffff1e39)

- Pada Worker3 
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/062f847c-1332-4983-8502-2538ce273618)

## 2. Membuat User Baru
Buat user baru di SERVER dan CLIENT. Nama user harus samo semua di seluruh komputer.

$ sudo adduser <nama user>

$ sudo usermod -aG sudo <nama user>

$ su - <nama user>

Server
-	Master
  
 ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/c8a90f06-c3e1-4f1b-bbfa-4d966f84be5a)

Client
-	Worker
  
 ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/3e7be691-f656-49e7-859c-e2452cd3c1d2)

-	Worker2
  
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/6beb8b21-cb4a-463d-b65a-95afa9c04a8a)

-	Worker3
  
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/795f5014-1f43-445b-8009-3461bbda2e4b)

## 3. Konfigurasi SSH
Setelah membuat dan masuk ke user, lakukan konfigurasi SSH.

1. Install SSH
   
$ sudo apt install openssh-server

-	Pada master
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/43e3afd8-5830-405c-b037-e73d0abd2b8f)

-	Pada worker
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/4fd78864-d105-4625-9b4f-cce6b0baaf42)

-	Pada worker2
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/24cb05a5-c36a-44ce-9d0f-4c099d9b3ce7)

-	Pada worker3
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/4e3d78fc-f15c-4825-a533-c90dba78eca3)

2. Melakukan pengecekan SSH
   
$ ssh <nama user>@<host>

-	SSH dari Master ke Worker
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/8d769f2d-ec0c-4128-9d0a-85176126d7a8)

-	SSH dari Worker ke Master
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/7a73feeb-1e20-4189-b4f4-78cf874cf569)

3. Generate Keygen
Lakukan di SERVER

$ ssh-keygen -t rsa

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/1ca483e6-57a9-4e7f-ba0b-b861b17b3bf5)

4. Copy key publik ke client
   
$ cd .ssh

$ cat id_rsa.pub | ssh <nama user>@<host> "mkdir .ssh; cat >> .ssh/authorized_keys"

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/99d2da70-74f2-432f-844c-89f927e8d37d)

## 5. Konfigurasi NFS

1. Buat shared folder

$ mkdir cloud

-	Pada Master
  
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/cd3740ee-bda8-4741-8cae-b8c63b4bb040)

-	Pada Worker
  
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/df5de58a-a766-43c5-9a29-6d5ad761e251)

-	Pada Worker2
  
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/e1b4bcc9-0b4a-4ba7-aabc-b7ef5ec87233)

-	Pada Worker3
  
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/9053c5d1-3383-46e7-b85c-d350b32bc3b9)

2. Install NFS Server

$ sudo apt install nfs-kernel-server

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/3e528d70-efd0-475e-879e-b3c7aae5a78b)

3. Konfigurasi file /etc/exports

<lokasi shared folder> *(rw,sync,no_root_squash,no_subtree_check)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/115e7835-f076-488a-9783-bef03f6a2fc5)

$ sudo exportfs -a

$ sudo systemctl restart nfs-kernel-server

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/2086342f-a786-4b8f-8e9e-f1c4767dfc02)

4. Install NFS Client
      
$ sudo apt install nfs-common

-	Worker
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/b652d435-d875-4802-b0d9-a13a8211c739)


-	Worker2
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/1546a803-2af4-413a-b2d9-670966998cc6)


-	Worker3
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/9bf51dff-a62e-446a-a522-24a0c470299e)

5. Mounting

$ sudo mount <server host>:<lokasi shared folder di server> <lokasi shared folder di client>

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/0caaa377-6248-4c7d-a4b2-f3f01adf6f52)

## 6. Instalasi MPI
1.	Install MPI

$ sudo apt install openmpi-bin libopenmpi-dev

-	Pada Master
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/cc11bc72-d267-4054-900d-6a20fc24d364)


-	Pada Worker
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/812086a1-1e87-474b-a85e-d00cd5ed5b23)


-	Pada Worker2
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/a9d5380f-439e-4810-b346-9e1c99ace759)


-	Pada Worker3
  ![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/bfe8749b-4135-420f-be56-fd09964f638a)

# Menjalankan Program Bubblesort.py
## 1.	Membuat Program

$ touch bubblesort.py

$ sudo nano bubblesort.py

<img width="438" alt="image" src="https://github.com/kikyputraa/Rizki-Putra-Ramadhan_09011182126024_PP_SK5B/assets/150577938/45d8c461-5600-4030-945b-3fa5563b925e">

## 2.	Instalasi Python

$ sudo apt install python3-pip

<img width="311" alt="image" src="https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/ccbd6c34-b70e-42e8-84b9-3e81d104e657">


## 3.	Eksekusi Numerik menggunakan Python

$ python3 bubblesort.py

<img width="394" alt="image" src="https://github.com/kikyputraa/Rizki-Putra-Ramadhan_09011182126024_PP_SK5B/assets/150577938/fc52ca0c-f9b2-46f7-9623-bf371b313e09">

## 4. Eksekusi Bubblesort menggunakan MPI

$ mpirun -np 3 -host master,worker,worker2,worker3 python3 bubblesort.py

<img width="391" alt="image" src="https://github.com/kikyputraa/Rizki-Putra-Ramadhan_09011182126024_PP_SK5B/assets/150577938/46a22e2b-c3dd-4b59-8f00-996159145d52">

