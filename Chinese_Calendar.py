year = int(input("Please enter a year: "))

calendar = ["Dragon","Snake","Horse",
            "Goat","Monkey","Rooster",
            "Dog","Pig","Rat",
            "Ox","Tiger","Rabbit"]

count = calendar[(year+4)%12]

print(year,":",count)