# Pokemon Game simplified
# Lawnrce Kim
#
# pokemon game
# but a little more simplified according to directions

"""
Pokemon game
"""
import csv
from random import randint
from random import seed
from copy import deepcopy

from pokemon import Pokemon
from pokemon import Move

seed(1) #Set the seed so that the same events always happen


#DO NOT CHANGE THIS!!!
# =============================================================================
element_id_list = [None, "normal", "fighting", "flying", "poison", "ground", "rock", 
                   "bug", "ghost", "steel", "fire", "water", "grass", "electric", 
                   "psychic", "ice", "dragon", "dark", "fairy"]

#Element list to work specifically with the moves.csv file.
#   The element column from the moves.csv files gives the elements as integers.
#   This list returns the actual element when given an index
# =============================================================================
    
def read_file_moves(fp):  
    '''
This function takes in the file pointer created from opening the moves.csv file and
returns a list of move objects

does not add moves if gen-id is not 1, damage classification is 1, no pow value and no acc value
    '''
    moves = []
    mov = csv.reader(fp)
    next(mov,None)
    for line in mov:
        try:
            name = line[1]
            typ = int(line[3])
            atk = int(line[9]) #1 is status change, 2 is physical, 3 is special
            # if atk is 1, move will not be added to list)
            if (line[2])== '1' and atk!=1 and line[4] != '' and line[6] != "":
                move = Move(name, element_id_list[typ], int(line[4]), int(line[6]), atk)
                moves.append(move)
        except:
            pass
    return moves

def read_file_pokemon(fp):
    '''
This function takes in the file pointer created from opening the pokemon.csv file and
returns a list of pokemon objects
    '''
    pokemon = []
    ids = set()
    pok = csv.reader(fp)
    next(pok,None)
    for line in pok:
        gen = int(line[11])
        ide = int(line[0])
        if gen == 1 and ide not in ids:
            name = line[1].lower()
            elmt1 = line[2].lower()
            elmt2 = line[3].lower()
            hp = int(line[5])
            patt = int(line[6])
            pdef = int(line[7])
            satt = int(line[8])
            sdef = int(line[9])
            ids.add(ide)
            poke = Pokemon(name, elmt1, elmt2, None, hp, patt, pdef, satt, sdef)
            pokemon.append(poke)
    return pokemon
        
def choose_pokemon(choice,pokemon_list):
    '''
choose pokemon based on index or name. If index, the number will be used to 
obtain the pokemon based on index, if given name, it will be compared to the name in
the index.
    '''
    try:
        if choice.isalpha():
            for count,lst in enumerate(pokemon_list):                
                if choice.lower() == lst.get_name():
                    pok = pokemon_list[count]
                    poke = deepcopy(pok)
                    return poke
        else:
            choice = int(choice)-1
            pok = pokemon_list[choice]
            poke = deepcopy(pok)
            return poke
    except:
        return False

def add_moves(pokemon,moves_list):
    '''
Adds moves to the pokemon. Pokemone in the pokemon list are at default set to None moves, so
this function will add moves to them, trying to add 4.
'''

    try:
        check = 0
        while int(pokemon.get_number_moves()) != 4: 
            rm = randint(0,len(moves_list)-1)
            if int(pokemon.get_number_moves()) == 0:
                pokemon.add_move(moves_list[rm])
            try:
                arm = moves_list[rm] #try except here because it might not work
            except:
                return False
            e1 = pokemon.get_element1()
            e2 = pokemon.get_element2()
            if e1 == arm.get_element() or e2 == arm.get_element():
                if arm not in pokemon.get_moves():
                    pokemon.add_move(arm)
            check += 1
            if check == 200:
                return False
        return True
    except:
        return False


