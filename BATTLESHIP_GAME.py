import Battleship_Functions
from time import sleep
# print_board(board) : prints board with player label
# print_opponent(board) : prints board with opponent label
# print_gamespace(player,opponent) : prints both player's and opponent's boards
# place_ship(board,ship) : takes user input to place ship
# place_ship_random(board,ship) : places defined ship arbitrarily
# define_board(board) : display for user ship placement step
# get_player_guess(board,board_forprinting,hits,locations) : gets player's next guess
# get_computer_guess(player_board,hit_number,locations,hit_locations) : get's computer's next guess

# greeting
print()
print(" ------------")
print("  BATTLESHIP")
print(" ------------")

# create opponent board
# board showing all ship locations
opponent = []
for x in range(0, 10):
  opponent.append(["O"] * 10)
opponent_locations = {}
Battleship_Functions.place_ship_random(opponent,"aircraft carrier",opponent_locations)
Battleship_Functions.place_ship_random(opponent,"battleship",opponent_locations)
Battleship_Functions.place_ship_random(opponent,"cruiser",opponent_locations)
Battleship_Functions.place_ship_random(opponent,"submarine",opponent_locations)
Battleship_Functions.place_ship_random(opponent,"destroyer",opponent_locations)
# viewable opponent board (doesn't give away opponent positions)
opponent_forprinting = []
for x in range(0, 10):
  opponent_forprinting.append(["O"] * 10)
#Battleship_Functions.print_opponent(opponent) #remove after debugging

# create player board
board = []
for x in range(0, 10):
  board.append(["O"] * 10)
ship_locations = {}
print()
print("PLACE SHIPS:")
print(" ships:  aircraft carrier (*****)  battleship (****)")
print("         cruiser (***)  submarine (***)  destroyer (**)")
print()
print("Do you want to place ships yourself or have them assigned randomly?")
board_design = 'none'
while board_design == 'none':
  board_design = input(" Type self or random: ")
  if board_design == 'self':
    Battleship_Functions.define_board(board,ship_locations)
  elif board_design == 'random':
    Battleship_Functions.place_ship_random(board,"aircraft carrier",ship_locations)
    Battleship_Functions.place_ship_random(board,"battleship",ship_locations)
    Battleship_Functions.place_ship_random(board,"cruiser",ship_locations)
    Battleship_Functions.place_ship_random(board,"submarine",ship_locations)
    Battleship_Functions.place_ship_random(board,"destroyer",ship_locations)
  else:
    board_design = 'none'

# print game board
Battleship_Functions.print_gamespace(board,opponent_forprinting)

# hit counter
opponent_hits = {"aircraft carrier": 0,
                 "battleship": 0,
                 "cruiser": 0,
                 "submarine": 0,
                 "destroyer": 0
                 }
opponent_aircraftcarrier_hits = opponent_hits["aircraft carrier"]
opponent_battleship_hits = opponent_hits["battleship"]
opponent_cruiser_hits = opponent_hits["cruiser"]
opponent_submarine_hits = opponent_hits["submarine"]
opponent_destroyer_hits = opponent_hits["destroyer"]
player_hits = {"aircraft carrier": 0,
               "battleship": 0,
               "cruiser": 0,
               "submarine": 0,
               "destroyer": 0
               }
player_aircraftcarrier_hits = player_hits["aircraft carrier"]
player_battleship_hits = player_hits["battleship"]
player_cruiser_hits = player_hits["cruiser"]
player_submarine_hits = player_hits["submarine"]
player_destroyer_hits = player_hits["destroyer"]

# hit locations on player board (used by computer opponent)
player_hit_locations = {"aircraft carrier": [],
                        "battleship": [],
                        "cruiser": [],
                        "submarine": [],
                        "destroyer": []
                        }

# game
sleep(3)
print()
print("PLAY GAME:")
winner = 'none'
alpha_coords = ["A","B","C","D","E","F","G","H","I","J"]
numbr_coords = ["1","2","3","4","5","6","7","8","9","10"]
while winner == 'none':
  print()
  print("YOUR TURN")
  Battleship_Functions.get_player_guess(opponent,opponent_forprinting,\
                                        opponent_hits,\
                                        opponent_locations)
  Battleship_Functions.print_gamespace(board,opponent_forprinting)
  if opponent_hits['aircraft carrier'] == 5 and \
     opponent_hits['battleship'] == 4 and \
     opponent_hits['cruiser'] == 3 and \
     opponent_hits['submarine'] == 3 and \
     opponent_hits['destroyer'] == 2:
    winner = 'player'
    print("Congratulations! You won!")
    sleep(60)
  else:
    sleep(3)
    print()
    print("COMPUTER'S TURN")
    sleep(2)
    Battleship_Functions.get_computer_guess(board,player_hits,\
                                            ship_locations,\
                                            player_hit_locations)
    Battleship_Functions.print_gamespace(board,opponent_forprinting)
    if player_hits['aircraft carrier'] == 5 and \
       player_hits['battleship'] == 4 and \
       player_hits['cruiser'] == 3 and \
       player_hits['submarine'] == 3 and \
       player_hits['destroyer'] == 2:
      winner = 'computer'
      print("Sorry, you lost. Better luck next time!")
      sleep(60)
