import sys
import random


while True:
    try:    
        first_num = sys.argv[1]
        second_num = sys.argv[2]
        answer = random.randint(int(first_num), int(second_num))
    except ValueError:
        print(f'You must input a number, letters are not allowed')
        break
    
    
    try:
        guessed_num = int(input('Guess the correct number: '))
        if 0 < guessed_num <= 10:
            if guessed_num == answer:
                print('Congrats you won!!')
                break
        else: 
            print('hey, 1-10 dude!')
    except ValueError:
        print('please enter a number')
        break
