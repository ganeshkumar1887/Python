class students:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    def dis(self):
        print("Name = ",self.name)
        print("Age =",self.age)
class s1(students):
    def __init__(self, name,age,rollno, marks):
        super().__init__(name, age)
        self.rollno = rollno
        self.marks = marks
    def dis(self):
        super().dis()
        print("Roll no = ",self.rollno)
        print("Marks = ",self.marks)
s=s1("Ganesh",22,101,99)
s.dis()

        