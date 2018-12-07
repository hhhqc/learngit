import configparser


class Player(object):
    def __init__(
            self,
            strength,
            agile,
            intelligence,
            physique,
            name,
            blood,
            mana,
            attack,
            speed,
            criticalChance,
            defenses,
            experience,
            level):
        self._strength = strength
        self._agile = agile
        self._intelligence = intelligence
        self._physique = physique
        self._name = name
        self._blood = blood
        self._mana = mana
        self._attack = attack
        self._speed = speed
        self._criticalChance = criticalChance
        self._defenses = defenses
        self._experience = experience
        self._level = level
        self._hpMax = blood
        self._mpMax = mana
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
        return self._blood + self.physique * 5

    @blood.setter
    def blood(self, value):
        self._blood = self._blood + value

    @property
    def hpMax(self):
        return self._hpMax + self.physique * 5

    # 法力=100+智力*5+装备法力
    @property
    def mana(self):
        return self._mana + self.intelligence * 5

    @mana.setter
    def mana(self, value):
        self._mana = self._mana + value

    @property
    def mpMax(self):
        return self._mpMax + self.intelligence * 5

    # 攻击=10+力量*2
    @property
    def attack(self):
        return self._attack + self.strength * 2

    @attack.setter
    def attack(self, value):
        self._attack = self._attack + value

    # 最大攻击=攻击*1.1
    @property
    def attackMax(self):
        return self.attack * 1.1

    # 最小攻击=攻击*0.9
    @property
    def attackMin(self):
        return self.attack * 0.9

    # 力量=力量+装备力量
    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        if self._strength is None:
            self._strength = value
        else:
            self._strength = self._strength + value

    # 敏捷=敏捷+装备敏捷
    @property
    def agile(self):
        return self._agile

    @agile.setter
    def agile(self, value):
        if self._agile is None:
            self._agile = value
        else:
            self._agile = self._agile + value

    # 智力=智力+装备智力
    @property
    def intelligence(self):
        return self._intelligence

    @intelligence.setter
    def intelligence(self, value):
        if self._intelligence is None:
            self._intelligence = value
        else:
            self._intelligence = self._intelligence + value

    # 体质=体质+装备体质
    @property
    def physique(self):
        return self._physique

    @physique.setter
    def physique(self, value):
        if self._physique is None:
            self._physique = value
        else:
            self._physique = self._physique + value

    # 暴击率=(10+敏捷*0.3)
    @property
    def criticalChance(self):
        return self._criticalChance + self._agile * 0.3

    @criticalChance.setter
    def criticalChance(self, value):
        self._criticalChance = self._criticalChance + value

    # 技能伤害倍率=(1+智力*0.02)
    @property
    def skillInjuryRate(self):
        return 1 + self._intelligence * 0.02

    # 防御力=10+体质*1+装备防御
    @property
    def defenses(self):
        return self._defenses + self._physique * 1

    @defenses.setter
    def defenses(self, value):
        self._defenses = self._defenses + value

    # 速度=10+敏捷*1.5+装备敏捷
    @property
    def speed(self):
        return self._speed + self._agile * 1.5

    @speed.setter
    def speed(self, value):
        self._speed = self._speed + value

    # 经验
    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = self._experience + value
        if (self._experience >= self.level * 100):
            self._experience =  self._experience - (self.level * 100)
            self.level = 1

    # 等级
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = self._level + value
        self.blood = self.hpMax - self.blood
        self.mana = self.mpMax - self.mana
        print('获得五点属性点,请选择增加的属性点')
        i = 1
        while(i<6):
            print('1.力量 2.智力 3. 敏捷 4.体质')
            property = input('请输入指令:')
            if(property=='1'):
                self.strength = 1
            elif(property=='2'):
                self.intelligence = 1
            elif(property=='3'):
                self.agile = 1
            elif(property=='4'):
                self.physique = 1
            else:
                print('输入错误请重新输入')
                i -= 1
            i += 1
    def getPlayer(self):
        return self.player
