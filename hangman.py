import random
from words import words

word = random.choice(words)
while '_' in word or '-' in word or ' ' in word:
    word = random.choice(words)
if len(word) >6 and len(word)<10:
   lives = 8
else:
    lives=6
word_letters = set(word)
used_letters = set()

while len(word_letters) > 0 and lives > 0:
    #used letters
    print("The words you have used are: ",' '.join(used_letters))
    print()
    #guess the word
    userInput = str(input("Guess the word: "))
    #check if used this letter before
    if userInput in used_letters:
        print("you have used this letter")
        checker = [letter if letter in used_letters else '-' for letter in word]
        print("The words you have used are: ",' '.join(checker))
        print("")
    #if userinput in word
    elif userInput in word:
        used_letters.add(userInput)
        print(f"left lives {lives} and {userInput} is in word")
        checker = [letter if letter in used_letters else '-' for letter in word]
        if userInput in word_letters:
            word_letters.remove(userInput)
            print(' '.join(checker))
    #if user input not in word
    else:
        used_letters.add(userInput)
        lives = lives-1
        print(f"left lives {lives} and {userInput} is not in word")

if lives == 0:
    print(f" you are dead , word is {word}")
else:
    print(f" you won ,word was {word}")
