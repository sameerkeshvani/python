def merged_list(list1, list2):
    mergelist = [(list1[i],list2[i]) for i in range(len(list1))]
    print(mergelist)
list1 = [1,2,3]
list2 = ['a','b','c']
merged_list(list1, list2)