from Model.LoadConfig import LoadConfig
class Backpack():
    def openBackpack(self):
        backpack = []
        backpack = LoadConfig.LoadConfigbackpack(backpack)
        return backpack

    def appendBackpack(backpack,equip):
        backpack.append(equip)
        return backpack

    def delBackpack(backpack,equip):
        backpack.remove(equip)
        return backpack
