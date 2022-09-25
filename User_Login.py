print("""
******************
Kullanıcı Girisi
******************
""")
sys_user_name = "kkubra"
sys_password = "12345"
user_name = input("Kullanıcı Adı: ")
password = input("Parola: ")
if (user_name == sys_user_name and password != sys_password):
    print("Hatalı parola girişi.")
elif (user_name != sys_user_name and password != sys_password):
    print("Hatalı kullanıcı adı ve parola girişi.")
elif (user_name != sys_user_name and password == sys_password):
    print("Hatalı kullanıcı adı girişi.")
else:
    print("Sisteme başarılı giriş yapıldı.")

