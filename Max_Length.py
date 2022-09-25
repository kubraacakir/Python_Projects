#Number of letters in the longest word

sentence = input("Please enter a sentence: ")
count = 0
maxLength = 0

for i in range(len(sentence) + 1):
    if i == len(sentence):
        if maxLength < count:
            maxLength = count
    elif sentence[i] == " ":
        if maxLength < count:
            maxLength = count
        count = 0
    else:
        count += 1

print(str(maxLength))
