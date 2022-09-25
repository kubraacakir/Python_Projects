def integerDivisor(number):
    integerDivisor = []
    for i in range(2,number):
        if number % i == 0:
            integerDivisor.append(i)
    return integerDivisor
while True:
    number = input()
    if number == "q":
        print("Program sonlandırılıyor...")
        print("Program sonlandı.")
        break
    else:
        number = int(number)
        print("Tam bölenler:",integerDivisor(number))
