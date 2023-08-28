# Data awal Inventaris Barang
data = {
    "KODE BARANG" : ["001", "002", "003", "004"],
    "NAMA BARANG" : ["Lemari Es", "Kipas Angin", "Televisi", "Air Cooler"],
    "SATUAN" : ["Unit", "Unit", "Unit", "Unit"],
    "MERK" : ["Polytron", "Kenword", "Samsung","Bolde"],
    "STOCK AWAL" : [89, 79, 64, 56],
    "TANGGAL MASUK" : ["23-05-2023", "23-05-2023", "21-05-2023", "28-05-2023"],
    "TANGGAL KELUAR" : ["05-04-2023", "06-04-2023", "-", "-"],
    "TOTAL KELUAR" : [49, 30, 0, 0],
    "STOCK AKHIR" : [40, 59, 64, 56]
    }

### mencetak table
def cetak_table(data):
    print("-"*150)
    # menampilkan nama kolom
    for column in data.keys():                                          # Mula2 mencetak keys ditampilkan sebagai nama kolom
        print(f"| {column:<15}", end="")
    print()

    # menampilkan isi tabel
    for i in range(len(data["KODE BARANG"])):                           # melakukan iterasi sebanyak data pada kode barang
        for column, values in data.items():                             # mencetak data barang sebanyak kode barang
            print(f"| {values[i]:<15}", end="")
        print()
    
    print("-"*150)

### mencetak tabel berdasarkan kode barang bisa lebih dari dua kode barang
def kodeBarang(kode_barang_list):
    print("-"*150)

    for column in data.keys():                                          # Mula2 mencetak keys ditampilkan sebagai nama kolom
        print(f"| {column:<15}", end="")
    print()

    for kode_barang in kode_barang_list:                                # melakukan iterasi sebanyak data di kode_barang_list
        if kode_barang in data["KODE BARANG"]:                          # dilakukan pengecheckan apakah data kode_barang terdapat di dict data[KODE BARANG] 
            index = data["KODE BARANG"].index(kode_barang)              # jika betul data kode_barang dicari index nya  
            for values in data.values():
                print(f"| {values[index]:<15}", end="")                 # setelah itu index digunakan untuk menampilkan data kode_barang berdasarkan dict data  
            print()
        elif kode_barang not in data["KODE BARANG"]:                    # jika data kode_barang tidak terdapat di dict data                 
            print()                                                     # maka akan muncul peringatan
            print(f"kode barang {kode_barang} tidak ditemukan")
            print("Periksa kembali input kode barang yang anda masukkan")

    print("-"*150)

### Fungsi utama untuk menampilkan data berdasarkan kode barang
def read_menu_kode():
    QE1 = input("Apakah anda sudah menyiapkan input data? (yes/no): ").lower()
    if QE1 == 'yes':                                                                   # jika mode input 'yes'
        print()
        print("-"*150)
        print("RULES")
        print("-"*150)
        print()
        print("** KODE BARANG hanya bisa dimasukkan dengan angka dari 001 - 999")          

        print()
        kode = input("Masukkan kode barang yang ingin anda cari: ")                     # menginputakan kode barang dijadikan sebagai pengecheckan pertama apakah data tersedia atau tidak
        print()

        kode_barang_list = list(kode.split())                                           # kode barang yang dimasukkan di split berdasarkan spasi
        kodeBarang(kode_barang_list)                                                    # memanggil fungsi KodeBarang(kode_barang_list) untuk mencetak tabel
        read_menu()

    elif QE1 == 'no':                                                                   # jika mode input 'no'
        print()
        read_menu()                                                                     # mengembalikan ke fungsi read_menu
        print()

    else:
        print()                                                                         # jika mode input salah
        print("Data yang anda masukkan tidak terisedia")
        print("Harap memasukkan data dengan benar")
        print("Bacalah kembali RULES yang telah diberikan")
        print()
        read_menu_kode()
        print()

