#my first python program :D
import random
number=random.randint(0,20)
print('NUMBER GAME')
print('-----------------------')
print('Guess the number(Hint:- It is between 0 and 20')
while True:
    user_input=int(input('Your number?: '))
    if(user_input>number):
        print('Too high!')
    elif(user_input<number):
        print('Too low!')
    else:
        print('You are right!')
        break    
