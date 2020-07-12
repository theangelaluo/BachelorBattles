#format name = (hp, headshot, move)
contestants = {
    'Kelsey': (100, 'kelsey.jpeg', 'testMove0'),
    'Lexi': (100, 'lexi.jpeg', 'testMove1'),
    'Natasha': (100, 'natasha.jpeg', 'testMove2'),
    'Madison': (100, 'madison.jpeg', 'testMove3'),
    'Hannah Ann': (100, 'hannah_ann.jpeg', 'testMove4'),
    'Victoria F': (100, 'victoria_f.jpeg','testMove5'),
    'Tammy': (100, 'tammy.jpeg','testMove6'),
    'Sydney': (100, 'sydney.jpeg','testMove7'),
    'Victoria P': (100, 'victoria_p.jpeg','testMove8'),
    'Shiann': (100, 'shiann.jpeg','testMove9'),
    'Kiarra': (100, 'kiarra.jpeg','testMove10'),
    'Alayah': (100, 'alayah.jpeg','testMove11'),
    'Mykenna': (100, 'mykenna.jpeg','testMove12')
}

#format moveName = damage
moves = {
    'testMove0': 100,
    'testMove1': 50,
    'testMove2': 150,
    'testMove3': 100,
    'testMove4': 50,
    'testMove5': 150,
    'testMove6': 150,
    'testMove7': 50,
    'testMove8': 150,
    'testMove9': 100,
    'testMove10': 50,
    'testMove11': 150,
    'testMove12': 150,
}

#Player object: contains the name of the player and their deck of 'cards'
class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

#Card object: contains the name of the bachelorette, their hp, and their signature move (i haven't added in the headshot bc idk how)
class Card:
    def __init__(self, name, headshot, hp, move):
        self.name = name
        self.headshot = headshot
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
    move = makeMove(contestant[2])
    card = Card(character, contestant[1], contestant[0], move)
    return card


#function to attack, called after form is submitted
def attack(playerName, playerCard, opponentCard):
    if playerName != "Opponent":
        damage = playerCard.move.damage
        opponentCard.hp -= damage
        if opponentCard.hp <= 0:
            return opponentCard.name + " has been sent home"
        return playerCard.name + " dealt " + str(damage) + " amount of damage to " + opponentCard.name
    else:
        damage = opponentCard.move.damage
        playerCard.hp -= damage
        if playerCard.hp <= 0:
            return playerCard.name + " has been sent home"
        return opponentCard.name + " dealt " + str(damage) + " amount of damage to " + playerCard.name


#gets the names of the current bachelorettes and puts them in tuple form (bc that's the only way dropdown menus work for some reason)
def dropdown(lst):
    characters = []
    for key in lst:
        characters.append((key, key))
    return characters

#check to see who's left
def checkDeck(lst):
    for element in lst:
        if element.hp > 0:
            return True
    return False


    


