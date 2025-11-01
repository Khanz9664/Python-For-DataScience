#Insert an Element at a Specific Position replacing the current element
l = [1,2,0,7,1,-5,10,2]
position = 3
element = 100
for i in range(0, len(l)):
    if i == 3:
        l[3] = element
print(l)
