print("""
**************************
Faktöriyel Bulma Programı

Çıkmak için q ' a basınız.
**************************
""")
while True:
    number = input("Lütfen bir sayı giriniz: ")
    if number == "q":
        print("Program sonlandırılıyor...")
        break
    else:
        number = int(number)
        factorial = 1
        for i in range(2,number + 1):
            factorial *= i
        print("Faktöriyel: ",factorial)