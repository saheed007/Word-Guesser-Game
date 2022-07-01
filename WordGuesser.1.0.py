# I am trying to build a word guesser game, something similar to Wordle
import random
print("Welcome to Word Guesser. \nYou have just three tries.\nEnter your guesses accordingly")

trials=1
word_set = ["pan", "man", "sit", "cut", "son", "den", "try", "day"]
word = random.choice(list(word_set))
print(word)

guess=""
while trials <= 5 and word != guess:
    guess=input("Input your guess: ")

    if trials == 1:
        print("First guess: "+ guess )
    if trials == 2:
        print("Second guess: "+ guess )
    if trials == 3:
        print("Third guess: "+ guess )
    if trials == 4:
        print("Fourth guess: "+ guess ) 
    if trials == 5:
        print("Last guess: "+ guess )

    if guess[0] == word[0] and guess[1] != word[1] and guess[2] != word[2]:
        print("You got only the first letter right: " + word[0]+ "--")

    if guess[0] == word[0] and guess[1] == word[1] and guess[2] != word[2]:
        print("You got only the first two letters right: " + word[0]+word[1]+ "-")

    if guess[0] == word[0] and guess[1] != word[1] and guess[2] == word[2]:
        print("You got only two letters right: " + word[0]+ "-"+word[2])

    if guess[0] != word[0] and guess[1] == word[1] and guess[2] != word[2]:
        print("You got only the middle letter right: -" + word[1]+ "-")
            
    if guess[0] != word[0] and guess[1] == word[1] and guess[2] == word[2]:
        print("You got only the last two letters right: -" + word[1] + word[2])

    if guess[0] != word[0] and guess[1] != word[1] and guess[2] == word[2]:
        print("You got only the last letter right: --" + word[2])

    if guess[0] != word[0] and guess[1] != word[1] and guess[2] != word[2]:
        print("You did not get any letter right: ---")        

    if word[:] == guess[:]:
        print("Correct!!!. You got all the letters right: "+word[0]+word[1]+word[2])
        break
    trials += 1
else:
    print("Oh, sorry, you lost. Try again")
