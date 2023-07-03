import json
import os
import time
import datetime

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

fileData = "dataUser.json"
dataUser = {}

username = []
password = []
konsul = []
waktu = []

def bacaData():
    global data, username, password, konsul, waktu
    try:
        with open(fileData, 'r') as file:
            data = json.load(file)
            username = data["username"]
            password = data["password"]
            konsul = data["konsul"]
            waktu = data["waktu"]
    except IOError as e:
        print(e)

    tulisData()

def tulisData():
    dataUser = {"username" : username, "password" : password, "konsul" : konsul, "waktu" : waktu}

    with open(fileData, 'w') as file:
        json.dump(dataUser, file)

#REGISTRASI----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def registrasi():
    global dataUser
    clean()
    print("~~ MENU REGRISTASI ~~")
    user = input("Masukkan Username Baru : ")
    passs = input("Masukkan Password Baru : ")

    bacaData()
    username.append(user)
    password.append(passs)
    konsul.append([])
    waktu.append([])
    tulisData()

    print("Username Dan Password Berhasil Disimpan, Silahkan Login ")
    time.sleep(2)
    main()

#LOGIN-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Masuk():
    global indexUser
    clean()
    bacaData()

    while True:
        print("~~ MENU LOGIN ~~")
        user = input("Masukkan Username : ")
        passs = input("Masukkan Password : ")
        if user in data["username"]:
            indexUser = data["username"].index(user)
            if passs == data["password"][indexUser]:
                print('ANDA BERHASIL LOGIN!')
                time.sleep(0.5)
                main_menu()
                break
            else:
                print("Username atau Password salah")
                time.sleep(0.5)
                clean()
        else:
            print("Username atau Password salah")
            time.sleep(0.5)
            clean()

#MENU AWAL---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    clean()
    print('''
            SELAMAT DATANG DI HALODOC
            1. Buat Akun
            2. Login
         ''')
    choice = input("Silahkan Pilih : ")

    if choice == "1" or choice == "buat akun" or choice == "Buat Akun" or choice == "BUAT AKUN":
        registrasi()

    elif choice == "2" or choice == "login" or choice == "Login" or choice == "LOGIN":
        Masuk()

#TANGGAL------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def tanggal():
    global waktu
    current = datetime.datetime.now()
    hari = current.day
    bulan = current.month
    tahun = current.year
    tanggal = f"{hari}-{bulan}-{tahun}" #digunakan untuk menampilkan waktu
    waktu[indexUser].append(tanggal)

#MENU UTAMA--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main_menu() :
    clean()
    print(" ~~ WELLCOME TO HELLODOC ~~")
    print("1. Konsultasi              ")
    print("2. Biaya Konsultasi        ")
    print("3. Struk Pembayaran        ")
    print("4. Data Konsultasi         ")
    print("5. Report Data             ")
    print("6. Logout                  ")
    nomer = int(input(" SILAHKAN PILIH MENU ---> "))
    if nomer == 1:
        konsultasi()
    elif nomer == 2:
        if len(data['konsul'][indexUser]) >= 1:
            biaya_konsultasi()
        else:
            biaya_belumkonsul()
    elif nomer == 3:
        if len(data['konsul'][indexUser]) >= 1:
            struk_pembayaran()
        else:
            struk_belumkonsul()
    elif nomer == 4:
        data_konsultasi()
    elif nomer == 5:
        report_data()
    elif nomer == 6:
        print("="*81)
        print("TERIMAKASIHHHH")
        print("="*81)
        exit()
    else:
        print('''
        "pilihan Tidak Sesuai! 
        Masukkan Pilihan Sesuai Kategori Menu Yang Tersedia."
        ''')
        main_menu()

#KONSULTASI---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def konsultasi():
    clean()
    print("----------------------------------------------------")
    print(f"                 HALO {data['username'][indexUser]} DISINI           ")
    print("           SILAHKAN LENGKAPI PERTANYAAN             ")
    print("----------------------------------------------------")
    print("Silahkan Membaca Keluhan Dibawah Ini :)          ")
    print("1. Demam Tinggi                                  ")
    print("2. Diare                                         ")
    print("3. Sakit Kepala                                  ")
    print("4. Fases Lembek Dan Cair                         ")
    print("5. Mual Dan Muntah                               ")
    print("6. Teggorokan Sakit Saat Menelan                 ")
    problem       = input("Apa Keluhan Yang Anda Alami                                          : ")

    if problem == "1" :
        tipes()
    elif problem == "2" :
        diare()
    elif problem == "3" :
        sakit_kepala()
    elif problem == "4" :
        diaree()
    elif problem == "5" :
        mual_muntah()
    elif problem == "6" :
        radang_tenggorokan()
    else :
        print('''
                "Pilihan Tidak Sesuai! 
                Masukkan Pilihan Sesuai Ketentuan"
             ''')
        konsultasi()