### mencetak table berdasarkan nama barang
def namaBarang(nama):
    print("-"*150)

    for column in data.keys():                                                          # mencetak keys values dijadikan sebagai nama kolom
        print(f"| {column:<15}", end="")
    print()

    if nama in data["NAMA BARANG"]:                                                     # jika nama barang ada di dict data[NAMA BARANG]
        index = data["NAMA BARANG"].index(nama)                                         # mencari index nya
        for values in data.values():
            print(f"| {values[index]:<15}", end="")                                     # mencetak values nya
        print()
    elif nama not in data["NAMA BARANG"]:                                               # jika tidak
        print()                                                                         # muncul peringatan
        print(f"nama barang {nama} tidak ditemukan")
        print("Periksa kembali input nama barang yang anda masukkan")

    print("-"*150)

# Fungsi utama untuk menampilkan data berdasarkan nama barang
def read_menu_nama():
    QE1 = input("Apakah anda sudah menyiapkan input data? (yes/no): ").lower()
    if QE1 == 'yes':                                                                    # jika iya
        print()
        print("-"*150)
        print("RULES")
        print("-"*150)
        print()
        print("** Nama barang diawali dengan huruf capital")
            
        print()
        QE1 = input("Masukkan NAMA BARANG yang ingin anda cari: ").title()
        print()
        namaBarang(QE1)                                                                 # mencetak tabel sesuai nama barang
        print()
        read_menu()
            
    elif QE1 == 'no':                                                                   # jika tidak
        print()
        read_menu()                                                                     # kembali ke menu read_menu
        print()

    else:
        print()                                                                         # jika mode menu salah
        print("Input mode menu yang anda masukkan tidak sesuai")                        
        print("Harap input kembali dengan benar")
        main_menu()                                                                     # kembali ke main menu
        print()

# mencetak table berdasarkan tanggal masuk
def sorted_data_stock_in():
    print("-"*150)
    sorted_data = sorted(data["TANGGAL MASUK"])

    found_index = []
    
    for column in data.keys():                                                          # menampilkan keys values sebagai nama kolom tabel
        print(f"|{column:<15}", end="")
    print()

    for idx in sorted_data:
        index = data["TANGGAL MASUK"].index(idx)                                        # mencari index pada data sort TANGGAL MASUK                  
        if index in found_index:                                                        
            index += 1                                                                  # jika index sebelumnya sama dengan index setelahnya
            found_index.append(index)                                                   # index tsb ditambah angka 1 dan hasilnya dimasukkan ke list found_index
        else:                                                                           # jika index TIDAK SAMA DENGAN SEBELUMNYA
            found_index.append(index)                                                   # index tersebut langsung dimasukkan ke list found_index
        
    for i in found_index:                                                               # mencetak values dict data berdasarkan found_index
        for values in data.values():
            print(f"|{values[i]:<15}", end="")
        print()
    print("-"*150)

# mencetak table berdasarkan tanggal keluar
def sorted_data_stock_out():
    print("-"*150)
    sorted_data = sorted(data["TANGGAL KELUAR"])

    found_index = []
    
    for column in data.keys():
        print(f"|{column:<15}", end="")                                             # menampilkan keys values sebagai nama kolom tabel
    print()

    for idx in sorted_data:
        index = data["TANGGAL KELUAR"].index(idx)                                   # mencari index pada data sort TANGGAL KELUAR
        if index in found_index:                                            
            index += 1                                                              # jika index sebelumnya sama dengan index setelahnya
            found_index.append(index)                                               # index tsb ditambah angka 1 dan hasilnya dimasukkan ke list found_index 
        else:                                                                       # jika index TIDAK SAMA DENGAN SEBELUMNYA
            found_index.append(index)                                               # index tersebut langsung dimasukkan ke list found_index
        
    for i in found_index:                                                           # mencetak values dict data berdasarkan found_index
        for values in data.values():
            print(f"|{values[i]:<15}", end="")
        print()
    print("-"*150)

