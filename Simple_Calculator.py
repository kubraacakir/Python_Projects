print("""************************
Hesap Makinesi Programı
İşlemler
1-Toplama işlemi
2-Çıkarma işlemi
3-Çarpma İşlemi
4-Bölme İşlemi
************************
""")
a = int(input("Please enter a number: "))
b = int(input("Please enter a number: "))
operation = input("Please choose a operation: ")
if operation == "1":
    print("{}+{}={}".format(a,b,a+b))
elif operation == "2":
    print("{}-{}={}".format(a,b,a-b))
elif operation == "3":
    print("{}x{}={}".format(a,b,a*b))
elif operation == "4":
    print("{}/{}={}".format(a,b,a/b))
else:
    print("Geçersiz işlem....")
