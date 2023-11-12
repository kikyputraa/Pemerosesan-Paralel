# MPI-Numeric menggunakan Python
Tugas Pemrosesan Paralel MPI Numerik

# A. Instalasi MPI pada Ubuntu Server
![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/1e455e59-7956-4af9-b63e-6fd75c0fa3db)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/ee84be23-d8eb-412d-956f-6a612fbacc1e)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/527eadc0-d45e-4e33-82e9-e75d4741364e)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/4e18cd25-e7b2-4a6e-9620-4d9314b51514)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/c0800e22-4133-49ca-8b17-aadc2b3d5015)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/9aa5ae23-edb3-4be5-a68b-8fd40fb5fdf7)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/9b0e12ec-7b67-4f35-8a64-b9821742e29f)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/090b8d1f-4e2c-45c0-8d69-94f9f538dc72)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/23847f6b-4e04-4be5-a231-fbf088602348)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/bdbb48a2-fe79-459a-9178-1bda4d04c10b)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/cbdc2fec-d4c3-4a12-a933-f7226658465b)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/ecaaf4e7-2ec9-41d0-91d4-31e763941583)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/8e585a13-f7a4-41d7-92eb-131f30e64975)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/5d24e78b-7df0-4ba3-8d74-2cfb7a50eef2)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/00b874a4-4c71-4deb-adef-b86621c238a8)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/4c7bfd58-3777-4282-ab89-9c3593f95164)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/248f6f8a-a6b7-40a4-8e6e-b2f931318bb1)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/ffa36a78-ccf8-4d6d-b0a3-598c40afd8dd)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/d53d238e-5784-44ac-b43e-33e66953d305)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/0c70d17e-dbb5-43df-8a70-2a4bbea0dc5d)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/0e551d9f-fcc3-4bcd-b53c-de796aa29bb3)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/21a5d870-8d05-429f-9a0b-486a2347020c)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/67e94b23-aca1-4f2d-a615-cfdf7b8cefbf)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/1c24ce01-de28-42d3-a5da-c7fd756b0ed5)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/3420b891-583c-44dd-9a85-2a97c2f368df)

![image](https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/d8432486-077d-40ab-bde8-000c1d51ab40)

# B. Menyiapkan Ubuntu Server dan Linux Mint
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

# C. Membuat MPI Cluster
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

## 7. Menjalankan Program Numerik.py
1.	Membuat Program

$ touch numerik.py

$ sudo nano numerik.py

<img width="441" alt="image" src="https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/ab66a01b-e977-4d95-ae8e-1436a00a5497">

2.	Instalasi Python

$ sudo apt install python3-pip

<img width="311" alt="image" src="https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/ccbd6c34-b70e-42e8-84b9-3e81d104e657">


3.	Eksekusi Numerik menggunakan Python

$ python3 numerik.py

<img width="290" alt="image" src="https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/49d39f2f-3794-42ed-843d-9f323e488724">

4. Eksekusi Numerik menggunakan MPI

$ mpirun -np 3 -host master,worker,worker2,worker3 python3 numerik.py

<img width="295" alt="image" src="https://github.com/Kikyputraa/MPI-Numerik/assets/150577938/98456ccd-f4de-44da-85b5-cc2f04937867">

