#sayı tahmin ettirme programı

import random

num=random.randint(1,100)
des_prediction=int(input('How many guesses do you want? '))
hak=des_prediction
counter=0
while (hak>0):
    hak-=1
    counter+=1
    
    prediction=int(input('Enter your guess: '))
    if num==prediction:
        print(f'Congratulations {counter}. you tried it. Your point is {100-(100/des_prediction)*(counter-1)}. Good Luck.')
        break
    elif num>prediction:
        print('Go up!')
    else:
        print('Go down')

    if hak==0:
        print(f'Your right has expired. Number withheld:{num}.')
    else:
        print()






