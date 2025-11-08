#Insert an Element at a Specific Position without replacing the current element (in-place insertion by shifting elements)
l = [1,2,0,7,1,-5,10,2]
position = 3
element = 100
for i in range(0, len(l)):
    if i == position:
        l = l + [None]
        j = len(l)-1
        while j >= i:
            l[j] = l[j-1]
            j = j-1
        l[position] = element
print(l)
