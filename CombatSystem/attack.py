from CombatSystem import combat
from CombatSystem import hp

from time import sleep
class Acttack():
    def getActtack(self,Model):
        return Model.attack

    def AttackMonomer(attacker, defender):
            defender.blood =  - attacker.attack
            combat.Combat.CombatInformation(attacker, defender, '攻击', attacker.attack)
            hp.HP.getHP(defender)
            sleep(0.3)

    def AttackAll(attacker, defenders):
        for defender in defenders:
            defender.blood = defender.blood - attacker.attack
            combat.Combat.CombatInformation(attacker, defender, '攻击', attacker.attack)
            hp.HP.getHP(defender)
            sleep(0.3)