# Fungsi utama untuk menampilkan data sorting berdasarkan tanggal masuk dan tanggal keluar
def sort_keluar_masuk():               
    user_input = input("Masukan nama kolom untuk mensorting data (MASUK/KELUAR): ").upper()
    
    if user_input == "MASUK":
        print()
        print("-"*150)
        sorted_data_stock_in()
        print("-"*150)
        print()
    elif user_input == "KELUAR":
        print()
        print("-"*150)
        sorted_data_stock_out()
        print("-"*150)
        print()
    else:
        print()
        print("Mode input yang anda masukkan salah")
        print("Harap memasukkan mode input dengan benar")
        print()
        sort_keluar_masuk()

# Fungsi Menu 1 stock barang masuk
#### Fungsi ini memiliki alur menampilkan daftar barang, tambah barang, update barang
#### Jika inputan data SESUAI akan meneruskan ke fungsi yang lain sesuai perintah inputan
#### Jika inputan data TIDAK SESUAI maka akan KEMBALI KE MENU STOCK BARANG MASUK
def stock_in():
    print()
    print("-"*150)
    print("Tampilan Stock Barang Masuk")
    print("-"*150)
    print()
    print("1. Tampilan Daftar Barang")
    print("2. Tambah Daftar Barang")
    print("3. Update Daftar Barang")
    print("4. Kembali ke Main Menu")
    print()
    user_input = input("Masukkan mode menu yang ingin dijalankan: ")

    if user_input == '1':
        print()
        read_menu()                                                                     # untuk menampilkan table data
        print()
        
    elif user_input == '2':
        print()
        tambah_barang()                                                                 # untuk menambahkan data barang
        print()
        
    elif user_input =='3':
        print()
        update_barang()                                                                 # untuk mengupdate data barang masuk
        print()
        
    elif user_input == '4':
        print()
        main_menu()
        print()

    else:
        print()
        print("Mode menu yang anda masukkan salah")
        print("Harap memasukkan sesuai dengan perintah")
        print("Anda kembali ke halaman utama")
        print()
        stock_in()

# Fungsi utama menampilkan daftar barang
def read_menu():
    print()
    print("-"*150)
    print("Tampilan Menu Daftar Barang")
    print("-"*150)
    print()
    print("1. Seluruh data iventaris yang tersedia")                    
    print("2. Berdarkan kode barang")
    print("3. Berdasarkan nama barang")                                
    print("4. Sorting barang berdasarkan tanggal")
    print("5. Kembali ke Tampilan Stock Barang Masuk")
    
    print()
    user_input = input("Masukkan mode menu yang ingin dijalankan: ")
    print()

    if user_input == '1':
        print()
        cetak_table(data)                                                       # fungsi ini bertujuan untuk mencetak table
        print()
        read_menu()                                                             # kembali ke menu read_menu()
        input("Tekan ENTER untuk kembali ke menu Tampilan Daftar Barang")
        read_menu()
        print()

    elif user_input == '2':
        print()
        read_menu_kode()                                                        # menampilkan data berdasarkan kode barang

    elif user_input == '3':
        print()
        read_menu_nama()                                                        # menampilkan data berdasarkan nama barang

    elif user_input == '4':
        print()
        print("Sorting Data Barang Berdasarkan Tanggal")
        print()
        print("RULES")
        print("*** Harap menginputkan dengan HURUF CAPITAL")
        print()
        sort_keluar_masuk()                                                     # menampilkan hasil sorting data berdasarkan tanggal masuk atau keluar
        read_menu()

    elif user_input == '5':
        print()
        print("Anda kembali ke menu Tampilan Stock Barang Masuk")
        stock_in()                                                              # ke menu stock in
        print()

    else:
        print() 
        print("Mode menu yang anda inputkan salah")
        print("Harap memasukan mode menu yang sesuai")
        read_menu()                                                             # kembali ke menu read menu
        print()

