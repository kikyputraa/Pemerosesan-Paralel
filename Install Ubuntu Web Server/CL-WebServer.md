Untuk menginstal WordPress menggunakan server web Apache di Ubuntu, Anda dapat mengikuti langkah-langkah berikut:

Catatan: Pastikan Anda sudah memiliki server Ubuntu yang diperbarui dan telah masuk sebagai pengguna dengan hak akses superuser (sudo).

# 1. Instal Apache:

   Untuk menginstal server web Apache, jalankan perintah berikut:
   
   ### sudo apt update
   ### sudo apt install apache2
   
   Setelah instalasi selesai, aktifkan dan mulai Apache:
   
   ### sudo systemctl start apache2
   ###  sudo systemctl enable apache2
   

# 2. Instal PHP dan Modulnya:

   Instal PHP dan modul yang diperlukan untuk berjalan bersama Apache:
   
   ### sudo apt install php libapache2-mod-php php-mysql
   

   Setelah instalasi, pastikan PHP bekerja dengan Apache dengan baik:
   ### sudo systemctl restart apache2
   

# 3. **Instal Database Server (MySQL atau MariaDB)**:

   Anda dapat memilih antara MySQL atau MariaDB sebagai server database. Berikut contoh penggunaan mySql:
   
   ### sudo apt install mysql-server
   

# 4. Buat Database dan Pengguna Database:

   Log masuk ke MariaDB sebagai root:
   
   ### sudo mysql
   

   Buat database baru dan pengguna database untuk WordPress. Gantilah nama_database, nama_pengguna, dan password_pengguna sesuai kebutuhan Anda:

   sql
   
   CREATE DATABASE nama_database;
   
   CREATE USER 'nama_pengguna'@'localhost' IDENTIFIED BY 'password_pengguna';
   
   GRANT ALL PRIVILEGES ON nama_database.* TO 'nama_pengguna'@'localhost';
   
   FLUSH PRIVILEGES;
   
   EXIT;
   

# 5. Instal WordPress:

   Unduh dan ekstrak arsip WordPress ke direktori web root. Gantilah nama_folder dengan nama folder yang Anda inginkan:
   
   ### cd /var/www/html
   
   ### sudo wget https://wordpress.org/latest.tar.gz
   
   ### sudo tar -xzvf latest.tar.gz
   
   ### sudo mv wordpress nama_folder
   
   

# 6. Konfigurasi WordPress:

   Buat salinan file konfigurasi WordPress:

  ### sudo cp /var/www/html/nama_folder/wp-config-sample.php /var/www/html/nama_folder/wp-config.php
   

   Selanjutnya, edit file wp-config.php:

  ### sudo nano /var/www/html/nama_folder/wp-config.php
   

   Ganti konfigurasi database dengan informasi yang sesuai yang telah Anda buat sebelumnya:
   
   php
   
   define('DB_NAME', 'nama_database');
   
   define('DB_USER', 'nama_pengguna');
   
   define('DB_PASSWORD', 'password_pengguna');
   
   define('DB_HOST', 'localhost');
   
   Simpan dan keluar dari editor teks.

# 7. Setel Hak Akses:

   Pastikan Apache memiliki hak akses yang tepat ke folder WordPress:

  ### sudo chown -R www-data:www-data /var/www/html/nama_folder
   

# 8. Konfigurasi Web Server:

   Buat konfigurasi server web Apache untuk mengarahkan permintaan ke WordPress. Buat file konfigurasi baru:

  ### sudo nano /etc/apache2/sites-available/nama_domain.conf
   

   Isi konfigurasi server web:
   
       <VirtualHost *:80>
       ServerAdmin admin@nama_domain
       DocumentRoot /var/www/html/nama_folder
       ServerName nama_domain
       ServerAlias www.nama_domain
       <Directory /var/www/html/nama_folder>
           Options FollowSymLinks
           AllowOverride All
           Require all granted
       </Directory>
       ErrorLog ${APACHE_LOG_DIR}/error.log
       CustomLog ${APACHE_LOG_DIR}/access.log combined
       </VirtualHost>
       
   </VirtualHost>
   

   Simpan dan keluar dari editor teks.

# 9. Aktifkan Konfigurasi dan Restart Apache:

   Aktifkan konfigurasi situs dan restart Apache:

  ### sudo a2ensite nama_domain.conf
  ### sudo systemctl restart apache2
   

# 10. Selesaikan Instalasi WordPress:

  Buka web browser Anda dan akses alamat domain atau alamat IP server Ubuntu Anda. Anda akan diarahkan ke halaman penginstalan WordPress. Ikuti petunjuk yang muncul di layar Anda untuk menyelesaikan penginstalan WordPress, termasuk pengaturan bahasa, informasi database, dan akun administrator.

Sekarang Anda sudah menginstal WordPress menggunakan server web Apache di server Ubuntu Anda. Selamat menggunakan!
