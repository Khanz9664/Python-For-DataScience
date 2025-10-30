l = [9,1,2,5,7,8,0,9,10,3,2,5]

for i in range(len(l)):
    key = l[i]
    j = i-1
    while j >= 0 and l[j] > key:
        l[j+1] = l[j]
        j=j-1
    l[j+1] = key
            
print(l)
