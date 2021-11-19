from random import randint


is_effective_dictionary = {'bug': {'dark', 'grass', 'psychic'}, 
                           'dark': {'ghost', 'psychic'},
                           'dragon': {'dragon'}, 
                           'electric': {'water', 'flying'}, 
                           'fairy': {'dark', 'dragon', 'fighting'},
                           'fighting': {'dark', 'ice', 'normal', 'rock', 'steel'}, 
                           'fire': {'bug', 'grass', 'ice', 'steel'}, 
                           'flying': {'bug', 'fighting', 'grass'}, 
                           'ghost': {'ghost', 'psychic'}, 
                           'grass': {'water', 'ground', 'rock'}, 
                           'ground': {'electric', 'fire', 'poison', 'rock', 'steel'}, 
                           'ice': {'dragon', 'flying', 'grass', 'ground'}, 
                           'normal': set(), 
                           'poison': {'fairy', 'grass'}, 
                           'psychic': {'fighting', 'poison'}, 
                           'rock': {'bug', 'fire', 'flying', 'ice'},
                           'steel': {'fairy', 'ice', 'rock'},
                           'water': {'fire', 'ground', 'rock'}
                           }

not_effective_dictionary = {'bug': {'fairy', 'flying', 'fighting', 'fire', 'ghost','poison','steel'}, 
                            'dragon': {'steel'}, 
                            'dark': {'dark', 'fairy', 'fighting'},
                            'electric': {'dragon', 'electric', 'grass'},
                            'fairy': {'fire', 'poison', 'steel'},
                            'fighting': {'bug', 'fairy', 'flying', 'poison', 'psychic'}, 
                            'fire': {'dragon', 'fire', 'rock', 'water'}, 
                            'flying': {'electric', 'rock', 'steel'}, 
                            'ghost': {'dark'}, 
                            'grass': {'bug', 'dragon', 'grass', 'fire', 'flying', 'poison', 'steel'}, 
                            'ground': {'bug','grass'}, 
                            'ice': {'fire', 'ice', 'steel', 'water'}, 
                            'normal': {'rock', 'steel'}, 
                            'poison': {'ghost', 'ground', 'poison', 'rock'}, 
                            'psychic': {'psychic', 'steel'}, 
                            'rock': {'fighting', 'ground', 'steel'}, 
                            'steel': {'electric', 'fire', 'steel', 'water'},
                            'water': {'dragon','grass', 'ice'}
                            }

no_effect_dictionary = {'electric': {'ground'}, 
                        'dragon': {'fairy'},
                        'fighting': {'ghost'}, 
                        'ghost': {'normal', 'psychic'}, 
                        'ground': {'flying'}, 
                        'normal': {'ghost'}, 
                        'poison': {'steel'},
                        'psychic': {'dark'}, 
                        
                        'bug': set(), 'dark': set(), 'fairy': set(),'fire': set(), 
                        'flying': set(), 'grass': set(), 'ice': set(), 
                        'rock': set(), 'steel': set(), 'water': set()
                        }

#Dictionaries that determine element advantages and disadvantages
# =============================================================================

class Move(object):
    def __init__(self, name = "", element = "normal", power = 20, accuracy = 80,
                 attack_type = 2):
        """ Initialize attributes of the Move object """
        
        self.name = name
        self.element = element
        self.power = power
        
        self.accuracy = accuracy
        self.attack_type = attack_type  #attack_type is 1, 2 or 3 
        # 1 - status moves, 2 - physical attacks, 3 - special attacks
        
    def __str__(self):
            
        '''
returns self.name or name of the move for printing
        '''        
        return self.name

    def __repr__(self):
        '''
returns the name of the move for in shell
        '''
        return self.name
        pass
    
    def get_name(self):
        '''
returns the name of the move when function is called
        '''
        return self.name
        pass
    
    def get_element(self):
        '''
returns the element of the move
        '''
        return self.element
        pass
    
    def get_power(self):
        '''
returns the power of the move, int
        '''
        return self.power
        pass
    
    def get_accuracy(self):
        '''
returns the accuracy of the move
        '''
        return self.accuracy
        pass
    
    def get_attack_type(self):
        '''
returns the attack type of the move
        '''
        return self.attack_type
        pass

    def __eq__(self,m):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == m.get_name() and self.element == m.get_element() and\
                self.power == m.get_power() and self.accuracy == m.get_accuracy() and\
                self.attack_type == m.get_attack_type()
        
        
