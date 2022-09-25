number = int(input("Please enter a number: "))
sum = 0
for i in range(1,number):
    if number % i != 0:
        continue
    elif number % i == 0:
        sum += i
        i += 1
print("Sum:",sum)
if sum == number:
    print("The number is perfect.")
else:
    print("The number isn't perfect.")