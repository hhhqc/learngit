import configparser
from Model.player import Player
from Model.monster import Monster


class LoadConfig():
    def LoadConfigPlayer(player):
        conf = configparser.ConfigParser()
        conf.read(r"..\config\player.config")
        player = Player(conf.getint(player, 'player_strength'),
                        conf.getint(player, 'player_agile'),
                        conf.getint(player, 'player_intelligence'),
                        conf.getint(player, 'player_physique'),
                        conf.get(player, 'player_name'),
                        conf.getint(player, 'player_blood'),
                        conf.getint(player, 'player_mana'),
                        conf.getfloat(player, 'player_attack'),
                        conf.getfloat(player, 'player_speed'),
                        conf.getfloat(player, 'player_criticalChance'),
                        conf.getint(player, 'player_defenses'),
                        conf.getint(player, 'player_experience'),
                        conf.getint(player, 'player_level'))
        # 初始化
        player.attack = 0
        player.blood = 0
        player.mana = 0
        player.speed = 0
        return player

    def LoadConfigMonster(monster):
        conf = configparser.ConfigParser()
        conf.read(r"..\config\monster.config")
        monster = Monster(conf.get(monster, 'monster_name'),
                          conf.getint(monster, 'monster_blood'),
                          conf.getfloat(monster, 'monster_attack'),
                          conf.getfloat(monster, 'monster_speed'),
                          conf.getfloat(monster, 'monster_criticalChance'),
                          conf.getfloat(monster, 'monster_skillInjuryRate'),
                          conf.getint(monster, 'monster_defenses'),
                          conf.getint(monster, 'monster_level'),
                          conf.getint(monster, 'monster_exe'))
        return monster

    def LoadConfigbackpack(backpack):
        conf = configparser.ConfigParser()
        conf.read(r"..\config\backpack.config")
        for i in range(1,6):
            BackpackBar = 'BackpackBar_'+str(i)
            backpack.append(conf.get(BackpackBar,'equip'))
        return backpack

    def LoadConfigEquip(equip):
        conf = configparser.ConfigParser()
        conf.read(r"..\config\euqip.config")
