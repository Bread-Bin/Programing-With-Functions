print("Welcome to Waaacky MadLibs 5!")
print(" ")
print("Please enter in the following information for a wacky story")
print("-------------------------------------------------------------")

name1 = input("Name: ")
name2 = input("Name 2: ")
flavor = input("Flavor: ")
food = input("Food: ")
food2 = input("Food 2: ")
adjective = input("Adjective: ")
adjective2 = input("Adjective 2: ")
adjective3 = input("Adjective 3: ")
adjective4 = input("Adjective 4: ")
adjective5 = input("Adjective 5: ")
adjective6 = input("Adjective 6: ")
size = input("Size: ")
size2 = input("Size 2: ")
animal = input("Animal: ")
verb2 = input("Movement (ending w/ ing): ")
exclamation = input("Exclamation: ")
emotion = input("Emotion: ")
print("-------------------------------------------------------------")

print("Your Story is:")
print(" ")

format = f'''One sunny afternoon, {name1} and {name2} decided to visit the local {adjective} ice cream shop.
As they walked inside, the sweet smell of {adjective2} waffle cones and {adjective3} ice cream flavors filled the air.
They eagerly approached the counter and saw a {adjective4} server who greeted them with a {adjective5} smile.

{name1} and {name2} looked at the menu board and saw so many {adjective4} options that it was hard to choose just one.
{name1.title()} decided on a {size} scoop of {flavor}, while {name2} chose a {size2} sundae with {food.lower()} and {food2.lower()}.
They found a table and sat down to eat their treats.

Before they knew it, a {animal} swooped by and stole {name1}'s icecream. {exclamation.title()} shouted {name2}.
They chased the {animal} by {verb2} down the street,
but when they caught the {animal} they found that {name1}'s ice cream was all gone.
{name1.title()} felt {adjective6} and {emotion} that their delicious experience had come to an end.'''

print(format)