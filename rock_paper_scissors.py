import random

win_game = 0
player_one_win =0
player_two_win =0
options = ["Rock", "Paper", "Scissors"]
#print(random.choice(options))

def player_one():
    player_one_roll = ""
    player_one_roll = random.choice(options)
    return player_one_roll

def player_two():
    player_two_roll = ""
    player_two_roll = random.choice(options)
    return player_two_roll

def game(player_one_roll, player_two_roll):
    global win_game
    global player_one_win
    global player_two_win
    player_one()
    player_two()
   
    if player_one_roll == "Rock" and player_two_roll == "Scissors":
        print("PLAYER ONE =", player_one_roll.upper(), " VS ","PLAYER TWO =", player_two_roll.upper())
        print("Player One Wins with", player_one_roll, "\n")
        win_game = win_game +1
        player_one_win +=1
                            
    elif player_one_roll == "Rock" and player_two_roll == "Rock":
        print("PLAYER ONE =", player_one_roll.upper(), " VS ","PLAYER TWO =", player_two_roll.upper())
        print("DRAW! THROW-HANDS", "\n")
        win_game = win_game +1
                                
    elif player_one_roll == "Paper" and player_two_roll == "Rock":
        print("PLAYER ONE =", player_one_roll.upper(), " VS ","PLAYER TWO =", player_two_roll.upper())
        print("Player One Wins with ", player_one_roll, "\n")
        win_game = win_game +1
        player_one_win +=1
                                
    elif player_one_roll == "Paper" and player_two_roll == "Paper":
        print("PLAYER ONE =", player_one_roll.upper(), " VS ","PLAYER TWO =", player_two_roll.upper())
        print("DRAW! THROW-HANDS", "\n")
        win_game = win_game +1
        
    elif player_one_roll == "Scissors" and player_two_roll == "Paper":
        print("PLAYER ONE =", player_one_roll.upper(), " VS ","PLAYER TWO =", player_two_roll.upper())
        print("Player One Wins with ",player_one_roll, "\n")
        win_game = win_game +1
        player_one_win +=1
                            
    elif player_one_roll == "Scissors" and player_two_roll == "Scissors":
        print("PLAYER ONE =", player_one_roll.upper(), " VS ","PLAYER TWO =", player_two_roll.upper())
        print("DRAW! THROW-HANDS", "\n")
        win_game = win_game +1
        
    else:
        print("PLAYER ONE =", player_one_roll.upper(), " VS ","PLAYER TWO =", player_two_roll.upper())
        print("Player Two Wins with ", player_two_roll, "\n")
        win_game = win_game +1
        player_two_win +=1
                    
while player_one_win !=3 and player_two_win !=3:
    game(player_one(), player_two())
if player_one_win ==3:
    print("PLAYER ONE WINS ",player_one_win, "OUT OF " ,win_game, "GAMES! WITH", win_game - player_one_win - player_two_win, "WERE A DRAW" )
if player_two_win ==3:
    print("PLAYER TWO WINS ",player_two_win, "OUT OF " ,win_game, "GAMES! WITH", win_game - player_one_win - player_two_win, "WERE A DRAW" )
