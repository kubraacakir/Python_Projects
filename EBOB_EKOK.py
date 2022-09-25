def ebob(a,b):
    if a > b:
        min = b
    else:
        min = a

    while a % min != 0 or b % min != 0:
        min -= 1

    return min

a = int(input("Please enter first number: "))
b = int(input("Please enter second number: "))
print("Ebob: ",ebob(a,b))

#3
def ekok_bulma(a,b):
    n = 2
    ekok = 1
    while True:
        if a % n == 0 and b % n == 0:
            ekok *= n
            a = a // n
            b = b // n
        elif a % n == 0 and b % n != 0:
            ekok *= n
            a = a // n
        elif a % n != 0 and b %n == 0:
            ekok *= n
            b = b // n
        else:
            n += 1
        if a == 1 and b == 1:
            break
    return ekok
print("Ekok:",ekok_bulma(a,b))






