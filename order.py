class user:
    def __init__(self,uname,pno):
        self.uname=uname
        self.pno=pno
    def displaydetails(self):
        print(self.__dict__)
class customer(user):
    def __init__(self,uname,pno,delv_add):
         super().__init__(uname,pno)
         self.delv_add=delv_add
    def place_order(self):
        print("order placed successfully")
c1=customer("LOKESH",9505523589,"rudravaram")
c1.displaydetails()
c1 .place_order()
class premium_customer(customer):
    def __init__(self,uname,pno,delv_add,mem_type):
        super().__init__(uname,pno,delv_add)
        self.mem_type=mem_type
    def apply_discount(self):
        print("premium discount applied")
pre_cus=premium_customer("LOKESH",9505523589,"AMERICA","diamound")
pre_cus.displaydetails()
pre_cus.apply_discount()
