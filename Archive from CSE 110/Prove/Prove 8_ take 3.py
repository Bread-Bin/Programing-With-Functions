import random

word_list = ["mosiah", "banana", "afro", "byui", "wrong", "tacocat", "lofi"]
guess = "0"

print("\nWelcome To The Guessing Game.\n")
print("Try and figure out the word as fast as you can.")

game_status = "yes"

# Main game loop
while game_status == "yes":
    word = random.choice(word_list)
    number_guesses = 0
    hint = ["_" for _ in word]

    while True:
        print(f"Hint: {' '.join(hint)}")

        guess = input("\nWhat is your guess?: ").lower()
        number_guesses += 1

        if len(guess) != len(word):
            print("\nSorry, that was the incorrect number of letters")
            continue

        for i, letter in enumerate(guess):
            if letter == word[i]:
                hint[i] = letter.upper()
            elif letter in word:
                hint[i] = letter.lower()
            else:
                hint[i] = "_"

        if guess == word:
            print("Correct!")
            print(f"It took you {number_guesses} guesses.")
            if number_guesses > 10:
                print("Took you long enough!")
            if number_guesses < 3:
                print("You cheated :(")
            game_status = input(f"\nWould you like to play again? (YES/NO) ").lower()
            break

    if game_status != "yes":
        break

print("Goodbye")