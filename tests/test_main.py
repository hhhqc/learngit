from CombatSystem.combat import Combat
from Model.player import Player
from Model.monster import Monster
from Model.LoadConfig import LoadConfig
from config import *
import random
import os
import configparser


def main():

    player = LoadConfig.LoadConfigPlayer('player')
    while(True):
        chance = random.randint(1, 10)
        if(chance > 9):
            monster = LoadConfig.LoadConfigMonster('monster_lv2')
        else:
            monster = LoadConfig.LoadConfigMonster('monster_lv1')
        print(player.name + '遭遇' + monster.name)
        print('开始战斗')
        combatSystem = Combat
        combatSystem.Combat(player, monster)
        if(player.blood <= 0):
            break
        if(monster.blood<=0):
            player.experience = monster.exe
        print(player.experience)
        print(player.level)
        print('-------------------------------')
        print('1.继续战斗 2.退出战斗')
        type = input('请输入指令:')
        if(type == '2'):
            break


if __name__ == "__main__":
    main()
