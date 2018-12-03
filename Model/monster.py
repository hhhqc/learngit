
class Monster(object):
    def __init__(self, name, blood, attack, speed, criticalChance,
                 skillInjuryRate, defenses, level):
        self._name = name
        self._blood = blood
        self._attack = attack
        self._speed = speed
        self._criticalChance = criticalChance
        self._skillInjuryRate = skillInjuryRate
        self._defenses = defenses
        self._level = level

        # 名字

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def blood(self):
        return self._blood

    @blood.setter
    def blood(self, value):
        self._blood = value

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        self._attack =  value

    # 最大攻击=攻击*1.1
    @property
    def attackMax(self):
        return self._attack * 1.1

    # 最小攻击=攻击*0.9
    @property
    def attackMin(self):
        return self._attack * 0.9

    @property
    def criticalChance(self):
        return self._criticalChance

    @criticalChance.setter
    def criticalChance(self,value):
        self._criticalChance = value

    @criticalChance.setter
    def criticalChance(self, value):
        self._criticalChance = value

    @property
    def skillInjuryRate(self):
        return self._skillInjuryRate

    @property
    def defenses(self):
        return self._defenses

    @defenses.setter
    def defenses(self, value):
        self._defenses = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed =  value

    # 等级
    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, value):
        self._level = value