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


#gets the names of the current bachelorettes and puts them in tuple form (bc that's the only way dropdown menus work for some reason)
def dropdown(lst):
    characters = []
    for key in lst:
        characters.append((key, key))
    return characters
