class Equip():
    def __init__(self,id,name,level,attack,strength,agile,intelligence,physique,speed,blood,mana,defenses):
        self._id = id
        self._name = name
        self._level = level
        self._attack = attack
        self._strength = strength
        self._agile = agile
        self._intelligence = intelligence
        self._physique = physique
        self._speed = speed
        self._blood = blood
        self._mana = mana
        self._defenses = defenses

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @property
    def attack(self):
        return self._attack

    @property
    def strength(self):
        return self._strength

    @property
    def agile(self):
        return self._agile

    @property
    def intelligence(self):
        return self._intelligence

    @property
    def physique(self):
        return self._physique

    @property
    def speed(self):
        return self._speed

    @property
    def blood(self):
        return self._blood

    @property
    def mana(self):
        return self._mana

    @property
    def defenses(self):
        return self._defenses

