word = "mosiah"
number_geusses = 0

print("Welcome to the geussing game.")

for letter in word:
    print(" ")
    guess = input("What is your guess?: ")
    if letter.lower() != guess:
        print("_", end ="")
    else:
        print(letter.lower(), end="")



#while True:
    #print(" ")
    #print("Hint: _ _ _ _ _ _")
    #guess = input("What is your guess?: ").lower()
    #number_geusses += 1
    
   # if guess == secret:
   #     print(" ")
   #     print("Congratulations! You guessed it!")
   #     print(f"Number of guesses: {number_geusses}")
   #     break

   # elif guess != secret:
    # print("Your guess was not correct.")


