

class Player(object):
    def __init__(self, name, blood,attack,mana,strength, agile,intelligence,physique,criticalChance,skillInjuryRate,defenses, experience, level):
        self.name = name
        self.blood = blood
        self.mana = mana
        self.attack = attack
        self.strength = strength
        self.agile = agile
        self.intelligence = intelligence
        self.physique = physique
        self.criticalChance = criticalChance
        self.skillInjuryRate = skillInjuryRate
        self.defenses = defenses
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

    # 血量=100+体质*5+装备血量
    @property
    def blood(self):
        return self._blood
    @blood.setter
    def blood(self):
        self._blood = 100 + self.physique * 5
    @blood.setter
    def blood(self, value):
        self._blood = 100 + self.physique * 5 + value

    # 法力=100+智力*5+装备法力
    @property
    def mana(self):
        return self._mana
    @mana.setter
    def mana(self):
        self._mana = 100 +  self._intelligence * 5
    @mana.setter
    def mana(self,value):
        self._mana = 100 + self._intelligence * 5 + value

    # 攻击=10+力量*2
    @property
    def attack(self):
        return self._attack
    @attack.setter
    def attack(self, value):
        self._attack = 10 + self._strength * 2 + value

    # 最大攻击=攻击*1.1
    @property
    def attackMax(self):
        return self._attack * 1.1

    # 最小攻击=攻击*0.9
    @property
    def attackMin(self):
        return self._attack * 0.9

    # 力量=力量+装备力量
    @property
    def strength(self):
        return self._strength
    @strength.setter
    def strength(self, value):
        self._strength = self._strength + value

    # 敏捷=敏捷+装备敏捷
    @property
    def agile(self):
        return self._agile
    @agile.setter
    def agile(self, value):
        self._agile = self._agile + value

    # 智力=智力+装备智力
    @property
    def intelligence(self):
        return self._intelligence
    @intelligence.setter
    def intelligence(self,value):
        self._intelligence = self._intelligence + value

    #体质=体质+装备体质
    @property
    def physique(self):
        return self._physique
    @physique.setter
    def physique(self,value):
        self._physique = self._physique + value

    #暴击率=(10+敏捷*0.3)
    @property
    def criticalChance(self):
        return self._criticalChance
    @criticalChance.setter
    def criticalChance(self):
        self._criticalChance = (10+self._agile*0.3)
    @criticalChance.setter
    def criticalChance(self,value):
        self._criticalChance = self._criticalChance + value

    #技能伤害倍率=(1+智力*0.02)
    @property
    def skillInjuryRate(self):
        return 1+self._intelligence*0.02

    #防御力=10+体质*1+装备防御
    @property
    def defenses(self):
        return self._defenses
    @defenses.setter
    def defenses(self,value):
        self._defenses = 10+ self._physique*1 + value

    # 速度=10+敏捷*1.5+装备敏捷
    @property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self,value):
        self._speed = 10 + self._agile * 1.5 + value

    # 经验
    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience =  self._experience + value

    # 等级
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = self._level + value
