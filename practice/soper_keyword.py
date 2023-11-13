class Parent:
    def __init__(self,name,roll,gender) -> None:
        self.name=name
        self.roll=roll
        self.gender=gender
        
    def stu(self):
        print("I am ",self.name)
        
        
        
class child(Parent):
    def stu(self):
        print("my roll ",self.roll)
        super().stu()
        
obj=child("souvik",2001106,"M")
obj.stu()