# Fungsi utama menambahkan data barang
def tambah_barang():    
    print("-"*150)
    print("Tampilan Tambah Daftar Barang")
    print("-"*150)
    print("-"*150)
    print("Rules")
    print("-"*150)
    print("*** Pastikan data anda tidak DUPLICATE")
    print("*** Kolom TANGGAL isikan tanggal-bulan-tahun")
    print("*** Mohon isikan data dengan lengkap")
    print("*** Pastikan data anda tidak NONE")
    print("-"*150)
    print()

    user_input = input("Apakah anda ingin menambahkan data? (yes/no): ").lower()
    
    if user_input == 'yes':
        new = data["KODE BARANG"]
  
        a = input("KODE BARANG: ")

        if a in new:
            print("Data telah tersedia sebelumnya")
            print("Anda TIDAK BISA memasukkan DUPLICATE data")
            print("Silahkan inputkan data kembali")
            print()
            tambah_barang()                                                      # untuk menambahkan data

        elif a not in new:
            b = input("NAMA BARANG: ")
            c = input("SATUAN: ")
            d = input("MERK: ")
            e = input("STOCK AWAL: ")
            f = input("TANGGAL MASUK: ")
        
            if e.isdigit() == False:
                print()
                print("Inputan STOCK AWAL yang anda masukkan salah")
                print("Harap memasukkan dengan inputan STCOK AWAL dengan bilangan integer")
                print()
                tambah_barang()

            else:
                e = int(e)
                print()
                validasi = input("Apakah anda akan menyimpan data ini?(yes/no): ").lower()
                print()
            
                if validasi == "yes":
                    print("-"*150)
                    data['KODE BARANG'].append(a)
                    data['NAMA BARANG'].append(b)
                    data['SATUAN'].append(c)
                    data['MERK'].append(d)
                    data['STOCK AWAL'].append(e)
                    data['TANGGAL MASUK'].append(f)
                    data['TANGGAL KELUAR'].append("-")
                    data['TOTAL KELUAR'].append(int(0))
                    data['STOCK AKHIR'].append(e-int(0))
                    print()
                    sorted_data_stock_in()                                              # menampilkan data hasil sorting tanggal masuk
                    print("Data Succesfully Updated")
                    print()
                    tambah_barang()
                    print()
                elif validasi == "no":
                    print("Data yang anda masukkan tidak tersimpan")
                    print()
                    tambah_barang()
                    print()
                else:
                    print("Perintah mode yang anda masukkan salah")
                    print("Harap input dengan benar")
                    print()
                    tambah_barang()
                    print()
           
    elif user_input == 'no':
        
        validasi = input("Apakah anda tetap ingin keluar dari mode tambah barang masuk? (yes/no): ").lower()
        
        if validasi == 'yes':
            print()
            main_menu()
            print()
        elif validasi == 'no':
            print()
            tambah_barang()
            print()
        else:
            print("Perintah mode yang anda masukkan salah")
            print("Harap ulangi inputan anda")
            print()
            tambah_barang()
            print()
    else:
        print("Perintah mode yang anda inputkan salah")
        print("Harap memasukan perintah dengan benar")
        print()
        tambah_barang()
        print()      

# mencetak table berdasarkan kode barang tertentu hanya satu kode barang
def check_barang(str):
    print("-"*150)

    if str in data["KODE BARANG"]:                                              # check apakah data ada di dict['KODE BARANG']
        index = data["KODE BARANG"].index(str)                                  # dicari index datanya

    my_dict = {}                                                                # buat dict temporary

    for key, values in data.items():                                            # masukkan key dan values dict temporary berdasarkan dict data
        my_dict[key] = values[index]

    for column in my_dict.keys():                                               # menampilkan keys dari dict temporary sebagai kolom 
        print(f"| {column:<15}", end="")
    print()
    
    for values in my_dict.values():                                             # menampilkan values dari dict temporary sebagai data kolom 
        print(f"| {values:<15}", end="")
    print()

    print("-"*150)

