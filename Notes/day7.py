import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["jon", "Jonathan", "JonJon"]
lives = 6

#randomly picking a word
word = random.choice(word_list)
letter_list = []
for blank in word:
    letter_list += '_'

print(letter_list)
#User input
end_game = False
while not end_game:
    guess = input("guess a letter? ")
    #letter check
    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            letter_list[position] = letter
    print(letter_list)
    if guess not in word:
        lives -= 1
        if lives == 0:
            print("YOU LOSE")
        print(letter_list)
    if "_" not in letter_list:
        end_game = True
        print("YOU WIN")
    
    print(stages[lives])