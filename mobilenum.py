class mobile:
    def calling(self,mobilenumber,countrycode=0):
        if countrycode!=0:
            print("calling:",mobilenumber,"+",countrycode)
        else:
            print("calling:",mobilenumber)
m1=mobile()
m1.calling(9505523589,+91)
m2=mobile()
m2.calling(9866542763)