def turn (player_num, player_pokemon, opponent_pokemon):
    '''
turn is the function for the players to duel another. Shows the stats of the pokemon and 
moves. After both players have attacked, it will display the hp of the pokemons after.
    '''
    print("Player {}'s turn".format(player_num))
    print(player_pokemon)
     
    while True:
        print("\nShow options: 'show ele', 'show pow', 'show acc'")  
        x = input("Select an attack between 1 and {} or show option or 'q': ".format(len(player_pokemon.get_moves()))).lower()
        if x == 'q':
            if player_num == 1:        
                print("Player {} quits, Player {} has won the pokemon battle!".format(player_num, 2))
            elif player_num == 2:
                print("Player {} quits, Player {} has won the pokemon battle!".format(player_num, 1))
            return False
        if x == 'show ele' or x == 'show pow' or x == 'show acc':
            if x == 'show ele':
                player_pokemon.show_move_elements()
            elif x == 'show pow':
                player_pokemon.show_move_power()
            elif x == 'show acc':
                player_pokemon.show_move_accuracy()
            continue
        if x == '1':
            m =player_pokemon.choose(0)
        elif (x) == '2':
            m = player_pokemon.choose(1)
        elif (x) == '3':
            m = player_pokemon.choose(2)
        elif (x) == '4':
            m = player_pokemon.choose(3)
        else:
            print('not working')
            continue
        print("selected move:",m)
        break
    print("{} hp before:{}".format(opponent_pokemon.get_name(), opponent_pokemon.get_hp()))
    player_pokemon.attack(m,opponent_pokemon)
    print("{} hp after:{}".format(opponent_pokemon.get_name(), opponent_pokemon.get_hp()))
    if int(opponent_pokemon.get_hp()) <= 0:
        if player_num == 1:         
            print("Player {}'s pokemon fainted, Player {} has won the pokemon battle!".format(2,player_num))
        elif player_num == 2:
            print("Player {}'s pokemon fainted, Player {} has won the pokemon battle!".format(1,player_num))
        return False
    if player_num == 2:
        print("Player {} hp after: ".format(1),opponent_pokemon.get_hp())
        print("Player {} hp after: ".format(2),player_pokemon.get_hp())
    return True

def main():
    mfpm = open("moves.csv", 'r')
    pfpm = open("pokemon.csv", 'r')   
    mfp = read_file_moves(mfpm)
    pfp = read_file_pokemon(pfpm)
    usr_inp = input("Would you like to have a pokemon battle? ").lower()
    while True: #true to do another game or wrong input
        while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':
            usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q: ").lower()
        if usr_inp != 'y':
            print("Well that's a shame, goodbye")
            return
        else:
            while True: #another while loop here for the invalid choiec of a pokmon
            #name or index
                p1 = input("Player 1, choose a pokemon by name or index: ")
                try:
                    pok1 = choose_pokemon((p1), pfp)
                except:
                    print("Invalid option, choose a pokemon by name or index: ")
                    continue
                print("pokemon{}:\n".format(1),pok1)
                tf1 = add_moves(pok1, mfp)
                if tf1 == False:
                    pass
                break
            #-------------------------------------------
            while True:
                p2 = input("Player 2, choose a pokemon by name or index: ")
                try: 
                    pok2 = choose_pokemon((p2), pfp)
                except:
                    print("Invalid option, choose a pokemon by name or index: ")
                    continue
                print("pokemon{}:\n".format(2),pok2)
                tf2 = add_moves(pok2, mfp)
                if tf2 == False:
                    pass
                break
        p2h = pok2.get_hp()
        p1h = pok1.get_hp()
        while int(p1h) > 0 or int(p2h) > 0: #they contain all the checkers
            c = turn(1,pok1,pok2)
            if c == False:
                p1h = -1
                break
            tf1 = add_moves(pok1, mfp)
            if tf1 == False:
                print('no work')
                p1h = -1
                p2h = -2
                break
            c2 = turn(2,pok2,pok1)
            if c2 == False:
                p1h = -1
                p2h = -2
            tf2 = add_moves(pok2, mfp)
            if tf2 == False:
                print('no work')
                p1h = -1
                p2h = -2
                break
            if c == False:
                print('game ended')
                break
        # for starting another game if wanted after a win
        another = input("Battle over, would you like to have another? ").lower()
        while another != 'n' and another != 'q' and another != 'y':
            another = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q:").lower()
        if another != 'y':
            print("Well that's a shame, goodbye")
            break
        if another == 'y':
            continue
    
if __name__ == "__main__":
    main()