# Fungsi utama update data barang baru
def update_barang():
    print()
    print("-"*150)
    print("Tampilan Update Menu")
    print("-"*150)
    print()
    print("1. Mengganti values dari kolom yang telah tersedia")
    print("2. Kembali ke menu Tampilan Stock Barang Masuk")
    print()
    user_input = input("Masukkan mode menu yang ingin anda jalankan? : ")
    print()

    if user_input == '1' :
        print("-"*150)
        print("RULES")
        print("-"*150)
        print()
        print("-"*150)
        print("** Masukkan terlebih dahulu KODE BARANG yang ingin anda update")
        print("** KODE BARANG diisi dengan angka dari 001 - 999")
        print("** Nama Kolom diisi dengan HURUF BESAR")
        print("** Pastikan data yang anda masukkan benar")
        print("-"*150)
        
        print()
        new = input("Masukkan KODE BARANG : ")
        print()

        if new in data["KODE BARANG"]:                                                  
            check_barang(new)                                                           # menampilkan hanya satu data saja
            print()
            index = data["KODE BARANG"].index(new)
            new2 = input("Masukkan kolom yang ingin anda ubah: ").upper()

            if new2 == "STOCK AWAL":                                                    # jika update data kolom STOCK AWAL
                ubah1 = input("STOCK AWAL: ")
                ubah2 = input("TANGGAL MASUK: ")
                ubah1 = int(ubah1)
                data["TANGGAL MASUK"][index] = ubah2
                data["STOCK AKHIR"][index] = data["STOCK AWAL"][index] + ubah1          # stock akhir penjumlahan dari stock awal dan data baru
                data["STOCK AWAL"][index] = data["STOCK AWAL"][index] + ubah1           # stock awal baru penjumlahan stock awal baru dan data baru
                cetak_table(data)
                print()
                update_barang()
            else:                                                                       # jika tidak
                ubah1 = input(f"{new2}: ")                                              # diganti kolom apa
                data[new2][index] = ubah1                                               # di inputkan data baru berdasarkan index datanya
                print()
                cetak_table(data)                                                      # menampilkan seluruh data
                print("Data Successfully updated")
                update_barang()

        elif new not in data["KODE BARANG"]:
            print("Anda tidak dapat melakukan updating data")
            print("KODE BARANG yang anda masukkan tidak tersedia")
            print("Harap cek ulang lagi KODE BARANG")
            update_barang()
        else:
            print("Anda salah melakukan input data")
            print("Silahkan baca kembali RULES")
            update_barang()

    elif user_input == '2':
        print()
        print("Anda kembali ke halaman menu utama")
        print()
        stock_in()                                                                     # kembali ke menu stock in barang
    else:
        print("Mode menu yang anda inputkan salah")
        print("Harap memasukkan mode menu dengan benar")
        update_barang()

