class bankacc:
    def __init__(self,accnum,name,pin):
        self._accnum=accnum
        self.name=name
        self.__pin=pin
    def getpin(self):
        return self.__pin
    def setpin(self,oldpin,newpin):
        if self.__pin==oldpin:
            self.__pin=newpin
            print("PIN changed successfully")
        else:
            print("incorrect PIN entered")
    def display(self):
        print(self._accnum)
        print(self.name)
b1=bankacc(1202030,"lokesh",1234)
b1.display()
print(b1.getpin())
b1.setpin(1234,6789)
print(b1.getpin())
print(b1._bankacc__pin)
