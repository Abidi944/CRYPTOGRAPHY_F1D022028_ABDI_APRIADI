import bcrypt 

def selamat():
    print("Welcome to the Jungle!")
    
def formRegist(Username=None, Password=None):
    Username = input("Buat Username: ")
    Password1 = input("Buat Password: ")
    Password2 = input("Konfirmasi Password: ")
    db = open("database.txt", 'r')
    z = []
    
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        c = a,b
        z.append(a)
    if not len(Password1)<=8:
        db = open("database.txt", 'r')
        if not Username == None:
            if len (Username) <1:
                print("Mohon masukkan username yang benar")
                formRegist()
            elif Username in z:
                print("Username sudah terdaftar")
                formRegist()
            else:
                if Password1 == Password2:
                    Password1 = Password1.encode('utf-8')
                    Password1 = bcrypt.hashpw(Password1, bcrypt.gensalt())
                    
                    db = open("database.txt", 'a')
                    db.write(Username + "," + str(Password1) + "\n")
                    print("Username dan Password berhasil dibuat")
                else:
                    print("Password tidak sama")
                    formRegist()
                    
    else:
        print("Password terlalu pendek")


def formLogin(Username=None, Password=None):
    Username = input("Masukkan Username: ")
    Password = input("Masukkan Password: ")
    
    if not len(Username or Password) < 1:
        if True:
            db = open("database.txt", 'r')
            z = []
            k = []
            for i in db:
                a,b = i.split(",")
                b = b.strip()
                c = a,b
                z.append(a)
                k.append(b)
                data = dict(zip(z, k))
                
            try:
                if Username in data:
                    hashed = data[Username].strip('b')
                    hashed = hashed.replace("'", "")
                    hashed = hashed.encode('utf-8')
                    
                    try:
                        if bcrypt.checkpw(Password.encode(), hashed):
                            print("Berhasil Login")
                            print("How are you doing ", Username + "?")
                            selamat()
                        else:
                            print("Password Salah!")
                            formLogin()
                    except:
                        print("Masukkan Ulang Username atau Password")
                        formLogin()
                else:
                    print("Username Tidak Dapat Ditemukan")
                    formLogin()
            except:
                print("Username atau Password Belum Terdaftar")
                formRegist()
        else:
            print("Login Error")
    else:
        print("Silahkan Coba Login Kembali")
        formLogin()

def home(option=None):
    print("Welcome! Silahkan Ketik Login atau Daftar untuk Memulai")
    option = input("Login | Daftar: ")
    if option == "Login":
        formLogin()
    elif option =="Daftar":
        formRegist()
    else:
        print("Mohon Ketik Login atau Daftar")
        home()

home()