###Imports###
from random import randint,choice
###Variables###
yes_answers =['Yes','More than likely','Chances are in your favor']
no_answers = ['No', 'Not likely', 'Not a chance',
              'Chances are not in your favor']

###Main Program###
while True:
    name = input('\nWhat is your name?:\n')
    input('Hello %s, what is your question?:\n' % name.title())
    random = randint(1,2)
    if random == 1:
        print(choice(yes_answers))
        
    elif random == 2:
        print(choice(no_answers))
