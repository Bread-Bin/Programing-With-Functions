import math


list = []
number = -1

while number != 0:
    number = int(input("enter a number: "))

    if number != 0:
        list.append(number)



print(f"\nSum: {sum(list)}")
print(f"Average: {sum(list) / len(list)}")

print(f"Smallest Value: {min(i for i in (list) if i >0)}")
print(f"Largest Vaulue: {max(list)}")

print(f"Your list is: {list}")
print(f"Sorted List: {sorted(list)}") 