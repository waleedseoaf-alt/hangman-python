ascii_art=[r'''+---+
  |   |
      |
      |
      |
      |
=========''', r'''+---+
  |   |
  O   |
      |
      |
      |
=========''', r'''+---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''+---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''+---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''+---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

import random
import string

words_list=['good', 'nice', 'car', 'new']

attempts=0
previous_attempts=[]

random_word=random.choice(words_list)

number_of_letters=["_"]*len(random_word)

print(f'{" ".join(number_of_letters)}\n')

print(ascii_art[0])

while '_' in number_of_letters and attempts<6:
	
	user_guess=input('peleas guess a letter\n').lower()
	
	
	if user_guess not in string.ascii_lowercase:
		continue
	elif user_guess in previous_attempts:
		print('you have already guessed the letter. try again')
		continue
	elif user_guess in random_word:
		for position in range(len(random_word)):
			if random_word[position]==user_guess:
				number_of_letters[position]=user_guess
		print (f'you have {6 - attempts} more tries')
		print(' '.join(number_of_letters))
		previous_attempts.append(user_guess)
	else:
		attempts+=1
		previous_attempts.append(user_guess)
		print(ascii_art[attempts])
		print (f'you have {6 - attempts} more tries')	
# النتيجة
if '_' not in number_of_letters:
	print ('''
	*************
	YOU WIN
	*************''')
else:
	print('you lose')	
	