#KONSULTASI LANJUTAN---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def tipes() :
    clean()
    print("Silahkan Membaca Keluhan Dibawah Ini :)          ")
    print("1. Diare                                         ")
    print("2. Sakit Kepala                                  ")
    print("3. Tidak Ada                                     ")
    keluhan2       = input("Apakah Ada Keluhan Lain Yang Dialami                                 : ")
    
    if keluhan2 == "1" :
        tipess() 
    elif keluhan2 == "2" :
        tipess1()
    elif keluhan2 == "3" :
        demam_tinggi()
    else :
        print('''
                "Pilihan Tidak Sesuai! 
                Masukkan Pilihan Sesuai Ketentuan"
             ''')
        tipes()

def demam_tinggi() :
    global konsul
    usia          = input("Kategori Umur (anak-anak/ remaja/ dewasa)                            : ")
    if usia == "anak-anak" :
        print("             SILAHKAN MEMBELI HUFAGRIPP ATAU TERMOREX            ")
        print("                         LEKAS SEMBUH YA                         ")
        print("       BILA ADA KELUHAN LANJUTAN LANGSUNG HUBUNGI DOKTER         ")
        time.sleep(5)
    elif usia == "remaja" or usia == "dewasa" : 
        print("                   SILAHKAN MEMBELI PARACETAMOL                  ")
        print("                         LEKAS SEMBUH YA                         ")
        print("       BILA ADA KELUHAN LANJUTAN LANGSUNG HUBUNGI DOKTER         ")
        time.sleep(5)
    else :
        print('''
                "Pilihan Tidak Sesuai! 
                Masukkan Pilihan Sesuai Ketentuan"
             ''')
        time.sleep(2)
        demam_tinggi()

    tanggal()
    konsul[indexUser].append("Demam Tinggi")
    tulisData()
    main_menu()

def tipess() :
    clean()
    print("Silahkan Membaca Keluhan Dibawah Ini :)          ")
    print("1. Sakit Kepala                                  ")
    print("2. Tidak Ada                                     ")
    keluhan3      = input("Apakah Ada Keluhan Lain Yang Dialami                                 : ")
    if keluhan3 == "1" :
        infeksi()
    elif keluhan3 == "2" :
        tipess1()
    else :
        print('''
                "Pilihan Tidak Sesuai! 
                Masukkan Pilihan Sesuai Ketentuan"
             ''')
        time.sleep(2)
        tipess()

def infeksi () :
    global konsul
    usia          = input("Kategori Umur (anak-anak/ remaja/ dewasa)                            : ")
    if usia == "anak-anak" :
        print("                          SILAHKAN MEMBELI ANTIBIOTIK                         ")
        print("                                LEKAS SEMBUH YA                               ")
        print("               BILA ADA KELUHAN LANJUTAN LANGSUNG HUBUNGI DOKTER              ")
        time.sleep(5)
    elif usia == "remaja" or usia == "dewasa" :
        print("                          SILAHKAN MEMBELI ANTIBIOTIK                         ")
        print("                               LEKAS SEMBUH YA                                ")
        print("                BILA ADA KELUHAN LANJUTAN LANGSUNG HUBUNGI DOKTER             ")
        time.sleep(5)
    else :
        print('''
                "Pilihan Tidak Sesuai! 
                Masukkan Pilihan Sesuai Ketentuan"
             ''')
        time.sleep(2)
        infeksi()
    
    tanggal()
    konsul[indexUser].append("Infeksi")
    tulisData()
    main_menu()

def tipess1() :
    global konsul
    usia          = input("Kategori Umur (anak-anak/ remaja/ dewasa)                            : ")
    if usia == "anak-anak" :
        print("             SILAHKAN MEMBELI PARACETAMOL ATAU IBUPROFEN                ")
        print("                          LEKAS SEMBUH YA                               ")
        print("          BILA ADA KELUHAN LANJUTAN LANGSUNG HUBUNGI DOKTER             ")
        time.sleep(5)
    elif usia == "remaja" or usia == "dewasa" :
        print("                     SILAHKAN MEMBELI AMOXILIN                   ")
        print("                          LEKAS SEMBUH YA                        ")
        print("         BILA ADA KELUHAN LANJUTAN LANGSUNG HUBUNGI DOKTER       ")
        time.sleep(5)
    else :
        print('''
                "Pilihan Tidak Sesuai! 
                Masukkan Pilihan Sesuai Ketentuan"
             ''')
        time.sleep(2)
        tipes()

    tanggal()
    konsul[indexUser].append("Tipes")
    tulisData()
    main_menu()

