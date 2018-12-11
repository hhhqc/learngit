from CombatSystem.combat import Combat
from Model.player import Player
from Model.monster import Monster
from Model.LoadConfig import LoadConfig
from Model.Equip import Equip
from config import *
import random
import os
import configparser
from Backpack.backpack import Backpack

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
        equipid = Equip.getEquipid(1)
        equipid = 'equip_' +str(equipid)
        equip = LoadConfig.LoadConfigEquip(equipid)
        print('物品掉落:')
        if(equip.id!=0):
            print(equip.name+":"+equip.quality)
        else:
            print('无')
        print(player.experience)
        print(player.level)
        while(True):
            print('-------------------------------')
            print('1.继续战斗 2.打开背包 5.退出战斗')
            type = input('请输入指令:')
            if(type == '5'):
                return
            elif(type=='2'):
                equipids = []
                backpack = Backpack.openBackpack(1)
                for equipid in backpack:
                    if equipid!='':
                        equipids.append('equip_' + equipid)
                equips = LoadConfig.LoadConfigEquips(equipids)
                for equip in equips:
                    print('装备ID:' + equip.id + ' 装备名字:' + equip.name)

                getequipid = input('请输入要查看装备的ID:')
                getequipid = ['equip_' + str(getequipid)]
                equip = LoadConfig.LoadConfigEquip(getequipid)
                equip.printequip()
            elif(type=='1'):
                break


    # backpack = Backpack.delBackpack(backpack,'1')
    # print(backpack)
    #
    # backpack = Backpack.openBackpack(1)
    # print(backpack)




if __name__ == "__main__":
    main()
