import time

print('''*******************************************************
This program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you ten statements that you could possibly apply to yourself.
Please rate how much you agree with each of the statements by responding with one of these four letters:

D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.''')

time.sleep(5)
print('''
      Let's begin!
      
      ''')
rosendick = [
    '1. I feel that I am a person of worth, at least on an equal plane with others.',
    '2. I feel that I have a number of good qualities.',
    '3. All in all, I am inclined to feel that I am a failure.',
    '4. I am able to do things as well as most other people.',
    '5. I feel I do not have much to be proud of.',
    '6. I take a positive attitude toward myself.',
    '7. On the whole, I am satisfied with myself.',
    '8. I wish I could have more respect for myself.',
    '9. I certainly feel useless at times.',
    '10. At times I think I am no good at all.'
]

def positive_response(answer):
    if answer == 'D':
        return 0
    elif answer == 'd':
        return 1
    elif answer == 'a':
        return 2
    elif answer == 'A':
        return 3
    
def negative_response(answer):
    if answer == 'D':
        return 3
    elif answer == 'd':
        return 2
    elif answer == 'a':
        return 1
    elif answer == 'A':
        return 0
    
score = 0
for question in rosendick:
    print(question)
    answer = input("Enter D, d, a, or A: ")
    if question in ['1. I feel that I am a person of worth, at least on an equal plane with others.',
                    '2. I feel that I have a number of good qualities.',
                    '4. I am able to do things as well as most other people.',
                    '6. I take a positive attitude toward myself.',
                    '7. On the whole, I am satisfied with myself.']:
        score += positive_response(answer)
    else:
        score += negative_response(answer)

print(f'''Your score is {score}.
A score below 15 may indicate problematic low self-esteem.''')