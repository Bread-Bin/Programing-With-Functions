import time

print("Text Adventure - Huanted Crypts")
print(" ")
time.sleep(1.5)

waking_up = ("You wake to find yourself in a small dimly lit room.")
stone_cell_look = ("The cold stone walls are all bare except for a single wooden door.")
hallway_1 = ("You open the door to find a long dark hallway with a single orange light at the far end.")
hallway_1_mid = ("As you walk down the hallway, the light at the ends seems to get further and further away. As you continue to follow it you find a large hole in the side of the wall. You can hear the sound of wind from the hole, but you can not see exactly where it goes.")
hide_cell = ("Not wanting to enter the unknow, you stay in your cell waiting. Without food or water you do not last long and die alone in the dark.")

#path 1
    #Light
follow_light = print('''You follow the mysterious ornage light until it seems to disapear from view.
You find yourself at a fork in the path.
To your left you see ''')

#path 2
    #Hole
climb_in_hole = print(" ")


while True:
    print(waking_up)
    print(" ")
    command = input("Actions: LOOK : ").lower()

    if command == "look":
        print(" ")
        print(stone_cell_look)
        print(" ")
        command_1 = input("Actions: OPEN : ").lower()
        if command_1 == "open":
            print(" ")
            print(hallway_1)
            print(" ")
            command_1_1 = input("Actions: WALK, HIDE : ").lower()
            if command_1_1 == "walk":
                print(" ")
                print(hallway_1_mid)
                command_2 = input("Actions: WALK, HOLE : ").lower()
                if command_2 == "walk":
                    print(" ")
                    print()
            elif command_1_1 == "hide":
                print(" ")
                print(hide_cell)
    else:
        print("I do not understand. PLEASE RESTART")
        False