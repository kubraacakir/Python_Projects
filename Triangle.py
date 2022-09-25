
first = int(input("Please enter first edge: "))
second = int(input("Please enter second edge: "))
third = int(input("Please enter third edge: "))

if first is second is third:
    print('Equilateral Triangle')
elif first is second != third or first is third != second or second is third != first:
    print('Isosceles Triangle')
else:
    print('Scalene Triangle')




