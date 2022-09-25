def isPrime(number):
    if (number == 1 or number == 0):
        return False

    elif (number == 2):
        return True

    else:
        for i in range(2,number):
            if number % i == 0:
                return False
        return True

while True:
    number = input("Please enter a number: ")

    if number == "q":
        break

    else:
        number = int(number)

        if(isPrime(number)):
            print(number,"is prime.")
        else:
            print(number,"isn't prime.")