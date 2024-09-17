#logika
username = input ("Masukkan Username: ")


if username == 'gaz':
    password = int(input ("Masukkan Password: "))
    if password == 123:
        print("Selamat datang")
    else:
        print("Password salah")
else:
    print("Username tidak terdaftar")
