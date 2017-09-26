# Battleship_Functions.py
from random import randint
from random import choice
from operator import itemgetter
from time import sleep

# function to print board
def print_board(board):
  alpha_coords = ["A","B","C","D","E","F","G","H","I","J"]
  numbr_coords = ["1","2","3","4","5","6","7","8","9","10"]
  print()
  print("          My Board")
  print("   ---------------------")
  print("    " + " ".join(numbr_coords))
  print("   ---------------------")
  for iter_row in range(len(board)):
    print("|%s| " % alpha_coords[iter_row]+" ".join(board[iter_row])+" |")
  print("   ---------------------")

# function to print opponent's board
def print_opponent(board):
  alpha_coords = ["A","B","C","D","E","F","G","H","I","J"]
  numbr_coords = ["1","2","3","4","5","6","7","8","9","10"]
  print()
  print("      Opponent's Board")
  print("   ---------------------")
  print("    " + " ".join(numbr_coords))
  print("   ---------------------")
  for iter_row in range(len(board)):
    print("|%s| " % alpha_coords[iter_row]+" ".join(board[iter_row])+" |")
  print("   ---------------------")

def print_gamespace(player,opponent):
  alpha_coords = ["A","B","C","D","E","F","G","H","I","J"]
  numbr_coords = ["1","2","3","4","5","6","7","8","9","10"]
  labels = ["Legend:","---------","Hit:   X","Miss: [ ]"," "," "," "," "," "," "]
  print()
  print("         My Board               Opponent's Board")
  print("   ---------------------      ---------------------")
  print("    " + " ".join(numbr_coords) + "       " + " ".join(numbr_coords))
  print("   ---------------------      ---------------------")
  for iter_row in range(len(player)):
    print("|%s| " % alpha_coords[iter_row]+" ".join(player[iter_row])+" |"\
          + "  " + "|%s| " % alpha_coords[iter_row]+" ".join(opponent[iter_row])+" |"\
          + "  " + labels[iter_row])
  print("   ---------------------      ---------------------")

'''
# define aircraft carrier location

print()
print("Place Aircraft Carrier (*****)")

alpha_coords = ["A","B","C","D","E","F","G","H","I","J"]
numbr_coords = ["1","2","3","4","5","6","7","8","9","10"]
ac_orient = 'none'
ac_row = 'none'
ac_col = 'none'

while ac_orient == 'none':
  ac_orient = input("Horizontal or Verical? (Input 'H' or 'V'): ")
  if ac_orient != 'H' and ac_orient != 'V':
    ac_orient = 'none'
    print("Error: incorrect input")
    
if ac_orient == 'H': #horizontal
  while ac_row == 'none':
    ac_row = input("Which row? \
(Choose 'A','B','C','D','E','F','G','H','I', or 'J'): ")
    if ac_row not in alpha_coords:
      ac_row = 'none'
      print("Error: incorrect input")
  while ac_col == 'none':
    ac_col = input("On which column does it begin? \
(Choose '1','2','3','4','5','6','7','8','9', or '10'): ")
    if ac_col not in numbr_coords:
      ac_col = 'none'
      print("Error: incorrect input")
    elif ac_col in numbr_coords[6:11]:
      ac_col = 'none'
      print("Error: too far right to fit the whole ship")
  for x in range(numbr_coords.index(ac_col),(numbr_coords.index(ac_col)+5)):
    board[alpha_coords.index(ac_row)][x] = "*"
  print_board(board)
  
elif ac_orient == 'V': #vertical
  while ac_col == 'none':
    ac_col = input("Which column? \
(Choose '1','2','3','4','5','6','7','8','9', or '10': ")
    if ac_col not in numbr_coords:
      ac_col = 'none'
      print("Error: incorrect input")
  while ac_row == 'none':
    ac_row = input("On which row does it begin? \
(Choose 'A','B','C','D','E','F','G','H','I', or 'J'): ")
    if ac_row not in alpha_coords:
      ac_row = 'none'
      print("Error: incorrect input")
    elif ac_row in alpha_coords[6:11]:
      ac_row = 'none'
      print("Error: too far down to fit the whole ship")
  for x in range(alpha_coords.index(ac_row),(alpha_coords.index(ac_row)+5)):
    board[x][numbr_coords.index(ac_col)] = "*"
  print_board(board)

'''

