class resturant:
    def bill(self,*items):
        total=0
        for i in items:
            total=total+i
        print("total bill:",total)
customer1=resturant()
customer1.bill(100)
customer2=resturant()
customer2.bill(100,200)
customer3=resturant()
customer3.bill(100,826,5487)
customer4=resturant()
customer4.bill(100,48,20,453)
customer5=resturant()
customer5.bill()
