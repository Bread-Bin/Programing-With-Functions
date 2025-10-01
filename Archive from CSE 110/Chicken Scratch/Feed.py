#for i in range(11):
    #print(2 ** i)

#for letter in "Hello World":
    #print(letter)

message = "Hello World"

#print(message[4])
#print(message[3:8])
#print(message[3:-2])
#print(message[:-2])

#len = length
for i in range(len(message)):
    print(f'{i:>2}. {message[i]}')

#same thing, slightly difrrent way to go about it
for i, letter in enumerate(message):
    print(f'{i:>2}. {letter}')


# +=  smashes the value of X with a new value of X
# so its like CheeseBall
# Cheese + Ball

