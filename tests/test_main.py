from CombatSystem.combat import Combat
from Model.player import Player
from Model.monster import Monster
from Model.LoadConfig import LoadConfig
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
    player = LoadConfig.LoadConfigPlayer('player')
    print(player.blood)
    players = [player]
    monster = LoadConfig.LoadConfigMonster('monster_lv1')
    monsters = [monster]
    # combatSystem = Combat
    # combatSystem.Combat(players, monsters)


if __name__ == "__main__":
    main()
