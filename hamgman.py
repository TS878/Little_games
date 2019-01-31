###Imports###
import random
###variables###
hangman_pics = ['''
+---+
        |
        |
        |
    ===''', '''
    +---+
    O   |
    |
    |
    ===''', '''
+---+
O   |
|   |
    |
    ===''', '''
+---+
O   |
/|   |
    |
    ===''', '''
+---+
O   |
/|\  |
    |
    ===''', '''
+---+
O   |
/|\  |
/    |
    ===''', '''
+---+
O   |
/|\  |
/ \  |
      ===''']

words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''.split()

###Functions###
def get_random_word(word_list):
    # This function returns a random string from the passed list of strings.
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]

def display_board(missed_letters, correct_letters, secret_word):
    print(hangman_pics[len(missed_letters)])
    print()
    
    print("Missed letters:", end=' ')
    for letter in missed_letters:
        print(letter,end=' ')
        print()
        
    blanks = '_' * len(secret_word)
    for i in range(len(secret_word)):
    #replace blanks with correctly guessed letters
        
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]
            
    for letter in blanks:
        print(letter, end=' ')
        print()
                
def get_guess(already_guessed):
    #returns the letter the player entered. makes sure the play enters a letter
    while True:
        guess = input("Guess a letter:\n")
        guess = guess.lower()
        
        if len(guess) != 1:
            print('Please type in a single letter')
        elif guess in already_guessed:
            print("You already guessed that letter. choose again.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':		
            print('Please enter a LETTER.')		
        else:		
            return guess

def play_again():
    # This function returns true if the player wants to play again otherwise it
    ## returns false
    print("Do you want to play again? (Yes or NO)")
    return input().lower().startswith('y')
    
###Main Program###
print('H A N G M A N')
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words)
game_is_done = False

while True:
    display_board(missed_letters, correct_letters, secret_word)
    guess = get_guess(missed_letters + correct_letters)
   
    if guess in secret_word:
        correct_letters = correct_letters + guess
    
    # Check if the player has won
    found_all_letters = True
    for i in range(len(secret_word)):
        if secret_word[i] not in correct_letters:
            found_all_letters = False
            break
    if found_all_letters:
        print("Yes the secret word is %s! You have Won" % secret_word)
        game_is_done = True
    else:
        missed_letters = missed_letters + guess
        
        #check if player has guessed to many times and lost.
        if len(missed_letters) == len(hangman_pics) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            
            print("You have run out of guesses.\nAfter " +
            str(len(missed_letters)) + " missed guesses and " +
            str(len(correct_letters)) + " correct guesses, the word was %s"
            %secret_word)
            game_is_done = True
            
    # Ask the player if they want to play again 
    if game_is_done:		
	        if play_again():		
	            missed_letters = ''		
	            correct_letters = ''		
	            game_is_done = False		
	            secret_Word = get_random_word(words)		
	        else:		
	            break
