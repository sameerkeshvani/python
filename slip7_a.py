class complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return self.a + other.a, self.b + other.b
c1=complex(10,20)
c2=complex(20,30)
c3=c1+c2
print(c3)