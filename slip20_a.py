class circle():
    def __init__(self,r):
        self.r=r
    def area(self):
        self.a = 3.14*self.r*self.r
        print("Area of circle:",self.a)
    def circumference(self):
        self.c = 2*3.14*self.r
        print("Circumference of circle:",self.c)
c = circle(10)
c.area()
c.circumference()