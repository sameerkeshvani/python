def tuple_int(tuple_str):
    inttuple = tuple((int(x[0]),(int(x[1]))) for x in tuple_str)
    return inttuple
tuple_str = (('333','33'),('1416','55'))
print("Original Values:")
print(tuple_str)
print(tuple_int(tuple_str))