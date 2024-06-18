import operator
d = {1:50, 2:40, 3:30, 4:20, 5:10}
d = sorted(d.items(), key=operator.itemgetter(1),reverse=True)
print(d)