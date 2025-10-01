import random

word_list = ["mosiah", "banana", "afro", "byui", "wrong", "tacocat", "lofi"]
number_guesses = 0
guess = "0"

print("\nWelcome To The Guessing Game. \n")

game_staus = "YES"




#main game loop
while game_staus == "YES":
    word = random.choice(word_list)
    hint = ["_" for _ in word]


    while True:
        
        print(f"Hint: {' '.join(hint)}")

        guess = input("\n What is your guess?: ").lower()
        number_guesses += 1

        for i, letter in enumerate(guess):
            if letter == word[i]:
                hint[i] = letter.upper()
            elif letter in word:
                hint[i] = letter.lower()
            else:
                hint[i] = "_"
            

        if len(guess) != len(word):
            print("\n Sorry, that was the incorrect number of letters")
            continue

        if guess == word:
            print("Correct!")
            print(f"It took you {number_guesses} guesses.")
            game_staus = input(f"\n Would you like to play agian?  YES/NO ").upper
            break

else:
    print("Goodbye")