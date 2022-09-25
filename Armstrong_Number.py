#(sayı kaç basamak ise her basamağı o sayının kuvveti ile çarpılır,toplamları aynı sayı ise armstrong)
number = input("Please enter a number: ")
numberOfDigits = len(number)
number = int(number)
digit = 0
armstrong = 0
temporaryNumber = number
while temporaryNumber > 0:
    digi = temporaryNumber % 10
    armstrong += digi ** numberOfDigits
    temporaryNumber //= 10
if armstrong == number:
    print("The number is armstrong.")
else:
    print("The number isn't armstrong.")
