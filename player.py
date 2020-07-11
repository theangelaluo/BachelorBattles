#format name = (hp, headshot, move)
contestants = {
    'Kelsey': (100, 'kelsey.jpeg', 'testMove0'),
    'Lexi': (100, 'lexi.jpeg', 'testMove1'),
    'Natasha': (100, 'natasha.jpeg', 'testMove2'),
    'Madison': (100, 'madison.jpeg', 'testMove3'),
    'Hannah Ann': (100, 'hannah_ann.jpeg', 'testMove4'),
    'Victoria F': (100, 'victoria_f.jpeg','testMove5'),
    'Tammy': (100, 'tammy.jpeg','testMove6'),
}

#format moveName = damage
moves = {
    'testMove0': 100,
    'testMove1': 50,
    'testMove2': 150,
    'testMove3': 100,
    'testMove4': 50,
    'testMove5': 150,
    'testMove6': 150

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

#gets the names of the current bachelorettes and puts them in tuple form (bc that's the only way dropdown menus work for some reason)
def dropdown():
    characters = []
    for key in contestants:
        characters.append((key, key))
    return characters



