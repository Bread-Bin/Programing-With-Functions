word = "Commitment".lower()
fav_letter = input("What is Your favorite letter?: ")
print(" ")


#for letter in word:
    #if letter.lower() == fav_letter.lower():
        #print(letter.upper(), end="")
    #else:
        #print(letter.lower(), end="")

print("")

for letter in word:
    if letter.lower() == fav_letter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
print(" ")

for i, letter in enumerate(word):
    print(f"The letter {letter} is at position {i}")