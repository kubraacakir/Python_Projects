print("""
******************
Kullanıcı Girisi
******************
""")
sys_user_name = "kkubra"
sys_password = "12345"
right_of_entry = 3

while True:
    user_name = input("Kullanıcı Adı: ")
    password = input("Parola: ")
    if user_name != sys_user_name and password == sys_password:
        print("Hatalı kullanıcı adı girişi.")
        right_of_entry -= 1
    elif user_name == sys_user_name and password != sys_password:
        print("Hatalı parola girişi.")
        right_of_entry -= 1
    elif user_name != sys_user_name and password!= sys_password:
        print("Hatalı kullanıcı adı ve parola girişi.")
        right_of_entry -= 1
    else:
        print("Başarılı giriş.Hoşgeldiniz.")
        break
    if right_of_entry == 0:
        print("Giriş hakkınız bitti...")
        break