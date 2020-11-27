import random

words = ['apple', 'banana']

word = random.choice(words)
print('Guess the characters: ')

guesses = ''

turns = 12
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failed += 1
    if failed == 0:
        print('You win, good job!')
        print('The word was: ', word)
        exit()
        break
    
    guess = input('Guess a character: ')
    guesses += guess
    if guess not in word:
        turns -= 1
        print('Wrong!')
        print('You have', + turns, 'more guesses.')
        if turns == 0:
            print('You loose, better luck next time!')
            exit()
    
