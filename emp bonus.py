class employee:
    def salary(self,basic,bonus=0):
        print(basic+bonus)
e1=employee()
e1.salary(100000)
e2=employee()
e2.salary(150000,50000)