class Pokemon(object):
    def __init__(self, name = "", element1 = "normal", element2 = "", moves = None,
                 hp = 100, patt = 10, pdef = 10, satt = 10, sdef = 10):
        ''' initializes attributes of the Pokemon object '''
        
        self.name = name
        self.element1 = element1
        self.element2 = element2
        
        self.hp = hp
        self.patt = patt
        self.pdef = pdef
        self.satt = satt
        self.sdef = sdef
        
        self.moves = moves
        
        try:
            if len(moves) > 4:
                self.moves = moves[:4]
                
        except TypeError: #For Nonetype
            self.moves = list()

    def __eq__(self,p):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == p.name and \
            self.element1 == p.element1 and \
            self.element2 == p.element2 and \
            self.hp == p.hp and \
            self.patt == p.patt and \
            self.pdef == p.pdef and \
            self.satt == p.satt and \
            self.sdef == p.sdef and \
            self.moves == p.moves

    def __str__(self):
        '''
returns all the moves of the pokemon in fromat
        '''
        x= "{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}\n{:<15s}{:<15s}\n".format(self.name,str(self.hp),str(self.patt),str(self.pdef),str(self.satt),str(self.sdef),(self.element1),(self.element2))
        q = []
        for i in self.moves:
            i = str(i)
            q.append('{:<15s}'.format(i))
        qq = ''.join(q)
        return x+qq

    def __repr__(self):
        '''
returns all the moves of the pokemon in fromat
        '''
        
        x= "{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}\n{:<15s}{:<15s}\n".format(self.name,str(self.hp),str(self.patt),str(self.pdef),str(self.satt),str(self.sdef),(self.element1),(self.element2))
        q = []
        for i in self.moves:
            i = str(i)
            q.append('{:<15s}'.format(i))
        qq = ''.join(q)
        return x+qq
    
    def get_name(self):
        '''
returns the name of the pokemon
        '''
        return self.name
        pass
    
    def get_element1(self):
        '''
returns the first element of the pokemon
        '''
        return self.element1
        pass
    
    def get_element2(self):
        '''
returns the second name of the pokemon
        '''
        return self.element2
        pass
    
    def get_hp(self):
        '''
returns the hp of the pokemon
        '''
        return self.hp
        pass
    
    def get_patt(self):
        '''
returns patt
        '''
        return self.patt
        pass

    def get_pdef(self):
        '''
returns pdef
        '''
        return self.pdef
        pass

    def get_satt(self):
        '''
return satt
        '''
        return self.satt
        pass

    def get_sdef(self):
        '''
returns sdef
        '''
        return self.sdef
        pass
    
    def get_moves(self):
        '''
returns the list of moves of the pokemon
        '''
        return self.moves
        pass

    def get_number_moves(self):
        '''
returns the len of moves or how many moves the pokemon has
        '''
        return len(self.moves)
        pass

    def choose(self,index):
        '''
chooses a move to use
        '''
        try:
            return self.moves[index]
        except:
            return None

        
    def show_move_elements(self):
        '''
prints the elements of each move the pokemon has
        '''
        elmts = []
        for move in self.moves:
            elmt = Move.get_element(move)
            elmts.append(elmt)
        for i in elmts:
            print('{:<15s}'.format(i), end="")
            
        pass


    def show_move_power(self):
        '''
prints the power of each move the pokemone has
        '''
        powers = []
        for move in self.moves:
            p = Move.get_power(move)
            powers.append(p)
        for i in powers:
            print('{:<15d}'.format(i), end="")
        pass

    def show_move_accuracy(self):
        '''
prints the accuracy of each move the pokemone has
        '''
        accuracy = []
        for move in self.moves:
            a = Move.get_accuracy(move)
            accuracy.append(a)
        for i in accuracy:
            print('{:<15d}'.format(i), end="")
        pass
        
        
    def add_move(self, move):
        '''
adds a move to the list of moves the pokemon has
        '''
        if len(self.moves) == 0:
            self.moves = []
            self.moves.append(move)
        elif len(self.moves) < 4:
            self.moves.append(move)
        pass
            
        
    def attack(self, move, opponent):
        '''
an attacking function from pokemon to its opponent
default values are given but will be changed throughout the function. it calculates the 
damage by first checking if the move hits or not, with randinto  to compare the accuracy
then it gets all the neccessary attack and defenses based on the attack type of the move
then it gets the elements of the move, if one certain element is effect on the opponent
pokemone, then the move will double, if it isnt  effect it is halved, and no effect if
there is no effect, thus the damage is 0.
        '''
        mp,a,d,modifier = 0,0,0,1.0
        mp = int(move.get_power())
        atype = move.get_attack_type()
        if int(atype) == 2:
            a = int(self.patt)
            d = int(opponent.get_pdef())
        if int(atype) == 3:
            a = int(self.satt)
            d = int(opponent.get_sdef())
        elif int(atype) == 1:
            print("Invalid attack_type, turn skipped.")
            return None
        ri = randint(1,100)
        # accuracy = int(Move.get_accuracy(move))
        # print(ri)
        # print(accuracy)
        if ri > move.get_accuracy():
            print("Move missed!")
            return None
        oe1 = Pokemon.get_element1(opponent)
        oe2 = Pokemon.get_element2(opponent)
        e1 = Move.get_element(move)
        if e1 in is_effective_dictionary:
            if oe1 in is_effective_dictionary[e1]:
                modifier *= 2

        if e1 in not_effective_dictionary:
            if oe1 in not_effective_dictionary[e1]:
                modifier *= .5

        if e1 in no_effect_dictionary:
            if oe1 in no_effect_dictionary[e1]:
                modifier = 0

        #--------------------------------------------
        if e1 in is_effective_dictionary:
            if oe2 in is_effective_dictionary[e1]:
                modifier *= 2

        if e1 in not_effective_dictionary:
            if oe2 in not_effective_dictionary[e1]:
                modifier *= .5

        if e1 in no_effect_dictionary:
            if oe2 in no_effect_dictionary[e1]:
                modifier = 0
        damage = (((mp*(a/d)*20)/50)+2)*modifier
        if damage == 0:
            print('No effect!')
        else:
            if modifier > 1:
                print("It's super effective!!!!")
            elif modifier < 1:
                print("Not very effective...")
            elif modifier == 0:
                print('No effect!')
        if e1 == self.element1 or e1 == self.element2:
            modifier *= 1.5 

        damage = (((mp*(a/d)*20)/50)+2)*modifier
        damage = int(damage)
        opponent.subtract_hp(damage)


        
    def subtract_hp(self,damage):
        '''
is used in the attack method, where it subtracts the health of the opponent
        '''
        h = int(self.hp)
        h = h - damage
        if h < 0:
            h = 0
        self.hp = h
