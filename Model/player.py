

class Player(object):
    def __init__(self, name, blood, strength, agile, experience, level):
        self.name = name
        self.blood = blood
        self.strength = strength
        self.agile = agile
        self.experience = experience
        self.level = level

    # 名字
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    # @name.deleter
    # def name(self):
    #     del self._name
    # 血量

    @property
    def blood(self):
        return self._blood

    @blood.setter
    def blood(self, value):
        self._blood = value
    # 攻击

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        self._attack = 10 + self.strength * 2

    # 最大攻击
    @property
    def attackMax(self):
        return self._attack * 1.1

    # 最小攻击
    @property
    def attackMin(self):
        return self._attack * 0.9

    # 力量
    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        self._strength = value

    # 敏捷
    @property
    def agile(self):
        return self._agile

    @agile.setter
    def agile(self, value):
        self._agile = value
    # 速度

    @property
    def speed(self):
        return 10 + self._agile * 2

    # 经验
    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = value

    # 等级
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
