while True:
    number = input("enter in #")
    if number.isnumeric():
        number = float(number)
        break
    print("That's not a number")

while True:
    number = input("enter in LOOK")
    if number == "Look":
        continue
    else:
        print("Sam")
        break

print("NUmber")