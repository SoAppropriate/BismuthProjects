class Db:
    import sqlite3
    def __init__(self):
        self.conn = self.sqlite3.connect("../../Bismuth/static/ledger.db")
        self.conn.text_factory = str
        self.c = self.conn.cursor()

class ScoreDb:
    import sqlite3
    def __init__(self):
        self.conn = self.sqlite3.connect("score.db")
        self.conn.text_factory = str
        self.c = self.conn.cursor()

class Game:
    def __init__(self):
        self.seed = None
        self.block = None
        self.hash = None
        self.finished = False
        self.story = {}
        self.step = 0
        self.quit = False

class Hero:
    FULL_HP = 500

    def __init__(self):
        self.health = self.FULL_HP
        self.power = 10
        self.alive = True
        self.in_combat = False
        self.experience = 0
        self.armor = 0
        self.inventory = {"weapon":None, "armor":None}

class Troll:
    def __init__(self):
        self.name = "Troll"
        self.health = 20
        self.power = 15
        self.alive = True

class Goblin:
    def __init__(self):
        self.name = "Goblin"
        self.health = 10
        self.power = 10
        self.alive = True

class Berserker:
    def __init__(self):
        self.name = "Berserker"
        self.health = 5
        self.power = 30
        self.alive = True

class Dragon:
    def __init__(self):
        self.name = "Dragon"
        self.health = 300
        self.power = 75
        self.alive = True