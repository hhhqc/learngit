from CombatSystem.combat import Combat
from Model.player import Player
from Model.npc import NPC
from config import *
import os
import configparser


def main():
    # print("战斗开始")
    # player = Player('player',100,20,10,0,1) # 名字,血量,力量,敏捷,经验,等级
    # players = [player]
    # npc = NPC('npc',100,10,10,0,1)
    # npcs = [npc]
    # combatSystem = Combat
    # combatSystem.Combat(players, npcs)
    conf = configparser.ConfigParser()
    conf.read(r"..\config\player.config")
    print(conf.getint('player', 'player_level'))
    player = Player(conf.get('player', 'player_name'),
                    conf.getfloat('player', 'player_blood'),
                    conf.getfloat('player', 'player_mana'),
                    conf.getfloat('player', 'player_attack'),
                    conf.getint('player', 'player_strength'),
                    conf.getint('player', 'player_agile'),
                    conf.getint('player', 'player_intelligence'),
                    conf.getint('player', 'player_physique'),
                    conf.getfloat('player', 'player_criticalChance'),
                    conf.getfloat('player', 'player_skillInjuryRate'),
                    conf.getfloat('player', 'player_defenses'),
                    conf.getfloat('player', 'player_experience'),
                    conf.getint('player', 'player_level'))



if __name__ == "__main__":
    main()
