import collections
string = "thequickbrownfoxjumpsoverthelazydog"
d = collections.defaultdict(int)
#defaultdict provides a default value to value in key-value pair and int defaultvalue is 0
for c in string:
    d[c] += 1
#sorted(dictionary,keys, True for descending)
for c in sorted(d, key=d.get, reverse=True):
    if d[c]>1:
        print("%s = %d" %(c, d[c]))