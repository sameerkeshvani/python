class py_solution:
    def is_valid_paranthesis(self, str1):
        stack, pchar = [], {"(":")","{":"}","[":"]"}
        for paranthesis in str1:
            if paranthesis in pchar:
                stack.append(paranthesis)
            elif len(stack) == 0 or pchar[stack.pop()] != paranthesis:
                return False
            return len(stack)==0
print(py_solution().is_valid_paranthesis("(){}[]"))
print(py_solution().is_valid_paranthesis("()[{)}"))
print(py_solution().is_valid_paranthesis("()"))