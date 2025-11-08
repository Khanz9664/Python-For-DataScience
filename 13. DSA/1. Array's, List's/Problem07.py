#Delete an Element at a Specific Index (manual element-shifting approach)
l = [1,2,10,7,1,-5,10,2]
element_at = 3
n = len(l)

for i in range(n):
    if i == element_at:
        for j in range(i, n-1):
            l[j] = l[j+1]
        l[n-1] = None
        
print(l)
