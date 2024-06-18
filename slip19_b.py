class shape():
    def __init__(self):
        pass
class square(shape):
    def __init__(self,l):
        self.l = l
    def area(self):
        self.a = self.l*self.l
        print("Area of square:",self.a)
    def volume(self):
        self.v = self.l*self.l*self.l
        print("Volume of square:",self.v)
class circle(shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        self.a = 3.14*self.r*self.r
        print("Area of circle:",self.a)
    def volume(self):
        self.v = (4/3)*3.14*(self.r*self.r*self.r)
        print("Volume of circle:",self.v)
s = square(5)
s.area()
s.volume()
c = circle(10)
c.area()
c.volume()