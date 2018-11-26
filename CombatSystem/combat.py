from time import sleep
from CombatSystem.hp import HP
class Combat():
    #战斗信息
    def CombatInformation(attackers,defender,attackmode,damage):
        mode = attackmode
        attackersName = attackers.name
        defenderName = defender.name
        return print(attackersName+'用'+mode+'对'+defenderName+'造成'+str(damage)+'伤害')

    def Combat(player,monster):
        #战斗
        while True:
            monster.blood = monster.blood - player.attack
            Combat.CombatInformation(player,monster,'攻击',player.attack)
            HP.getHP(monster)
            if(monster.blood<=0):
                break
            sleep(0.3)

            player.blood = player.blood - monster.attack
            Combat.CombatInformation(monster, player, '攻击', monster.attack)
            HP.getHP(player)
            if(player.blood<=0):
                break
            sleep(0.3)

