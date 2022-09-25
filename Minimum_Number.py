number = int(input("Please enter how many numbers to enter: "))
minimum = int(input("Please enter numbers: "))

for a in range(number-1):
    num =int(input("Please enter numbers: "))
    if minimum > num:
        minimum = num

print("The minimum number is",minimum)

