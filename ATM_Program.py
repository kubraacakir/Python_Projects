print("""
Bakiyeniz 1000 TL'dir.

İşlemler;
1-Bakiye Sorgulama
2-Para Yatırma
3-Para Çekme

Programdan çıkmak için q'ya basınız.
""")

balance = 1000

while True:
    query = input("İşlemi seçiniz: ")

    if query == "q":
        print("Yine bekleriz...")
        break

    elif query == "1":
        print("Bakiyeniz: {} tl'dir.".format(balance))

    elif query == "2":
        amount = int(input("Miktarı giriniz: "))
        balance += amount

    elif query == "3":
        amount = int(input("Miktarı giriniz: "))

        if amount > balance:
            print("Böyle bir miktar çekemezsiniz.")
            continue

        balance -= amount

    else:
        print("Geçersiz işlem...")