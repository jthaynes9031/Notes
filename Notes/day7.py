import random
#Today im looking to combine everything i learned in the past week into one program
#HANGMAN
word_list = ["jon", "Jonathan", "JonJon"]

#randomly picking a word
word = random.choice(word_list)
letter_list = []
for blank in word:
    letter_list += '_'

print(letter_list)
#User input
guess = input("guess a letter? ")
#letter check
for position in range(len(word)):
    letter = word[position]
    if letter == guess:
        letter_list[position] = letter
print(letter_list)
