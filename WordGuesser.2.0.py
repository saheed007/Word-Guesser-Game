import random

# Player details ############################################################
player_name = input("Input your name: ")
player_email = input("Input your email: ")
player_live = 0

class user:
    def __init__ (self, player_name, player_email):
        self.name = player_name
        self.email = player_email

print(f"\nWelcome {player_name.title()}, your username is {player_email.removesuffix('@gmail.com')}")


# choosing a difficulty level ###############################################
level_choice = True
level = ''
while level_choice == True:
    diff = [['Easy' , 1], ['Medium', 2], ['Hard', 3]]
    diff_input = input('Choose a difficulty level:\n 1: Easy\n 2: Medium\n 3: hard\n--> ').title()

    if diff_input == '1' or diff_input == 'Easy':
        print("You chose Easy\n")
        level = "Easy"
        level_choice = False
    elif diff_input == '2' or diff_input == 'Medium':
        print("You chose Medium\n")
        level = "Medium"
        level_choice = False
    elif diff_input == '3' or diff_input == 'Hard':
        print("You chose Hard\n")
        level = "Hard"
        level_choice = False
    else:
        print('Choose a valid level; enter the number or level')

# Default display grid ##############################################################
grid_1 = '''
 ______________
|    |    |    |
|    |    |    |
|____|____|____|
|    |    |    |
|    |    |    |
|____|____|____|
|    |    |    |
|    |    |    |
|____|____|____|
|    |    |    |
|    |    |    |
|____|____|____|
|    |    |    |
|    |    |    |
|____|____|____|'''

grid_2 = '''
 ______________
|    |    |    |
|    |    |    |
|____|____|____|
|    |    |    |
|    |    |    |
|____|____|____|
|    |    |    |
|    |    |    |
|____|____|____|
|    |    |    |
|    |    |    |
|____|____|____|'''

grid_3 = '''
 ______________
|    |    |    |
|    |    |    |
|____|____|____|
|    |    |    |
|    |    |    |
|____|____|____|
|    |    |    |
|    |    |    |
|____|____|____|'''


# setting the questions to the chosen difficulty level #####################

word_set ={1:["pan", "man", "sit", "cut", "son", "den", "try", "day"],2: ["fly", "sly", "pea"], 3:["gut", "wry", "qsr"]}
chosen_word_list = []

if level == "Easy":
    chosen_word_list = word_set[1]
    grid = grid_1
    max_trial  = 5
elif level == "Medium":
    chosen_word_list = word_set[2]
    grid = grid_2
    max_trial = 4
else:
    chosen_word_list = word_set[3]
    grid = grid_3
    max_trial = 3


word = random.choice(list(chosen_word_list))
print(word)

player_live = max_trial
print(f'You have {player_live} lives left')
trials = 1
guess=""
while trials <= max_trial  and word != guess:
    
    guess = input("Input your guess: ")

# setting grid cordinates according to trials
    grid_cord = [[37,41,46],[88,92,97],[139,143,148],[190,194,199],[241,245,250]]
    x, y, z = 0, 0, 0
    if trials == 1:
        x, y, z = grid_cord[0][0], grid_cord[0][1], grid_cord[0][2]
    elif trials == 2:
        x, y, z = grid_cord[1][0], grid_cord[1][1], grid_cord[1][2]
    elif trials == 3:
        x, y, z = grid_cord[2][0], grid_cord[2][1], grid_cord[2][2]
    elif trials == 4:
        x, y, z = grid_cord[3][0], grid_cord[3][1], grid_cord[3][2]
    else:
        x, y, z = grid_cord[4][0], grid_cord[4][1], grid_cord[4][2]

# Output ##############################################################
    try: 
        if guess[0] == word[0] and guess[1] != word[1] and guess[2] != word[2]:
            grid = grid[:x] + word[0].upper() + grid[(x+1):(y)] + '-' + grid[(y+1):(z)] + '-' +grid[(z+1):]

        if guess[0] == word[0] and guess[1] == word[1] and guess[2] != word[2]:
            grid = grid[:x] + word[0].upper() + grid[(x+1):(y)] + word[1].upper() + grid[(y+1):(z)] + '-' +grid[(z+1):]

        if guess[0] == word[0] and guess[1] != word[1] and guess[2] == word[2]:
            grid = grid[:x] + word[0].upper() + grid[(x+1):(y)] + '-' + grid[(y+1):(z)] + word[2].upper() +grid[(z+1):]

        if guess[0] != word[0] and guess[1] == word[1] and guess[2] != word[2]:
            grid = grid[:x] + '-' + grid[(x+1):(y)] + word[1].upper() + grid[(y+1):(z)] + '-' +grid[(z+1):]

        if guess[0] != word[0] and guess[1] == word[1] and guess[2] == word[2]:
            grid = grid[:x] + '-' + grid[(x+1):(y)] + word[1].upper() + grid[(y+1):(z)] + word[2].upper() +grid[(z+1):]

        if guess[0] != word[0] and guess[1] != word[1] and guess[2] == word[2]:
            grid = grid[:x] + '-' + grid[(x+1):(y)] + '-' + grid[(y+1):(z)] + word[2].upper() +grid[(z+1):]

        if guess[0] != word[0] and guess[1] != word[1] and guess[2] != word[2]:
            grid = grid[:x] + '-' + grid[(x+1):(y)] + '-' + grid[(y+1):(z)] + '-' +grid[(z+1):]

        if word[:] == guess[:]:
            grid = grid[:x] + word[0].upper() + grid[(x+1):(y)] + word[1].upper() + grid[(y+1):(z)] + word[2].upper() +grid[(z+1):]
            
            print(grid)
            print(f'You got the answer correct after {trials} trials')
            break
        trials += 1
        player_live -= 1
        
    except:
        print("\nPlease enter a three letter word")
    print(grid)
    print(f'You have {player_live} lives left')

    if trials == max_trial + 1  and word != guess:
        print("Oh, sorry, you lost. Try again.")
        
        

    


























