from CombatSystem.combat import Combat
from Model.player import Player
from Model.npc import NPC


def main():
    print("战斗开始")
    player = Player('player',100,25)
    npc = NPC('npc',100,40)
    combatSystem = Combat
    combatSystem.Combat(player, npc)


if __name__ == "__main__":
    main()
