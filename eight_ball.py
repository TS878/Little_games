###Imports###
import os
from random import randint,choice
###Variables###
magic = '''
                      __       __ 
  /\\  /\\      /\\     /     |  /  \\
 /  \\/  \\    /__\\    | __  |  |   
/        \\  /    \\   \\__/  |  \\__/
                               
'''
eight_ball = '''
  __            
 /  \           ___
|    |         |   \      /\    |    |
 \__/    ___   |___/     /  \   |    |
 /  \          |   \    /____\  |    |
|    |         |___/   /      \ |___ |___
 \__/
 '''
answers = {
'yes':['Yes','More than likely','Chances are in your favor'],
'no':['No', 'Not likely', 'Not a chance',
    'Chances are not in your favor', "I wouldn't do that"]
           }

###Main Program###
while True:
    print(magic + eight_ball)
    name = input('What is your name?:\n')
    
    while True:
        input('Hello %s, what would you like to know?:\n' % name.title())
        random = randint(1,2)
        if random == 1:
            print(choice(answers['yes']))
        
        elif random == 2:
            print(choice(answers['no']))
        
        print('Do you want to ask another question? (yes or no)')
            
        a_new_question = input().lower().startswith('y')
        if a_new_question:
            os.system('clear')
        elif not a_new_question:
            break
