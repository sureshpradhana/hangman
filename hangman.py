import random
from words import words

word = random.choice(words)
while '_' in word or '-' in word or ' ' in word:
    word = random.choice(words)
print(word)

lives = 6
word_letters = set(word)
used_letters = set()

while len(word_letters) > 0 and lives > 0:
    userInput = str(input("enter the word: "))
    if userInput in used_letters:
        print("already used this letter")
        checker = [letter if letter in used_letters else '-' for letter in word]
        print(' '.join(checker))
    elif userInput in word:
        used_letters.add(userInput)
        print(f"left lives {lives} and {userInput} is in word")
        checker = [letter if letter in used_letters else '-' for letter in word]
        if userInput in word_letters:
            word_letters.remove(userInput)
            print(' '.join(checker))
    else:
        lives = lives-1
        print(f"left lives {lives} and {userInput} is not in word")

if lives == 0:
    print(" you are dead ")
else:
    print(" you won ")