# untuk menginputkan data barang keluar
def daftar_keluar():
    print()
    print("-"*150)
    print("Tampilan Daftar Keluar Barang")
    print("-"*150)
    print()
    print("RULES")
    print()
    print("-"*150)
    print("** Masukkan terlebih dahulu KODE BARANG yang ingin anda update")
    print("** KODE BARANG diisi dengan angka dari 001 - 999")
    print("** Pastikan data yang anda masukkan benar")
    print("** Nama Kolom diisi dengan HURUF BESAR")
    print("-"*150)
        
    print()
    new = input("Masukkan KODE BARANG : ")
    print()

    if new in data["KODE BARANG"]:
        check_barang(new)
        print()
        index = data["KODE BARANG"].index(new)
        tanggal = input("TANGGAL KELUAR: ")
        keluar = input("TOTAL KELUAR: ")

        if keluar.isdigit() == False:                                                                   # jika kode barang isdigit == False
            print()                                                                                     # muncul peringatan
            print("Inputan TOTAL KELUAR yang anda masukkan salah")
            print("Harap memasukkan dengan bilangan integer")
            print() 
            daftar_keluar()
 
        else:                                                                                           # jika isdigit == True
            keluar = int(keluar)                                                                        # total keluar diubah ke int
            if keluar > data["STOCK AWAL"][index]:                                                      # di check apakah lebih besar dari stock awal
                print()                                                                                 # jika iya
                print("Anda tidak bisa memasukkan angka total keluar lebih dari stock awal")            # muncul peringatan
                print("Silahkan input total keluar tidak melebihi stock awal")
                daftar_keluar()
                print()
            else:                                                                                       # jika tidak
                data["TANGGAL KELUAR"][index] = tanggal
                data["TOTAL KELUAR"][index] = keluar
                print()
                data["STOCK AKHIR"][index] = data["STOCK AWAL"][index] - data["TOTAL KELUAR"][index]    # dilakukan operasi pengurangan
                sorted_data_stock_out()
                print("Data Successfully Updated")
                print()
                input("Tekan ENTER untuk kembali ke menu Tampilan Stock Barang Keluar")
                stock_out()
        
    elif new not in data["KODE BARANG"]:
        print("Anda tidak dapat melakukan input daftar barang")
        print("KODE BARANG yang anda masukkan tidak tersedia")
        print("Harap cek ulang lagi KODE BARANG")
        daftar_keluar()

    else:
        print()
        print("Mode menu yang anda inputkan salah")
        print("Harap memasukkan mode menu dengan benar")
        stock_out()
        print()

# Fungsi Menu 2 stock barang keluar
#### Fungsi ini memiliki alur menampilkan daftar barang, menginputkan data barang keluar
#### Jika inputan data SESUAI akan meneruskan ke fungsi yang lain sesuai perintah inputan
#### Jika inputan data TIDAK SESUAI maka akan KEMBALI KE MENU STOCK BARANG KELUAR
def stock_out():
    print()
    print("-"*150)
    print("Tampilan Stock Barang Keluar")
    print("-"*150)
    print()
    print("1. Tampilan Daftar Barang")
    print("2. Input Daftar Keluar Barang")
    print("3. Kembali ke Main Menu")
    print()

    user_input = input("Masukkan mode menu yang ingin dijalankan: ")

    if user_input == '1':
        print()
        print("-"*150)
        print("Tampilan Daftar Barang")
        print("-"*150) 
        print()
        cetak_table(data)
        print()
        input("Tekan ENTER untuk kembali ke menu Tampilan Daftar Barang")
        stock_out()
        print()
                
    elif user_input =='2':
        print()
        daftar_keluar()
        print()

    elif user_input =='3':
        print()
        main_menu()
        print()
    else:
        print()
        print("Mode menu yang anda masukkan salah")
        print("Harap memasukkan sesuai dengan perintah")
        print("Anda kembali ke halaman utama")
        print()
        stock_out()

# Fungsi Menu 3 Hapus Data Barang
#### Fungsi ini memiliki alur menghapus data barang satu per satu
#### Jika inputan data SESUAI akan menghapus barang secara permanen 
#### Jika inputan data TIDAK SESUAI maka akan KEMBALI KE MENU UTAMA
def hapus_barang():
    print("-"*150)
    print("Tampilan Delete Daftar Barang")
    print("-"*150)
    print()
    print("Rules")
    print("*** Input data KODE BARANG diawali dari 001 - 999")
    print()
    user_input = input("Apakah anda yakin ingin menghapus data barang? (yes/no): ").lower()
    print()

    if user_input == 'yes':
        kode = input("Masukkan kode barang yang ingin anda hapus? ")
        if kode in data["KODE BARANG"]:
            index = data["KODE BARANG"].index(kode)
            print()
            check_barang(kode)
            print()

            for key in data.keys():
                del data[key][index]
                print()
                cetak_table(data)
                print(f"kolom dengan kode barang {kode} telah sukses dihapus")
                print()
                input("Tekan tombol ENTER untuk kembali ke halaman Detele Daftar Barang")
                hapus_barang()

        else:
            print()
            print("KODE BARANG yang anda masukkan tidak tersedia")
            print("Harap periksa kembali inputan anda")
            print()
            hapus_barang()
    
    elif user_input == 'no':
        print()
        print("Anda kembali Tampilan Dafar Tampilan Hapus Barang")
        main_menu()

    else:
        print()
        print("KODE BARANG yang anda inputkan tidak tersedia")
        print("Silahkan periksa kembali inputan anda")
        print()
        main_menu()       

