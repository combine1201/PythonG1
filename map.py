from time import sleep
from random import randint
from character import Player, Monster

class Map:

    def __init__(self, X, Y):
        self.x = X
        self.y = Y
        self.data = None
        self.createMap()
        self.players = []
        self.monsters = []

    def createMap(self):
        d = []
        d.append(['#' for _ in range(self.x+2)])
        for _ in range(self.y):
            row = []
            row.append('#')
            for x in range(self.x):
                row.append('_')
            row.append('#')
            d.append(row)
        d.append(['#' for _ in range(self.x+2)])
        print(d)
        self.data = d
        self.x += 2
        self.y += 2

    def __str__(self):
        return "\n".join([" ".join(row) for row in reversed(self.data)])

    def __setitem__(self, key, value):
        self.data[key[1] % self.y][key[0] % self.x] = value

    def __getitem__(self, key):
        return self.data[key[1]][key[0]]

    def update(self):
        for monster in self.monsters:
            self[monster.position] = 'W'
        
        for player in self.players:
            oldPosition = player.position
            direction = player.character.move()
            newPosition = self.translate(direction, oldPosition)
            if not newPosition:
                print("Invalid Option")
                sleep(.2)
                return
            if self[newPosition] != '_':
                print("Something is in the way!")
                sleep(.2)
                return
            player.position = newPosition
            self[oldPosition] = '_'
            self[newPosition] = str(player.character)
        

    def translate(self, direction, position):
        if direction == 'n':
            return (position[0], position[1]+1)
        elif direction == 'w':
            return (position[0]-1, position[1])
        elif direction == 's':
            return (position[0], position[1]-1)
        elif direction == 'e':
            return (position[0]+1, position[1])
        elif direction == None:
            return position
        else:
            return None

    def addCharacter(self, character):
        # Adds character to center of map for testing
        start = (randint(1,self.x-1), randint(1,self.y-1))
        while self[start] != '_':
            start = (randint(1,self.x-1), randint(1,self.y-1))
        newChar = PlayerContext(character, start)
        self[newChar.position] = str(newChar.character)
        if isinstance(character, Player):
            self.players.append(newChar)
        elif isinstance(character, Monster):
            self.monsters.append(newChar)

class PlayerContext:

    def __init__(self, character, position):
        self.character = character
        self.position = position
