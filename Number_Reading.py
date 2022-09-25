birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

def oku(sayi):
    a = sayi % 10
    b = sayi // 10
    c = onlar[int(b)]+" "+birler[int(a)]
    return c
print(oku(int(input())))
