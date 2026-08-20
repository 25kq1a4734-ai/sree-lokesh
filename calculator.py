class div:
   def division(self,a,b):
       return a/b
class moddiv:
    def division(self,a,b):
        return a%b
class floordiv:
    def division(self,a,b):
        return a//b
class calculator(floordiv,moddiv,div):
    pass
c1=calculator()
print(c1.division(25,5))
