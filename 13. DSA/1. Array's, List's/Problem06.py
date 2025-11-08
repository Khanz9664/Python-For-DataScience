#Delete an Element by Value (manual in-place deletion by value.)
l = [1,2,10,7,1,-5,10,2]
element = 10
n = len(l)

for i in range(n):
    if l[i] == element:
        for j in range(i, n-1):
            l[j] = l[j+1]
        l[n-1] = None 
        #break #use this to delete only first occurance
print(l)
