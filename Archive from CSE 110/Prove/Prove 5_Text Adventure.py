import time

print("Story intro")
time.sleep(2)

print(" ")
x = 1

while x == 1:
    print(" ")
    print(f"You wake to find yourself in a small dimly lit room. ")
    command = input("Actions: LOOK : ").lower()

    if command == "look":
        print(" ")
        print("The stone walls are all bare except for a single wooden door")
        command_1 = input("Actions: OPEN : ").lower()
        if command_1 == "open":
            print(" ")
            print("You open the door to find a long dark hallway with a single orange light at the far end.")
            command_1_1 = input("Actions: WALK, HIDE : ").lower()
            if command_1_1 == "walk":
                print(" ")
                print("As you walk down the hallway, the light at the ends seems to get further and further away. As you continue to follow it you find a large hole in the side of the wall. You can hear the sound of wind from the hole, but you can not see exactly where it goes.")
                command_1_1_1 = input("Actions: KEEP WALKING, HOLE : ").lower()
                if command_1_1_1 == "keep walking":
                    print(" ")

                elif command_1_1_1 == "hole":
                    print(" ")

            elif command_1_1 == "hide":
                print(" ")
                print("You do not trust what you can not know. You choose to stay in your little room, waiting out the hours. You do not realize the darkness creeping closser to untill it is too late. That light was the last light you saw as your entire world was engoulfed in to the void.")
                print("YOU DIED")
                x=2
            else:
                print(" ")
                print("I do not understand: PLEASE RESTART")
                X = 2
        else:
            print(" ")
            print("I do not understand: PLEASE RESTART")
            X = 2
    else:
        print(" ")
        print("I do not understand: PLEASE RESTART")
        X = 2

