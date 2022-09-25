#ikinci dereceden bir bilinmeyenli denklemin köklerini bulma
#denklem: ax**2 + bx + c
#deltayı hesaplama:  b ** 2 - 4 * a * c
#birinci kök : (-b - delta ** 0.5) / (2 * a)
#ikinci kök : (-b + delta ** 0.5) / (2 * a)

a = int(input("Please enter first edge: "))
b = int(input("Please enter second edge: "))
c = int(input("Please enter third edge: "))
delta = b ** 2 - 4 * a * c
x1 = (-b - delta ** 0.5) / (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)

print("First root: {}\nSecond Root: {}\n".format(x1,x2))