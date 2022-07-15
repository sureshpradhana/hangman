import random
from words import words

word = random.choice(words)
while '_' in word or '-' in word or ' ' in word:
    word = random.choice(words)
lives = 6
word_letters = set(word)
used_letters = set()

while len(word_letters) > 0 and lives > 0:
    #used letters
    print(' '.join(used_letters))
    #guess the word
    userInput = str(input("Guess the word: "))
    #check if used this letter before
    if userInput in used_letters:
        print("you have used this letter")
        checker = [letter if letter in used_letters else '-' for letter in word]
        print(' '.join(checker))
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
        lives = lives-1
        print(f"left lives {lives} and {userInput} is not in word")

if lives == 0:
    print(" you are dead ")
else:
    print(" you won ")
