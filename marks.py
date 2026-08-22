class student:
    def __init__(self,marks):
        self.marks=marks
    def __gt__(self,other):
        if self.marks>other.marks:
            print("true")
        else:
            print("false")
s1=student(97)
s2=student(100)
s1>s2
