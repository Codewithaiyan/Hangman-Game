import random
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/         ''')

print("Welcome to Hangman Game")

stages = ['''
    _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
 _|___''','''
    _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |
     |
 _|___''','''
    _______
     |/      |
     |      (_)
     |      \|/
     |
     |
     |
 _|___''','''
    _______
     |/      |
     |      (_)
     |       |
     |
     |
     |
 _|___''','''
    _______
     |/      |
     |      (_)
     |
     |
     |
     |
 _|___''','''
    _______
     |/      |
     |
     |
     |
     |
     |
_|___''']

word_list = ["camel", "horse", "tiger", "aardvark"'abruptly',
'absurd',
'abyss',
'beekeeper',
'bikini',
'blitz',
'blizzard',
'boggle',
'bookworm',
'boxcar',
'boxful',
'buckaroo',
'buffalo',
'buffoon',
'buxom',
'buzzard',
'buzzing',
'buzzwords',
'caliph',
'cobweb',
'cockiness',
'croquet',
'funny',
'gabby',
'galaxy',
'galvanize',
'gazebo',
'giaour',
'gizmo',
'glowworm',
'glyph',
'gnarly',
'gnostic',
'gossip',
'grogginess',
'haiku',
'haphazard',
'hyphen',
'iatrogenic',
'icebox',
'injury',
'ivory',
'ivy',
'jackpot',
'jaundice',
'jawbreaker',
'jaywalk',
'jazziest',
'jazzy',
'jelly',
'jigsaw',
'jinx',
'jiujitsu',
'polka',
'pshaw',
'psyche',
'puppy',
'puzzling',
'quartz',
'queue',
'quips',
'quixotic',
'quiz',
'quizzes',
'quorum',
'razzmatazz',
'rhubarb',
'rhythm',
'rickshaw',
'schnapps',
'scratch',
'shiv',
'snazzy',
'sphinx',
'spritz',
'squawk',
'staff',
'strength',
'strengths',
'stretch',
'stronghold',
'stymied',
'subway',
'swivel',
'syndrome',
'thriftless',
'thumbscrew',
'topaz',
'transcript',
'transgress',
'transplant',
'waltz',
'wave',
'wavy',
'waxy',
'wellspring',
'wheezy',
'whiskey',
'whizzing',
'whomever',
'wimpy',
'witchcraft',
'wizard',
'woozy',
'wristwatch',
'wyvern',
'xylophone',
'yachtsman',
'yippee',
'yoked',
'youthful',
'yummy',
'zephyr',
'zigzag',
'zigzagging',
'zilch',
'zipper',
'zodiac',
'zombie', ]
lives = 6
choosen_word = random.choice(word_list)

placeholder = " "

word_length = len(choosen_word)
for position in range(word_length):
  placeholder += "_"
print(placeholder)

game_over = False
correct_list = []

while game_over != True:
  guess = input("guess a letter : ").lower()
  print(guess)

  display = ""

  for letter in choosen_word:
      if letter == guess:
        display += letter
        correct_list.append(guess)
      elif letter in correct_list:
        display += letter
      else:
        display += "_"

  print(display)

  if guess not in choosen_word:
    lives -= 1
    if lives == 0:
      game_over = True
      print("**********you lose !**********")


  if "_" not in display:
    game_over = True
    print("**********you win !**********")

  print(stages[lives])