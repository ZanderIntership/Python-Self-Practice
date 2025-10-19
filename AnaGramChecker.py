wordA = input("Input word A : ")
wordB = input("Input word B : ")
Counter = 0


for  J in range (len(wordA)):
    for I in range (len(wordB)):
        if wordA[I] == wordB[J]:
            Counter += 1
            break

if Counter == len(wordA):
    print("These two words have the same letters")
else:
    print("These two words have different letters")

print(Counter)