def place_ship(board,ship,dict_locations):
  ships = {
    'aircraft carrier': 5,
    'battleship': 4,
    'cruiser': 3,
    'submarine': 3,
    'destroyer': 2
  }
  alpha_coords = ["A","B","C","D","E","F","G","H","I","J"]
  numbr_coords = ["1","2","3","4","5","6","7","8","9","10"]
  ship_orient = 'none'
  ship_row = 'none'
  ship_col = 'none'
  ship_check = 'none'
  #
  print()
  print("Place %s (%d spaces)" % (ship, ships[ship]))
  #
  while ship_orient == 'none':
    ship_orient = input("Horizontal or Verical? (Input H or V): ")
    if ship_orient != 'H' and ship_orient != 'V':
      ship_orient = 'none'
      print("  Error: incorrect input")
  # horizontal
  if ship_orient == 'H':
    while ship_check == 'none':
      while ship_row == 'none':
        ship_row = input("Which row? (Choose A through J): ")
        if ship_row not in alpha_coords:
          ship_row = 'none'
          print("  Error: incorrect input")
      while ship_col == 'none':
        ship_col = input("On which column does it begin? (Choose 1 through 10): ")
        if ship_col not in numbr_coords:
          ship_col = 'none'
          print("  Error: incorrect input")
        elif ship_col in numbr_coords[(11-ships[ship]):10]:
          ship_col = 'none'
          print("  Error: too far right to fit the whole ship")
      ship_spaces = board[alpha_coords.index(ship_row)][numbr_coords.index(ship_col):(numbr_coords.index(ship_col)+ships[ship])]
      if "*" in ship_spaces:
        ship_check = 'none'
        ship_row = 'none'
        ship_col = 'none'
        print("  Error: can not place ship on occupied spaces")
      else:
        ship_check = 'done'
    for x in range(numbr_coords.index(ship_col),(numbr_coords.index(ship_col)+ships[ship])):
      board[alpha_coords.index(ship_row)][x] = "*"
    dict_locations[ship] = [] #add ship to dictionary
    for x in range(0,ships[ship]):
      dict_locations[ship].append([alpha_coords.index(ship_row),numbr_coords.index(ship_col)+x]) 
    return (board,dict_locations)
  # vertical
  elif ship_orient == 'V':
    while ship_check == 'none':
      while ship_col == 'none':
        ship_col = input("Which column? (Choose 1 through 10): ")
        if ship_col not in numbr_coords:
          ship_col = 'none'
          print("  Error: incorrect input")
      while ship_row == 'none':
        ship_row = input("On which row does it begin? (Choose A through J): ")
        if ship_row not in alpha_coords:
          ship_row = 'none'
          print("  Error: incorrect input")
        elif ship_row in alpha_coords[(11-ships[ship]):10]:
          ship_row = 'none'
          print("  Error: too far down to fit the whole ship")
      ship_spaces = []
      for x in range(alpha_coords.index(ship_row),(alpha_coords.index(ship_row)+ships[ship])):
        ship_spaces.append(board[x][numbr_coords.index(ship_col)])
      if "*" in ship_spaces:
        ship_check = 'none'
        ship_row = 'none'
        ship_col = 'none'
        print("  Error: can not place ship on occupied spaces")
      else:
        ship_check = 'done'
    for x in range(alpha_coords.index(ship_row),(alpha_coords.index(ship_row)+ships[ship])):
      board[x][numbr_coords.index(ship_col)] = "*"
    dict_locations[ship] = [] #add ship to dictionary
    for x in range(0,ships[ship]):
      dict_locations[ship].append([alpha_coords.index(ship_row)+x,numbr_coords.index(ship_col)])
    return (board,dict_locations)
  #

