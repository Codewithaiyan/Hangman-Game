import random

from hangman_words import word_list;
from hangman_art import stages, logo;

print("Welcome to Hangman Game")

lives = 6
print(logo)

choosen_word = random.choice(word_list)

placeholder = " "

word_length = len(choosen_word)
for position in range(word_length):
  placeholder += "_"
print(placeholder)

game_over = False
correct_list = []

while game_over != True:

  print(f"**********{lives}/6 Lives left**********")

  guess = input("guess a letter : ").lower()
  
  if guess in correct_list:
    print(f"you already guessed {guess}")

  display = ""

  for letter in choosen_word:
      if letter == guess:
        display += letter
        correct_list.append(guess)
      elif letter in correct_list:
        display += letter
      else:
        display += "_"

  print("word to guess: " + display)

  if guess not in choosen_word:
    lives -= 1
    print(f"you guessed {guess}, that's not in the word. you have {lives} lives left")

    if lives == 0:
      game_over = True
      print(f"**********IT WAS {choosen_word} YOU LOSE !**********")


  if "_" not in display:
    game_over = True
    print("**********YOU WIN !**********")

  print(stages[lives])