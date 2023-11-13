class A:
    def __init__(self) -> None:
        self.val1=100
        
    def dis1(self):
        print(self.val1)
        
class B(A):
    def dis2(self,val1):
        print(self.val1)
        
const=B()
const.dis2(10)