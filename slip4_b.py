class employee:
    def accept(self,mid,name,dept,sal):
        self.mid=mid
        self.name=name
        self.dept=dept
        self.sal=sal
    def display(self):
        print("Member Id:",self.mid,"\nName:",self.name,"\nDepartment:",self.dept,"\nSalary:",self.sal)
class manager(employee):
    def accept(self,mid,name,dept,sal,bonus):
        employee.accept(self,mid,name,dept,sal)
        self.bonus=bonus
    def display(self):
        self.total=self.sal+self.bonus
        employee.display(self)
        print("Bonus:",self.bonus,"\nTotal Salary:",self.total)
m = manager()
m.accept(1,"Sameer","CA",100000,5000)
m.display()