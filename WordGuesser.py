# I am trying to build a word guesser game, something similar to Wordle
import random
print("Welcome to Word Guesser. \nYou have just three tries.\nEnter your guesses accordingly")

trials=1
word_set = (("m", "a", "n"), ("m", "e", "n"), ("p", "a", "n"), ("l", "a", "d"), ("b", "i", "n"), ("s", "i", "t"), ("c", "a", "p"), ("g", "o", "t"), ("t", "o", "y"))

word = random.choice(tuple(word_set))
f_g1=()
while trials <= 5 and word[:] != f_g1[:]:
    f_g=input("Input your guess: ")
    f_g1= (f_g[0], f_g[1], f_g[2])

    if trials == 1:
        print("First guess: "+ f_g )
    if trials == 2:
        print("Second guess: "+ f_g )
    if trials == 3:
        print("Third guess: "+ f_g )
    if trials == 4:
        print("Fourth guess: "+ f_g )
    if trials == 5:
        print("Last guess: "+ f_g )

    if f_g1[0] == word[0] and f_g1[1] != word[1] and f_g1[2] != word[2]:
        print("You got only the first letter right: " + word[0]+ "--")

    if f_g1[0] == word[0] and f_g1[1] == word[1] and f_g1[2] != word[2]:
        print("You got only the first two letters right: " + word[0]+word[1]+ "-")

    if f_g1[0] == word[0] and f_g1[1] != word[1] and f_g1[2] == word[2]:
        print("You got only two letters right: " + word[0]+ "-"+word[2])

    if f_g1[0] != word[0] and f_g1[1] == word[1] and f_g1[2] != word[2]:
        print("You got only the middle letter right: -" + word[1]+ "-")
            
    if f_g1[0] != word[0] and f_g1[1] == word[1] and f_g1[2] == word[2]:
        print("You got only the last two letters right: -" + word[1] + word[2])

    if f_g1[0] != word[0] and f_g1[1] != word[1] and f_g1[2] == word[2]:
        print("You got only the last letter right: --" + word[2])

    if f_g1[0] != word[0] and f_g1[1] != word[1] and f_g1[2] != word[2]:
        print("You did not get any letter right: ---")        

    if word[:] == f_g1[:]:
        print("Correct!!!. You got all the letters right: "+word[0]+word[1]+word[2])
        break
    trials += 1
else:
    print("Oh, sorry, you lost. Try again")