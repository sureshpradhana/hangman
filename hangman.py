import random
from words import words

word = random.choice(words)
while '_' in word or '-' in word or ' ' in word:
    word = random.choice(words)
print(word)

lives =6
word_letters=set(word)
used_letters=set()

while len(word_letters)>0 and lives>0:
    userInput =str(input("enter the word: "))
    used_letters.add(userInput)
    if userInput in word:
        checker=[letter if letter in used_letters else '-' for letter in word]
        print(checker)
    else:
        lives=lives-1
        print(f"left lives {lives} and {userInput} is not in word")

if lives==0:
    print(" you are dead ")
else :
    print (" you won ")


    



