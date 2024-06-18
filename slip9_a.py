class string:
    def get_string(self):
        self.s = input("Enter a string")
    def reverse_string(self):
        self.str =""
        for self.i in self.s:
            self.str = self.i + self.str
        print("Reversed:",self.str)
s = string()
s.get_string()
s.reverse_string()