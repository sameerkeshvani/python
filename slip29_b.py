import operator
d={1:2,3:4,4:3,2:1,0:0,'one':1,'three':3,'five':5,'two':2,'four':4}
s=sorted(d.items(),key=operator.itemgetter(1))
print(f"Ascending order {s}")
sr = sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print("Descending order",sr)