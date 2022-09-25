"""
#111
a = input()
def fonksiyon(sentence):
    s = sentence.split(" ")
    new_sentence = []
    for i in s:
        r = i[len(i)-1]
        if 64 < ord(r) < 91 or 96 < ord(r) < 123:
            new_sentence.append(i)
        else:
            t = i[0:len(i)-1]
            new_sentence.append(t)
    print(new_sentence)
fonksiyon(a)
"""
"""
#
sesli = ["A","E","I","O","U","a","e","i","o","u"]
sessiz = ["B","C","D","F","G","H","J","K","L","M","N","P","R","S","T","V","W","X","Y","Z"]
def latin(str1):
    for i in str1:
        if i[0] in sesli:
            x = str1 + "way"
        else:
            if i[1:len(i) - 1] in sesli:
                
str1 = input()
print(latin(str1))
"""
import random
kelimeler = ["resim" , "battaniye" , "şarkı" , "kardan adam" , "kartopu" , "bilgisayar" , "canlıders" , "kolonya" , "kitap" , "maşa"]
kelime = random.choice(kelimeler)
tahminSayisi = 5
harfler = []
x = len(kelime)
z = list('_' * x)
print(' '.join(z), end='\n')
while tahminSayisi > 0:
    y = input("Bir harf tahmin edin : ")
    if y in harfler:
        print("Lutfen daha once tahmin ettiginiz harfleri tekrar tahmin etmeyin...")
        continue

    elif len(y) > 1:
        print("Lutfen sadece bir harf girin.")
        continue

    elif y not in kelime:
        tahminSayisi -= 1
        print("Yanlış tahmin!.",tahminSayisi,"tane tahmin hakkınız kaldı.")

    else:
        for i in range(len(kelime)):
            if y == kelime[i]:
                print("Doğru Tahmin")
                z[i] = y
                harfler.append(y)
                print(' '.join(z), end='\n')

    cevap = input("Kelimenin tamamını tahmin etmek istiyor musunuz? ['e' veya 'h'] : ")


    if cevap == "e":
        tahmin = input("Kelimenin tamamını tahmin edebilirsiniz : ")
        if tahmin == kelime:
            print("Tebrikler bildiniz...")
            break
        else:
            tahminSayisi -= 1
            print("Yanlış tahmin ettiniz.",tahminSayisi,"tane tahmin hakkınız kaldı.")

    elif cevap != "e" or cevap != "h":
        print("Hatalı giriş.")
        continue

    if tahminSayisi == 0:
        print("Tahmin hakkınız kalmadı. Kaybettiniz! Adam Asıldı.Doğru cevap",kelime,"idi.")
        break

