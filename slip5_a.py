class string:
    def get_String(self):
        self.s = input("Enter a string")
    def print_String(self):
        print("Entered String is\n",self.s.upper())
s = string()
s.get_String()
s.print_String()