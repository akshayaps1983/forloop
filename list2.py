list1 = ['a','b','c','d']
list2 = ['e','f','g']
list3 = ['h','i','j']
list4 = list1
list4.append('100')
print(list1)
print(list2)
list5 = list1.copy()
list5.append('200')
print(list5)
print(list1)