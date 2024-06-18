class student:
    def __init__(self, rollno, name, age, gender):
        self.rollno = rollno
        self.name = name
        self.age = age
        self.gender = gender
class test(student):
    def __init__(self, rollno, name, age, gender, m1, m2, m3):
        student.__init__(self, rollno, name, age, gender)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def display(self):
        self.total = self.m1+self.m2+self.m3
        print(self.rollno,self.name,self.age,self.gender,self.total)
t1 = test(11,"Sameer","20","Male",20,20,20)
t1.display()
t2 = test(12,"Sahil","20","Male",10,12,21)
t2.display()
t3 = test(13,"Sunny","20","Male",12,12,23)
t3.display()