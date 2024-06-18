def bubble_sort(list2):
    for i in range(len(list2)-1):
        for j in range(len(list2)-1):
            if(list2[j+1]<list2[j]):
                temp = list2[j]
                list2[j] = list2[j+1]
                list2[j+1] = temp
    print(list2)
list1 = input("Enter the list of numbers").split()
list2 = [int(x) for x in list1]
print(list2)
bubble_sort(list2)