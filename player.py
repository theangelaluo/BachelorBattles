#format name = (hp, move)
contestants = {
    'jenn': (100, 'testMove'),
    'test': (50, 'testMove2'),
    'angela': (150, 'testMove3')
}

#format moveName = damage
moves = {
    'testMove': 100,
    'testMove2': 50,
    'testMove3': 150
}

#Player object: contains the name of the player and their deck of 'cards'
class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
    
#Card object: contains the name of the bachelorette, their hp, and their signature move (i haven't added in the headshot bc idk how)
class Card:
    def __init__(self, name, hp, move):
        self.name = name
        #self.headshot = headshot
        self.hp = hp
        self.move = move

#Move object: conatins the name of the move and how much damage it inflicts
class Move:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

#takes the name of the move and returns a Move object
def makeMove(moveName):
    damage = moves[moveName]
    move = Move(moveName, damage)
    return move

#takes the name of a bachelorette and returns a Card
def makeCard(character):
    contestant = contestants[character]
    move = makeMove(contestant[1])
    card = Card(character, contestant[0], move)
    return card

#gets the names of the current bachelorettes and puts them in tuple form (bc that's the only way dropdown menus work for some reason)
def dropdown():
    characters = []
    for key in contestants:
        characters.append((key, key))
    return characters



