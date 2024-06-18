class rectangle():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        self.a=self.l*self.b
        print("Area of rectangle:",self.a)
    def perimeter(self):
        self.p=2*(self.l+self.b)
        print("Perimeter of rectangle:",self.p)
r=rectangle(5,10)
r.area()
r.perimeter()