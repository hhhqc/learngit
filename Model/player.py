

class Player(object):
    def __init__(self, name, blood,mana,strength, agile,intelligence,physique,criticalChance,defenses, experience, level):
        self.name = name
        self.blood = blood
        self.strength = strength
        self.agile = agile
        self.experience = experience
        self.level = level
        self.attack = self.strength

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
    #血量=100+体质*5
    @blood.setter
    def blood(self):
        self._blood = 100 + self.physique * 5
    @blood.setter
    def blood(self, value):
        self._blood = 100 + self.physique * 5 + value

    # 法力
    @property
    def mana(self):
        return self._mana
    #法力=100+智力*5
    @mana.setter
    def mana(self):
        self._mana = 100 +  self._intelligence * 5
    @mana.setter
    def mana(self,value):
        self._mana = 100 + self._intelligence * 5 + value

    # 攻击
    @property
    def attack(self):
        return self._attack
    @attack.setter
    def attack(self, value):
        self._attack = 10 + value * 2

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
        self._strength = self._strength + value

    # 敏捷
    @property
    def agile(self):
        return self._agile
    @agile.setter
    def agile(self, value):
        self._agile = self._agile + value

    # 智力
    @property
    def intelligence(self):
        return self._intelligence
    @intelligence.setter
    def intelligence(self,value):
        self._intelligence = value

    #体质
    @property
    def physique(self):
        return self._physique
    @physique.setter
    def physique(self,value):
        self._physique = value

    #暴击率
    @property
    def criticalChance(self):
        return self._criticalChance
    @criticalChance.setter
    def criticalChance(self,value):
        self._criticalChance = value

    #技能伤害倍率
    @property
    def skillInjuryRate(self):
        return self._skillInjuryRate

    #防御力
    @property
    def defenses(self):
        return self._defenses
    @defenses.setter
    def defenses(self,value):
        self._defenses = value

    # 速度
    @property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self,value):
        self._speed = 10 + self._agile * 1.5

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
