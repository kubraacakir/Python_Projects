import random
import time
print("""****************************************
Sayı Tahmin Oyunu

10 ile 50 arasındaki sayıyı tahmin edin.
****************************************
""")
random_number = random.randint(10,50)
guessRight= 7
while True:
    guess = int(input("Tahmininiz:"))
    if guess < random_number:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha yüksek bir sayı söyleyiniz.")
        guessRight -= 1
    elif guess > random_number:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha düşük bir sayı söyleyiniz.")
        guessRight -= 1
    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler!Sayınız:",random_number)
        break
    if guessRight == 0:
        print("Tahmin hakkınız bitti.")
        print("Sayı:",random_number)
        break