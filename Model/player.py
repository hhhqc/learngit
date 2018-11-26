

class Player(object):
    def __init__(self,name,blood,attack):
        self.name = name
        self.blood = blood
        self.attack = attack

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name = value
    @name.deleter
    def name(self):
        del self._name

    @property
    def blood(self):
        return self._blood
    @blood.setter
    def blood(self,value):
        self._blood = value
    @blood.deleter
    def blood(self):
        del self._blood

    @property
    def attack(self):
        return self._attack
    @attack.setter
    def attack(self,value):
        self._attack = value
    @attack.deleter
    def attack(self):
        del self._attack