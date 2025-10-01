import random

m_number = random.randint(1,10)
guess_count = 0
#m_number = int(input("What is the magic number? "))

while True:
    guess = int(input("What is your guess?  1-100: "))
    guess_count = guess_count + 1
    if m_number > guess:
        print("Higher")
    elif m_number < guess:
        print("Lower")
    elif m_number == guess:
        print("Correct!")
        print(f"It took you {guess_count} guesses")
        break

