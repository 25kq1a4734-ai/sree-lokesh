class student:
    def marks(self,*subjects):
        total=0
        for i in subjects:
            total=total+i
        print("total marks:",total)
student1=student()
student1.marks(35)
student2=student()
student2.marks(75,56,28)
student3=student()
student3.marks(38,78,56,65)
student4=student()
student4.marks(36,98)
student5=student()
student5.marks(87,72,45)
