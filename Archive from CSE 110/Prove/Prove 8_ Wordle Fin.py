word = "mosiah"
number_guesses = 0
guess = "0"

print("Welcome to the guessing game.")
print(" ")

game_staus = "yes"

while game_staus == "yes":

    hint = ["_"  for _ in word]

    while guess != word:

        print("Hint: ", end="")
        for i in range(len(word)):
            print("_", end="")
        print("")
        print(" ")
        guess = input("What is your guess?: ").lower()
        number_guesses += 1



        for i, letter in enumerate(guess):
            try:
                if letter == word[i]:
                    hint[i] = letter.upper()
                elif letter in word:
                    hint[i] = letter.lower()
            except IndexError:
                break
        

        for i, letter in enumerate(guess):
            if letter == word[i]:
                print(letter.upper(), end="")
            else:
                print(letter.lower(), end="")

        if guess == word:
            print("Correct!")
            print(f"It took you {number_guesses} guesses.")
            break
        
        elif len(guess) != len(word):
            print("Sorry, that was the incorrect number of letters")
            print("Please try agian")
            print(" ")
            continue




