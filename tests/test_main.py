from CombatSystem.combat import Combat
from Model.player import Player
from Model.npc import NPC


def main():
    print("战斗开始")
    player = Player('player',100,10,10,2,1)
    print(player.attackMax)
    # players = [player]
    # npc = NPC('npc',100,40)
    # npcs = [npc]

    # combatSystem = Combat
    # combatSystem.Combat(players, npcs)


if __name__ == "__main__":
    main()
