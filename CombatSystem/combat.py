from time import sleep
from CombatSystem.hp import HP
from CombatSystem.attack import Acttack


class Combat():
    # 战斗信息
    def CombatInformation(attacker, defender, attackmode, damage):
        mode = attackmode
        attackersName = attacker.name
        defenderName = defender.name
        return print(
            attackersName +
            '用' +
            mode +
            '对' +
            defenderName +
            '造成' +
            str(damage) +
            '伤害')

    def Combat(player, monster):
        plaSpeed = player.speed
        monSpeed = monster.speed
        # 战斗
        while True:
            if(plaSpeed >= monSpeed):
                print("1.普通攻击 2.选择技能 3.使用道具 4.逃跑")
                instruction = input("请输入指令:")
                if instruction == '1':
                    Acttack.AttackMonomer(player, monster)
                    if(Combat.IsDeath(monster)):
                        break
                elif instruction == '2':
                    print("1.普通攻击")
                    skill = input("请选择技能:")
                    if skill == '1':
                        Acttack.AttackMonomer(player, monster)
                        flag = Combat.IsDeath(monster)
                        if (flag):
                            break

                Acttack.AttackMonomer(monster, player)
                if (Combat.IsDeath(player)):
                    break
            else:
                Acttack.AttackMonomer(monster, player)
                if (Combat.IsDeath(player)):
                    break

                print("1.普通攻击 2.选择技能 3.使用道具 4.逃跑")
                instruction = input("请输入指令:")
                if instruction == '1':
                    Acttack.AttackMonomer(player, monster)
                    if (Combat.IsDeath(monster)):
                        break
                elif instruction == '2':
                    print("1.普通攻击")
                    skill = input("请选择技能:")
                    if skill == '1':
                        Acttack.AttackMonomer(player, monster)
                        if (Combat.IsDeath(monster)):
                            break

    def IsDeath(defender):
        if defender.blood <= 0:
            return True
        else:
            return False
