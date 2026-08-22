class bankacc:
    def __init__(self,bal):
        self.bal=bal
    def __add__(self,other):
        return self.bal+other.bal
b1=bankacc(50000)
b2=bankacc(50000)
print(b1+b2)
