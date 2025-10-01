#How to access or refrence other files in your code. (aka. how to avoid 1,700 lines of code)
#open("How to Note in Python.txt")
#open("feed.py")

#file = open("Example.txt") #standard way to open file

with open("Example.txt") as file: #better way to open files that will close the file after the with block is finished running.
    #for loop action stuff here

#print(next(file))

    for line in file:
        print(line.strip()) #.strip() removes the extra gaps between lines that come from reading the text file.
                            #can also be used to remove characters frim a string .string(character)
                            #.lstrip & .rstrip to only remove left or right selected characters


#print(line.strip().split(",")) allows you to split parts of a line by chopping it up by a certin caracter ie: ,  in this case
#strip before split