# fuction to establish a random board
def place_ship_random(board,ship,dict_locations):
  ships = {
    'aircraft carrier': 5,
    'battleship': 4,
    'cruiser': 3,
    'submarine': 3,
    'destroyer': 2
  }
  alpha_coords = ["A","B","C","D","E","F","G","H","I","J"]
  numbr_coords = ["1","2","3","4","5","6","7","8","9","10"]
  ship_orient = 'none'
  ship_row = 'none'
  ship_col = 'none'
  ship_check = 'none'
  #
  while ship_orient == 'none':
    ship_orient = randint(0,1)
  # horizontal
  if ship_orient == 0:
    while ship_check == 'none':
      while ship_row == 'none':
        ship_row = randint(0,9)
      while ship_col == 'none':
        ship_col = randint(0,9)
        if ship_col in range((11-ships[ship]),10):
          ship_col = 'none'
      ship_spaces = board[ship_row][ship_col:(ship_col+ships[ship])]
      if "*" in ship_spaces:
        ship_check = 'none'
        ship_row = 'none'
        ship_col = 'none'
      else:
        ship_check = 'done'
    for x in range(ship_col,(ship_col+ships[ship])):
      board[ship_row][x] = "*"
    dict_locations[ship] = [] #add ship to dictionary
    for x in range(0,ships[ship]):
      dict_locations[ship].append([ship_row,ship_col+x]) 
    return (board,dict_locations)
  # vertical
  elif ship_orient == 1:
    while ship_check == 'none':
      while ship_col == 'none':
        ship_col = randint(0,9)
      while ship_row == 'none':
        ship_row = randint(0,9)
        if ship_row in range((11-ships[ship]),10):
          ship_row = 'none'
      ship_spaces = []
      for x in range(ship_row,(ship_row+ships[ship])):
        ship_spaces.append(board[x][ship_col])
      if "*" in ship_spaces:
        ship_check = 'none'
        ship_row = 'none'
        ship_col = 'none'
      else:
        ship_check = 'done'
    for x in range(ship_row,(ship_row+ships[ship])):
      board[x][ship_col] = "*"
    dict_locations[ship] = [] #add ship to dictionary
    for x in range(0,ships[ship]):
      dict_locations[ship].append([ship_row+x,ship_col])
    return (board,dict_locations)
  #

