# UTS-PBO

•	REQUIREMENT ANALYSIS
Requirement analysis untuk Ukrida E-Library Management System

A.	REQUIREMENT ANALYSIS & FURPS
  
  •	REQUIREMENT ANALYSIS :

  o	Identify the main functionalities required in the library management system.

      1.	Masuk ke Sistem:
             - Sistem akan menampilkan halaman log in bagi pengguna yang ingin mengakses sistem Ukrida E-Library.
             - Untuk mahasiswa ukrida dapat log in dengan memasukkan NIM mahasiswa dan password.

      2.	Mencari Buku:
             - Sistem harus memungkin pengguna untuk mencari buku di dalam sistem tersebut.
             - Pengguna harus dapat memasukkan informasa data diri untuk mencari buku berupa ID buku dan nama buku.
             - Sistem harus memungkinkan pengguna untuk melihat daftar buku yang ada di perpustakaan.

      3.	 Meminjam Buku:
             - Sistem harus memungkin pengguna untuk meminjam buku di dalam sistem tersebut.
             - Sistem harus memungkinkan pengguna untuk melihat stock buku yang terdapat di perpustakaan.
             - Pengguna harus dapat memasukkan informasi nama buku, nama mahasiswa, NIM mahasiswa.
             - Sistem harus memungkinkan jadwal sampai kapan buku dapat dipinjam dan dikembalikan.

      4.	Mengembalikan Buku:
             - Sistem harus mencatat waktu pengembalian dan membandingkannya dengan tanggal jatuh tempo.
             - Jika buku dikembalikan terlambat, sistem harus menghitung denda berdasarkan kebijakan perpustakan.
             - Pengguna harus diberitahu tentang denda melalui sistem dengan pemberitahuan email.
             - Sistem harus memperbarui status buku dari “dipinjam” menjadi “tersedia”.

      5.	Menambah Buku Baru:
             - Sistem harus dapat melakukan input data buku baru.
             - Sistem harus dapat melakukan input data buku baru sesuai tempat buku tersebut.
            
      6.	Memperbarui Detail Buku yang Ada:
             - Sistem harus dapat meng-update ketersediaan buku yang ada.
             - Sistem harus dapat memberikan detail perubahan buku (tempat, dan status).
            
      7.	Mengelola Informasi Anggota:
             - Sistem harus melindungi data pribadi anggota dari akses yang rentan.
             - Sistem harus dapat memasukkan data anggota seperti nama, Alamat, tempat tanggal lahir, dan identifikasi.

      8.	Keluar dari Sistem:
             - Sistem harus dapat menyediakan option keluar dari sistem tersebut Ketika pengguna sudah selesai menggunakan sistem Ukrida E-Library.

  o	Describe how the system should handle usability, reliability, performance, and supportability aspects.

      1.	Kegunaan (Usability):
             - Aksesibilitas: Sistem harus dapat mudah diakses oleh pengguna.
             - Responsif dan Mobile-Friendly: Sistem harus dapat mudah diakses oleh semua pengguna dengan berbagai divice.
            
      2.	Keandalan (Reliability):
             - Pengujian Ekstensif: Sistem harus diuji secara menyuluruh untuk memastikan apakah semua fungsi sistem bekerja dengan efektiv.
             - Pemulihan dari Kegagalan: Sistem harus dapat melakukan pemulihan otomatis untuk memastikan data tidak hilang.
             - Keamanan Data: Sistem harus memperkuat keamanan agar data pada sistem Ukrida E-Library tidak mengalami kebocoran data.

      3.	 Kinerja (Performance):
             - Waktu Muat yang Cepat: Sistem harus dapat mengoptimalisasi kinerjanya agar efisien untuk mempercepat waktu muat halaman.
             - Monitoring dan Optimasi: Sistem harus dapat mengimplementasikan alat monitoring untuk memantau kinerja sistem dan mengidentifikasi apa saja yang membutuhkan pembaruan atau peningkatan.
            
      4.	 Dukungan (Support):
             - Dokumentasi: Menyediakan dokumentasi yang lengkap dan mudah dimengerti untuk pengguna dan administrator sistem.
             - Dukungan Teknis: Tawarkan dukungan teknis melalui kanal seperti telepon, email, dan live chat.
             - Pelatihan Pengguna: Menyediakan sesi pelatihan untuk pengguna utama dan librarian untuk memastikan apakah mereka cukup memahami dalam menggunakan sistem tersebut.
    

  •	IDENTIFY COMPONENT

  o	Based on the requirement analysis, identify the main classes, objects, and methods that will be required to implement the system.

      1.	Kelas, Objek dan Metode (Classes, Objects, and Methods):

        a)	Kelas: Pengguna
            Objek: Student, Librarian
            Metode: login(), logout(), changePassword()
      
        b)	Kelas: Book
            Objek: BookItem
            Metode: searchBook(), returnBook(), updateBookInfo()
            
        c)	Kelas: Librarian
            Objek: StudentMember, LibrarianMember
            Metode: registerMember(), updateMemberInfo(), deactivateMember()

B.	UML Diagrams

    • Use Case Diagram

![Gambar tak berjudul](https://github.com/Oliviaaarst/UTS-PBO/assets/151018674/0ae28e5a-d381-4974-b00d-ce029c0d83d7)
