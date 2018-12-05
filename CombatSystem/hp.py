
class HP():
    def getHP(Model):
        if(Model.blood <= 0):
            print(Model.name + "剩余" + str(0) + '点hp')
            print('战斗结束')
            return
        return print(Model.name + "剩余" + str(Model.blood) + '点hp')
