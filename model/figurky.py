class Figurka:
    def __init__(self, barva, typ):
        self.__barva = barva
        self._typ = typ
        self._vektory = None


    def getsmery(self):
        return self._vektory

    def getbarva(self):
        return self.__barva

    def gettyp(self):
        return self._typ