#
def define_board(board,dict_locations):
  all_ships = ["aircraft carrier","battleship","cruiser","submarine","destroyer"]
  ships_placed = []
  first_ship = 'none'
  second_ship = 'none'
  third_ship = 'none'
  fourth_ship = 'none'
  fifth_ship = 'none'
  print_board(board)
  print()
  # first ship
  while first_ship == 'none':
    first_ship = input("Which ship do you want to place first? ")
    if first_ship not in all_ships:
      print("  Error: incorrect input")
      first_ship = 'none'
  ships_placed.append(first_ship)
  place_ship(board,first_ship,dict_locations)
  print_board(board)
  print("Ships placed: %s" %first_ship)
  print("Ships left: %s, %s, %s, and %s" \
        %(list(set(all_ships)-set(ships_placed))[0],\
        list(set(all_ships)-set(ships_placed))[1],\
        list(set(all_ships)-set(ships_placed))[2],\
        list(set(all_ships)-set(ships_placed))[3]))
  print()
  # second ship
  while second_ship == 'none':
    second_ship = input("Which ship do you want to place next? ")
    if second_ship in ships_placed:
      print("  Error: already placed that ship")
      second_ship = 'none'
    elif second_ship not in all_ships:
      print("  Error: incorrect input")
      second_ship = 'none'
  ships_placed.append(second_ship)    
  place_ship(board,second_ship,dict_locations)
  print_board(board)
  print("Ships placed: %s and %s" %(first_ship,second_ship))
  print("Ships left: %s, %s, and %s" \
        %(list(set(all_ships)-set(ships_placed))[0],\
        list(set(all_ships)-set(ships_placed))[1],\
        list(set(all_ships)-set(ships_placed))[2]))
  print()
  # third ship
  while third_ship == 'none':
    third_ship = input("Which ship do you want to place next? ")
    if third_ship in ships_placed:
      print("  Error: already placed that ship")
      third_ship = 'none'
    elif third_ship not in all_ships:
      print("  Error: incorrect input")
      third_ship = 'none'
  ships_placed.append(third_ship)  
  place_ship(board,third_ship,dict_locations)
  print_board(board)
  print("Ships placed: %s, %s, and %s" %(first_ship,second_ship,third_ship))
  print("Ships left: %s, and %s" \
        %(list(set(all_ships)-set(ships_placed))[0],\
        list(set(all_ships)-set(ships_placed))[1]))
  print()
  # fourth ship
  while fourth_ship == 'none':
    fourth_ship = input("Which ship do you want to place next? ")
    if fourth_ship in ships_placed:
      print("  Error: already placed that ship")
      fourth_ship = 'none'
    elif fourth_ship not in all_ships:
      print("  Error: incorrect input")
      fourth_ship = 'none'
  ships_placed.append(fourth_ship)  
  place_ship(board,fourth_ship,dict_locations)
  print_board(board)
  print("Ships placed: %s, %s, %s, and %s" %(first_ship,second_ship,third_ship,fourth_ship))
  print("Ships left: %s" \
        %(list(set(all_ships)-set(ships_placed))[0]))
  print()
  # fifth ship
  fifth_ship = list(set(all_ships)-set(ships_placed))[0]
  print("Finally, place the %s." % fifth_ship)
  place_ship(board,fifth_ship,dict_locations)
  print_board(board)
  return (board,dict_locations)

