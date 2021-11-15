keranjang = []
nama = []
jumlah = []
    
loop = True
 
print('================== Aplikasi List Belanja ==============')
print('======= Selamat Datang Di Aplikasi list Belanja =======')
print('==================== Fiki Andriyan ====================')
print('=======================================================')
while (loop):
    print('================== Menu ==============')
    print('1. Tambah ke Daftar Belanja')
    print('2. List Belanja')
    print('3. Quit/ Keluar')
    print('======================================')
       
    menu = input('Masukan menu = ')

    if menu == "1":
        print("==============")
        print('Silahkan Masukan Keperluan Belanja anda Ke daftar Belanja')
        print('====================== Daftar Belanja ===================')
        tambah_belanja = (input('Mau Belanja Apa :  '))
        nama_pembeli = (input('masukan Nama Anda :  '))
        jumlah_beli = (input('Masukan Jumlah Yang Anda Beli : '))
        keranjang.append(tambah_belanja)
        nama.append(nama_pembeli)
        jumlah.append(jumlah_beli)
        
    elif menu == "2":
        print('===== List Belanja =====')
        for i in range(0,len(keranjang)):
            info_nama = nama[i]
            info_belanja = keranjang[i]
            info_jumlah = jumlah[i]
            print(f'{i +1} . {info_nama} membeli {info_belanja} sejumlah {info_jumlah}')

    elif menu == "3":
        quit()
    else:
        print("Masukan Menu Dengan Benar")
       