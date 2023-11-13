class A:
    def __init__(self,val1) -> None:
        self.val1=val1
        
    def getval1(self):
        print(self.val1)
        
class B(A):
    def __init__(self, val1,val2) -> None:
        super().__init__(val1)
        self.val2=val2
        
    def getval(self):
        print(self.val2)
        
obj=B(100,500)
obj.getval()
obj.getval1()