#
def get_player_guess(board,board_forprinting,hits,locations):
  alpha_coords = ["A","B","C","D","E","F","G","H","I","J"]
  numbr_coords = ["1","2","3","4","5","6","7","8","9","10"]
  opponent_aircraftcarrier_hits = hits["aircraft carrier"]
  opponent_battleship_hits = hits["battleship"]
  opponent_cruiser_hits = hits["cruiser"]
  opponent_submarine_hits = hits["submarine"]
  opponent_destroyer_hits = hits["destroyer"]
  opponent_location_aircraftcarrier = locations["aircraft carrier"]
  opponent_location_battleship = locations["battleship"]
  opponent_location_cruiser = locations["cruiser"]
  opponent_location_submarine = locations["submarine"]
  opponent_location_destroyer = locations["destroyer"]
  shot_check = 'none'
  shot_row = 'none'
  shot_col = 'none'
  print(" Choose where to shoot:")
  while shot_check == 'none':
    while shot_row == 'none':
      shot_row = input("  Which row? ")
      if shot_row not in alpha_coords:
        shot_row = 'none'
        print("   Error: incorrect input")
    while shot_col == 'none':
      shot_col = input("  Which column? ")
      if shot_col not in numbr_coords:
        shot_col = 'none'
        print("   Error: incorrect input")
    if " " in board[alpha_coords.index(shot_row)][numbr_coords.index(shot_col)]:
      shot_check = 'none'
      shot_row = 'none'
      shot_col = 'none'
      print("   Error: already guessed there")
    elif "X" in board[alpha_coords.index(shot_row)][numbr_coords.index(shot_col)]:
      shot_check = 'none'
      shot_row = 'none'
      shot_col = 'none'
      print("   Error: already guessed there")
    else:
      shot_check = 'done'
  if [alpha_coords.index(shot_row),numbr_coords.index(shot_col)] in opponent_location_aircraftcarrier:
    print(" Hit: aircraft carrier")
    opponent_aircraftcarrier_hits = opponent_aircraftcarrier_hits+1
    if opponent_aircraftcarrier_hits > 4:
      print(" You sunk my aircraft carrier!")
    board[alpha_coords.index(shot_row)][numbr_coords.index(shot_col)] = "X"
    board_forprinting[alpha_coords.index(shot_row)][numbr_coords.index(shot_col)] = "X"
  elif [alpha_coords.index(shot_row),numbr_coords.index(shot_col)] in opponent_location_battleship:
    print(" Hit: battleship")
    opponent_battleship_hits = opponent_battleship_hits+1
    if opponent_battleship_hits > 3:
      print(" You sunk my battleship!")
    board[alpha_coords.index(shot_row)][numbr_coords.index(shot_col)] = "X"
    board_forprinting[alpha_coords.index(shot_row)][numbr_coords.index(shot_col)] = "X"
  elif [alpha_coords.index(shot_row),numbr_coords.index(shot_col)] in opponent_location_cruiser:
    print(" Hit: cruiser")
    opponent_cruiser_hits = opponent_cruiser_hits+1
    if opponent_cruiser_hits > 2:
      print(" You sunk my cruiser!")
    board[alpha_coords.index(shot_row)][numbr_coords.index(shot_col)] = "X"
    board_forprinting[alpha_coords.index(shot_row)][numbr_coords.index(shot_col)] = "X"
  elif [alpha_coords.index(shot_row),numbr_coords.index(shot_col)] in opponent_location_submarine:
    print(" Hit: submarine")
    opponent_submarine_hits = opponent_submarine_hits+1
    if opponent_submarine_hits > 2:
      print(" You sunk my submarine!")
    board[alpha_coords.index(shot_row)][numbr_coords.index(shot_col)] = "X"
    board_forprinting[alpha_coords.index(shot_row)][numbr_coords.index(shot_col)] = "X"
  elif [alpha_coords.index(shot_row),numbr_coords.index(shot_col)] in opponent_location_destroyer:
    print(" Hit: destroyer")
    opponent_destroyer_hits = opponent_destroyer_hits+1
    if opponent_destroyer_hits > 1:
      print(" You sunk my destroyer!")
    board[alpha_coords.index(shot_row)][numbr_coords.index(shot_col)] = "X"
    board_forprinting[alpha_coords.index(shot_row)][numbr_coords.index(shot_col)] = "X" 
  else:
    print(" Miss")
    board[alpha_coords.index(shot_row)][numbr_coords.index(shot_col)] = " "
    board_forprinting[alpha_coords.index(shot_row)][numbr_coords.index(shot_col)] = " "
  hits["aircraft carrier"] = opponent_aircraftcarrier_hits
  hits["battleship"] = opponent_battleship_hits
  hits["cruiser"] = opponent_cruiser_hits
  hits["submarine"] = opponent_submarine_hits
  hits["destroyer"] = opponent_destroyer_hits
  return (board,board_forprinting,hits)

