import random
tries = 6
hang =  ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
print(""" welcome to hangman game """)
print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
guessed_letter =[]
list = ["office","good","bad"]
chosenword = random.choice(list)

theword= []

for x in chosenword:
    theword.append("_")
print("".join(theword))

while "_" in theword and tries >0:
    letter= input("Enter your letter:")
    

    if letter in guessed_letter:
        print("you have entered this letter before")
        print(f"you have {tries} left")
        continue
    guessed_letter.append(letter)
    if letter not in chosenword:
              tries -= 1
              print(hang[6-tries])
    else:

      for n in range(len(chosenword)):
            if chosenword[n] == letter:
              theword[n] = letter
    print(" ".join(theword))
    print(f"you have {tries} left")
            
if tries ==0 :
  print("""you lose'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''' """)
else:
  print("you winnnnnnnnn")

