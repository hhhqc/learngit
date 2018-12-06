from Model.LoadConfig import LoadConfig
class Backpack():
    def openBackpack(backpack):
        backpack = LoadConfig.LoadConfigbackpack(backpack)
        return backpack

    def appendBackpack(backpack,equip):
        backpack = LoadConfig.LoadConfigbackpack(backpack)
        backpack.append(equip)
        return backpack

    def delBackpack(backpack,equip):
        backpack = LoadConfig.LoadConfigbackpack(backpack)
        backpack.remove(equip)
        return backpack
