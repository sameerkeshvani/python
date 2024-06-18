class string:
    def get_string(self):
        self.s = input("Enter a string")
    def print_string(self):
        print("Upper String:",self.s.upper())
    def reverse_string(self):
        self.str =""
        for self.i in self.s:
            self.str = self.i + self.str
        print("Reversed in lower string:",self.str.lower())
s = string()
s.get_string()
s.print_string()
s.reverse_string()