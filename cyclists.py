import createXML

class Cyclist:

    def __init__(self, v=0, x=0):
        self.v = v
        self.x = x

    def getCoordinate(self):
        return self.x

    def getSpeed(self):
        return self.v

    def setCoordinate(self, x):
        self.x = x

    def setSpeed(self, v):
        self.v = v

    def setNewXinTime(self, t, flag):
        if flag:
            self.x = self.x - self.v * t
        else:
            self.x = self.x + self.v * t