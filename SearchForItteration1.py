

print("How the application works\nEnter a word and the program will scan how many times that word display in the textfile")

SearchFor = input("Enter a word to search for: ")
found = False
doublecheck = False
count = 0
with open("Document.txt","r") as file:
    SpecificDoc = file.read()

for I in range (len(SpecificDoc)):
    if SearchFor[0] == SpecificDoc[I]:
        for J in range (len(SearchFor)):

            if SearchFor[J] == SpecificDoc[I + J]:
                found = True
            else:
                found = False
                break

            if found and SpecificDoc[I + len(SearchFor)] == ' ' or SpecificDoc[I + len(SearchFor)] == ',' or SpecificDoc[I + len(SearchFor)] == '.' or SearchFor[J] == '!' or SearchFor[J] == '?':
                found = True



    if found == True:
        count += 1
        found = False

print(count)
