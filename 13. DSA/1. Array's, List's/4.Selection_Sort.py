l = [1,2,5,7,8,0,9,10,3,2,5]

for i in range(len(l)):
    smallest = l[i]
    k = i
    for j in range(i, len(l)):
        if l[j] < smallest:
            smallest = l[j]
            k = j
    l[i], l[k] = l[k], l[i]
print(l)
