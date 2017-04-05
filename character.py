movePrompt = """Where would you like to move?
    [N]orth
    [W]est
    [S]outh
    [E]ast\n"""

class Character:

    def __init__(self, name=None, level=1, inventory=None):
        if not name:
            self.name = input("What's your name?")
        self.name = name
        self.hp = 10
        self.level = level
        self.baseDamage = 1
        self.hitChance = 10
        self.inventory = inventory

    def __str__(self):
        return "C"

class Player(Character):

    def __init__(self, *args):
        super().__init__(*args)
        self.hitChance = 100

    def levelUp(self):
        self.level += 1

    def move(self):
        direction = input(movePrompt)
        return direction.lower()[:1]

    def __str__(self):
        return "P"

class Monster(Character):

    def __init__(self):
        super().__init__("Wolf")
        self.hp = 2

    def __str__(self):
        return "W"

    def move(self):
        return None
