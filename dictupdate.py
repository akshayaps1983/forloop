dict={1:"she",2:"tom",3:"girl"}
dict.update({4:"boy"})
print(dict)
dict[5]="I"
print(dict)
dict.pop(1)
print(dict)
dict.popitem()#pop the last item
print(dict)
del dict[2]
print(dict)
dict.clear()
print(dict)