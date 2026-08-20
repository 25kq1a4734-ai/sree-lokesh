class product:
    def __init__(self,pname,price,stock):
        self.pname=pname
        self.price=price
        self.stock=stock
    def displaydetails(self):
        print(self.__dict__)
class electronics(product):
    def __init__(self,pname,price,stock,warranty):
        super().__init__(pname,price,stock)
        self.warranty=warranty
TV=electronics("sony",50000,10,10)
TV .displaydetails()



class clothes(product):
    def __init__(self,pname,price,stock,size):
        super().__init__(pname,price,stock)
        self.size=size
cloth=clothes("raymond",2000,1,"L")
cloth.displaydetails()