def diare() :
    global konsul
    clean()
    usia          = input("Kategori Umur (anak-anak/ remaja/ dewasa)                            : ")
    if usia == "anak-anak" : 
        print("                             SILAHKAN MEMBELI ORALIT                          ")
        print("                                LEKAS SEMBUH YA                               ")
        print("                BILA ADA KELUHAN LANJUTAN LANGSUNG HUBUNGI DOKTER             ")
        time.sleep(5)
    elif usia == "remaja" or usia == "dewasa" :
        print("                         SILAHKAN MEMBELI LOPERAMIDE                          ")
        print("                               LEKAS SEMBUH YA                                ")
        print("                BILA ADA KELUHAN LANJUTAN LANGSUNG HUBUNGI DOKTER             ")
        time.sleep(5)
    else :
        print('''
                "Pilihan Tidak Sesuai! 
                Masukkan Pilihan Sesuai Ketentuan"
             ''')
        time.sleep(2)
        diare()
    
    tanggal()
    konsul[indexUser].append("Diare")
    tulisData()
    main_menu()

def sakit_kepala () :
    global konsul
    clean()
    usia          = input("Kategori Umur (anak-anak/ remaja/ dewasa)                            : ")
    if usia == "anak-anak" :
        print("                            SILAHKAN MEMBELI BODREXIN                         ")
        print("                                LEKAS SEMBUH YA                               ")
        print("               BILA ADA KELUHAN LANJUTAN LANGSUNG HUBUNGI DOKTER              ")
        time.sleep(5)
    elif usia == "remaja" or usia == "dewasa" :
        print("                      SILAHKAN MEMBELI BODREX ATAU OSKADON                    ")
        print("                               LEKAS SEMBUH YA                                ")
        print("                BILA ADA KELUHAN LANJUTAN LANGSUNG HUBUNGI DOKTER             ")
        time.sleep(5)
    else :
        print('''
                "Pilihan Tidak Sesuai! 
                Masukkan Pilihan Sesuai Ketentuan"
             ''')
        time.sleep(2)
        sakit_kepala()
    
    tanggal()
    konsul[indexUser].append("Sakit Kepala")
    tulisData()
    main_menu()

def diaree() :
    clean()
    print("Silahkan Membaca Keluhan Dibawah Ini :)          ")
    print("1. Sakit Perut                                   ")
    print("2. Mual Dan Muntah                               ")
    print("3. Tidak Ada                                     ")
    keluhan4      = input("Apakah Ada Keluhan Lain Yang Dialami                                 : ")
    if keluhan4 == "1" :
        diare()
    elif keluhan4 == "2" :
        diare()
    elif keluhan4 == "3" :
        diare()
    else :
        print('''
                "Pilihan Tidak Sesuai! 
                Masukkan Pilihan Sesuai Ketentuan"
             ''')
        time.sleep(2)
        diaree()

def mual_muntah () :
    clean ()
    print("Silahkan Membaca Keluhan Dibawah Ini :)          ")
    print("1. Fases Lembek Dan Cair                         ")
    print("2. Kram Perut                                    ")
    print("3. Tidak Ada                                     ")
    keluhan5      = input("Apakah Ada Keluhan Lain Yang Dialami                                 : ")
    if keluhan5 == "1" :
        diare()
    elif keluhan5 == "2" :
        diare()
    elif keluhan5 == "3" :
        masuk_angin()
    else :
        print('''
                "Pilihan Tidak Sesuai! 
                Masukkan Pilihan Sesuai Ketentuan"
             ''')
        time.sleep(2)
        mual_muntah()

