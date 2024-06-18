class calculator():
    def calculation(self,a,b):
        self.a=a
        self.b=b
        print("Addition:",a+b)
        print("Substraction:",a-b)
        print("Multiplication:",a*b)
        print("Division:",a/b)
c = calculator()
c.calculation(10,5)