def get_computer_guess(player_board,hit_number,locations,hit_locations):
  #
  ships = {
    'aircraft carrier': 5,
    'battleship': 4,
    'cruiser': 3,
    'submarine': 3,
    'destroyer': 2
  }
  alpha_coords = ["A","B","C","D","E","F","G","H","I","J"]
  numbr_coords = ["1","2","3","4","5","6","7","8","9","10"]
  player_aircraftcarrier_hits = hit_number["aircraft carrier"]
  player_battleship_hits = hit_number["battleship"]
  player_cruiser_hits = hit_number["cruiser"]
  player_submarine_hits = hit_number["submarine"]
  player_destroyer_hits = hit_number["destroyer"]
  player_location_aircraftcarrier = locations["aircraft carrier"]
  player_location_battleship = locations["battleship"]
  player_location_cruiser = locations["cruiser"]
  player_location_submarine = locations["submarine"]
  player_location_destroyer = locations["destroyer"]
  shot_check = 'none'
  shot_row = 'none'
  shot_col = 'none'
  guess_list = []
  for key in ships: #go through list of ships
    if hit_number[key]>0 and hit_number[key]<ships[key]: #if ship has more than 0 but less than max hits
      #search in viscinity of ship (called key)
      if hit_number[key]>1: #if at least 2 hits on ship already
        #check ship orientation
        if hit_locations[key][0][0] == hit_locations[key][1][0]: #row orientation
          #sort list of points
          hits_list_sorted = sorted(hit_locations[key], key=itemgetter(1))
          #grab point to left
          new_guess_left = [hits_list_sorted[0][0],hits_list_sorted[0][1]-1]
          if new_guess_left[1] in range(0,10):
            if player_board[new_guess_left[0]][new_guess_left[1]] == '*' or \
               player_board[new_guess_left[0]][new_guess_left[1]] == 'O':
              guess_list.append(new_guess_left)
          #grab point to right
          new_guess_right = [hits_list_sorted[0][0],hits_list_sorted[len(hits_list_sorted)-1][1]+1]
          if new_guess_right[1] in range(0,10):
            if player_board[new_guess_right[0]][new_guess_right[1]] == '*' or \
               player_board[new_guess_right[0]][new_guess_right[1]] == 'O':
              guess_list.append(new_guess_right)
          #check for points in middle
          for x in range(1,len(hits_list_sorted)-1):
            new_guess_middle = [hits_list_sorted[0][0],hits_list_sorted[0][1]+x]
            if new_guess_middle not in hits_list_sorted:
              guess_list.append(new_guess_middle)
          #choose one from guess_list
          #print(guess_list) ## remove after debugging
          shot = choice(guess_list)
          shot_row = shot[0]
          shot_col = shot[1]
          shot_check = 'done'
        else: #column orientation
          #sort list of points
          hits_list_sorted = sorted(hit_locations[key], key=itemgetter(0))
          #grab point above
          new_guess_above = [hits_list_sorted[0][0]-1,hits_list_sorted[0][1]]
          if new_guess_above[0] in range(0,10):
            if player_board[new_guess_above[0]][new_guess_above[1]] == '*' or \
               player_board[new_guess_above[0]][new_guess_above[1]] == 'O':
              guess_list.append(new_guess_above)
          #grab point below
          new_guess_below = [hits_list_sorted[len(hits_list_sorted)-1][0]+1,hits_list_sorted[0][1]]
          if new_guess_below[0] in range(0,10):
            if player_board[new_guess_below[0]][new_guess_below[1]] == '*' or \
               player_board[new_guess_below[0]][new_guess_below[1]] == 'O':
              guess_list.append(new_guess_below)
          #check for points in middle
          for x in range(1,len(hits_list_sorted)-1):
            new_guess_middle = [hits_list_sorted[0][0]+x,hits_list_sorted[0][1]]
            if new_guess_middle not in hits_list_sorted:
              guess_list.append(new_guess_middle)
          #choose one from guess_list
          #print(guess_list) ##remove after debugging
          shot = choice(guess_list)
          shot_row = shot[0]
          shot_col = shot[1]
          shot_check = 'done'
      else: #only one point found
        #check all 4 neighboring points
        new_guess_left = [hit_locations[key][0][0],hit_locations[key][0][1]-1]
        if new_guess_left[1] in range(0,10):
          if player_board[new_guess_left[0]][new_guess_left[1]] == '*' or \
             player_board[new_guess_left[0]][new_guess_left[1]] == 'O':
            guess_list.append(new_guess_left) 
        new_guess_right = [hit_locations[key][0][0],hit_locations[key][0][1]+1]
        if new_guess_right[1] in range(0,10):
          if player_board[new_guess_right[0]][new_guess_right[1]] == '*' or \
             player_board[new_guess_right[0]][new_guess_right[1]] == 'O':
            guess_list.append(new_guess_right) 
        new_guess_above = [hit_locations[key][0][0]-1,hit_locations[key][0][1]]
        if new_guess_above[0] in range(0,10):
          if player_board[new_guess_above[0]][new_guess_above[1]] == '*' or \
             player_board[new_guess_above[0]][new_guess_above[1]] == 'O':
            guess_list.append(new_guess_above) 
        new_guess_below = [hit_locations[key][0][0]+1,hit_locations[key][0][1]]
        if new_guess_below[0] in range(0,10):
          if player_board[new_guess_below[0]][new_guess_below[1]] == '*' or \
             player_board[new_guess_below[0]][new_guess_below[1]] == 'O':
            guess_list.append(new_guess_below)
        #print(guess_list)
        shot = choice(guess_list)
        shot_row = shot[0]
        shot_col = shot[1]
        shot_check = 'done'
  if shot_row == 'none' and shot_col == 'none':
      #choose randomly on board
      while shot_check == 'none':
        while shot_row == 'none':
          shot_row = randint(0,9)
        while shot_col == 'none':
          shot_col = randint(0,9)
        if " " in player_board[shot_row][shot_col] or \
           "X" in player_board[shot_row][shot_col]:
          shot_check = 'none'
          shot_row = 'none'
          shot_col = 'none'
        else:
          shot_check = 'done'
  print(" " + "-".join([alpha_coords[shot_row],numbr_coords[shot_col]]))
  sleep(1)
  #save location of hit like in player code above
  if [shot_row,shot_col] in player_location_aircraftcarrier:
    print(" I hit your aircraft carrier.")
    hit_locations['aircraft carrier'].append([shot_row,shot_col])
    player_aircraftcarrier_hits = player_aircraftcarrier_hits+1
    if player_aircraftcarrier_hits > 4:
      print(" I sank your aircraft carrier!")
    player_board[shot_row][shot_col] = "X"
  elif [shot_row,shot_col] in player_location_battleship:
    print(" I hit your battleship.")
    hit_locations['battleship'].append([shot_row,shot_col])
    player_battleship_hits = player_battleship_hits+1
    if player_battleship_hits > 3:
      print(" I sank your battleship!")
    player_board[shot_row][shot_col] = "X"
  elif [shot_row,shot_col] in player_location_cruiser:
    print(" I hit your cruiser.")
    hit_locations['cruiser'].append([shot_row,shot_col])
    player_cruiser_hits = player_cruiser_hits+1
    if player_cruiser_hits > 2:
      print(" I sank your cruiser!")
    player_board[shot_row][shot_col] = "X"
  elif [shot_row,shot_col] in player_location_submarine:
    print(" I hit your submarine.")
    hit_locations['submarine'].append([shot_row,shot_col])
    player_submarine_hits = player_submarine_hits+1
    if player_submarine_hits > 2:
      print(" I sank your submarine!")
    player_board[shot_row][shot_col] = "X"
  elif [shot_row,shot_col] in player_location_destroyer:
    print(" I hit your destroyer.")
    hit_locations['destroyer'].append([shot_row,shot_col])
    player_destroyer_hits = player_destroyer_hits+1
    if player_destroyer_hits > 1:
      print(" I sank your destroyer!")
    player_board[shot_row][shot_col] = "X"
  else:
    print(" Miss")
    player_board[shot_row][shot_col] = " "
  hit_number["aircraft carrier"] = player_aircraftcarrier_hits
  hit_number["battleship"] = player_battleship_hits
  hit_number["cruiser"] = player_cruiser_hits
  hit_number["submarine"] = player_submarine_hits
  hit_number["destroyer"] = player_destroyer_hits
  return (player_board,hit_number,hit_locations)
