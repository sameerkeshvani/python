tpl = (1,2,2)
tpl2 = []
tpl3 = {}
count = 0
count1 = 1
for te in range(len(tpl)):
    if tpl[te] not in tpl2:
        count += 1
        tpl2.append(tpl[te])
    else:
        count1 += 1
        tpl3.update({tpl[te]:count1})
print(len(tpl2))
print(tpl3)