# mencetak tabel laporan barang
def print_laporan_barang():
    print("| KODE BARANG                    | NAMA BARANG                   | SATUAN                    | MERK                  | STOCK AKHIR                   |")
    print("-"*150)

    kode = data["KODE BARANG"]
    nama = data["NAMA BARANG"]
    satuan = data["SATUAN"]
    merk = data["MERK"]
    akhir = data["STOCK AKHIR"]

    for i in range(len(data["KODE BARANG"])):
        print(f"| {kode[i]:<30} | {nama[i]:<29} | {satuan[i]:<25} | {merk[i]:<21} | {akhir[i]:<29} |")

# Fungsi Menu 4 Laporan Barang
#### Fungsi ini memiliki alur menginputkan data pegawai 
#### setelah itu menampilkan data utama --> kode, nama, satuan, merk, stock akhir
def laporan_barang():
    print()
    print("Masukkan data petugas pengisi laporan barang")
    nama = input("Nama petugas: ")
    jabatan = input("Jabatan petugas: ")
    tanggal = input("Tanggal: ")
    lokasi = input("Gudang: ")
    print()

    print(" "*63, "Laporan Inventaris Barang"," "*62)
    print("-"*150)
    print(f"Nama Petugas    : {nama}", " "*60, f"Jabatan Petugas    : {jabatan}")
    print(f"Tanggal         : {tanggal}", " "*53, f"Gudang             : {lokasi}")
    print("-"*150)
    print()
    print_laporan_barang()

    print()
    QE1 = input("Apakah anda ingin keluar dari tampilan laporan inventaris barang? (yes/no)")
    if QE1 == 'yes':
        print()
        main_menu()
        print()

    elif QE1 == 'no':
        print()
        print("Anda kembali ke tampilan laporan inventaris barang")
        print()
        laporan_barang()
        print()
    else:
        print()
        print("Perintah mode menu yang anda masukkan salah")
        print("Harap memasukkan mode menu dengan benar")
        print()
        laporan_barang()

# Fungsi utama program
def main_menu():
    print("-"*150)
    print("Selamat Datang di Aplikasi Inventaris Barang")
    print("-"*150)
    print()
    print("""
    1. Stock Barang Masuk
    2. Stock Barang Keluar
    3. Hapus Data Barang
    4. Laporan Barang
    5. Keluar Program
    """)
    print()

    user_input = input("Masukkan mode menu yang anda pilih: ")

    if user_input == '1':
        print()
        stock_in()
        print()

    elif user_input == '2':
        print()
        stock_out()
        print()

    elif user_input == '3':
        print()
        hapus_barang()
        print()

    elif user_input == '4':
        print()
        laporan_barang()
        print()

    elif user_input == '5':
        print("-"*53,"Terimakasih Telah Menggunakan Aplikasi Kami", "-"*53)
        print("-"*60, "Happy Nice Day", "-"*75)
        exit()
    
    else:
        print()
        print("Mode menu yang anda masukkan salah")
        print("Harap memasukkan mode menu sesuai dengan perintah")
        print("Anda kembali ke halaman utama")
        main_menu()    

main_menu()