def masuk_angin() :
    global konsul
    usia          = input("Kategori Umur (anak-anak/ remaja/ dewasa)                            : ")
    if usia == "anak-anak" : 
        print("                        SILAHKAN MEMBELI MINYAK TELON                         ")
        print("                                LEKAS SEMBUH YA                               ")
        print("                BILA ADA KELUHAN LANJUTAN LANGSUNG HUBUNGI DOKTER             ")
        time.sleep(5)
    elif usia == "remaja" or usia == "dewasa" :
        print("                   SILAHKAN MEMBELI TOLAK ANGIN ATAU ANTANGIN                 ")
        print("                               LEKAS SEMBUH YA                                ")
        print("                BILA ADA KELUHAN LANJUTAN LANGSUNG HUBUNGI DOKTER             ")
        time.sleep(5)
    else :
        print('''
                "Pilihan Tidak Sesuai! 
                Masukkan Pilihan Sesuai Ketentuan"
             ''')
        time.sleep(2)
        masuk_angin()
    
    tanggal()
    konsul[indexUser].append("Masuk Angin")
    tulisData()
    main_menu()
    
def radang_tenggorokan () :
    global konsul
    clean()
    usia          = input("Kategori Umur (anak-anak/ remaja/ dewasa)                            : ")
    if usia == "anak-anak" : 
        print("                        SILAHKAN MEMBELI COOLING 5 SPRAY                      ")
        print("                                LEKAS SEMBUH YA                               ")
        print("                BILA ADA KELUHAN LANJUTAN LANGSUNG HUBUNGI DOKTER             ")
        time.sleep(5)
    elif usia == "remaja" or usia == "dewasa" :
        print("                    SILAHKAN MEMBELI DIGEROL ATAU STREPSIL                    ")
        print("                               LEKAS SEMBUH YA                                ")
        print("                BILA ADA KELUHAN LANJUTAN LANGSUNG HUBUNGI DOKTER             ")
        time.sleep(5)
    else :
        print('''
                "Pilihan Tidak Sesuai! 
                Masukkan Pilihan Sesuai Ketentuan"
             ''')
        time.sleep(2)
        radang_tenggorokan()
    
    tanggal()
    konsul[indexUser].append("Radang Tenggorokan")
    tulisData()
    main_menu()

#BIAYA KONSULTASI------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def biaya_konsultasi () :
    clean ()
    harga_konsul1 = 100000
    harga1 = "KONSULTASI 1X SEBESAR"
    print (str(harga1), "RP.",harga_konsul1)
    print ("TERSEDIA PEMBAYARAN GOPAY, SHOPEEPAY, DANA, DAN OVO -------> 081234567890")
    time.sleep(5)
    main_menu()

#STRUK PEMBAYARAN-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def struk_pembayaran (): 
    clean ()
    bacaData()
    harga_konsul1= 100000
    hargaa1 = "Konsultasi 1x"
    total = harga_konsul1 * len(data['konsul'][indexUser])
    print (">>> STRUK PEMBAYARAN, HARAP DIBAYAR DILARANG HUTANG <<<")
    print ("="*20)
    print (hargaa1,"=",harga_konsul1)
    print ("TOTAL         =",total)
    print ("Biaya anda konsultasi sebesar Rp.",total)
    print ("="*20)
    print ("><><>< TERIMAKSIH TELAH MENGGUNAKAN JASA KITA ><><><")
    time.sleep(5)
    main_menu()

#DATA KONSULTASI----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def data_konsultasi():
    clean()

    bacaData()

    print('-'*50) 
    print(f"|\tNama \t    Keluhan \t    Waktu \t|")
    print("-"*50) 
    for i in data:
        for j in range(0, len(data['konsul'][indexUser])):
            print(f"|\t{data['username'][indexUser]} \t {data['konsul'][indexUser][j]} \t {data['waktu'][indexUser][j]}\t|")
        break

    print("")
    input("Tekan enter untuk kembali ke menu...")
    main_menu()

#REPORT DATA----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def report_data():
    clean()
    bacaData()

    print(" ~~ WELLCOME TO HELLODOC ~~")
    print(" ~~ Report Data Pengguna ~~")
    print("")

    for i in data:
        for j in range(len(data['username'])):
            print(f" {j+1}. {data['username'][j]} Konsultasi Sebanyak {len(data['konsul'][j])} Kali, Yaitu {data['konsul'][j]} Pada {data['waktu'][j]}")
        break

    print("")
    input("Tekan Enter Untuk Kembali Ke Menu...")
    main_menu() 

#BIAYA JIKA BELUM KONSUL-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def biaya_belumkonsul() :
    clean()
    print (" ~~~ SILAHKAN KONSULTASI TERLEBIH DAHULU ~~~ ")
    time.sleep(3)
    main_menu()

#STRUK JIKA BELUM KONSULTASI-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def struk_belumkonsul() :
    clean ()
    print (" ~~~ SILAHKAN KONSULTASI TERLEBIH DAHULU ~~~ ")
    time.sleep(3)
    main_menu()

if __name__ =='__main__':
    main()