from contestants import contestants, moves

#Player object: contains the name of the player and their deck of 'cards'
class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

#Card object: contains the name of the bachelorette, their hp, and their signature move
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


#check to see who's left
def checkDeck(lst):
    for element in lst:
        if element.hp > 0:
            return True
    return False


    


