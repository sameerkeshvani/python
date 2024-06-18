class rectangle():
    def __init__(self,l,b):
        self.a = 2*(l+b)
        print("Area:",self.a)
    def perimeter(self,l,b):
        self.p = l*b
        print("\nPerimeter:",self.p)
r = rectangle(5,5)
r.perimeter(5,5)