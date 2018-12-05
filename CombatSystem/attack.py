from CombatSystem import combat
from CombatSystem import hp

from time import sleep


class Acttack():
    def getActtack(self, Model):
        return Model.attack

    def AttackMonomer(attacker, defender):
        damage = attacker.attack - defender.defenses
        if(damage >= 0):
            defender.blood = - damage
        else:
            defender.blood = -1
        combat.Combat.CombatInformation(attacker, defender, '攻击', damage)
        hp.HP.getHP(defender)
        sleep(0.3)

    def AttackAll(attacker, defenders):
        for defender in defenders:
            defender.blood = defender.blood - attacker.attack
            combat.Combat.CombatInformation(
                attacker, defender, '攻击', attacker.attack)
            hp.HP.getHP(defender)
            sleep(0.3)
