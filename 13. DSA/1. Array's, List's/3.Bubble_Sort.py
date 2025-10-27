l = [0,1,2,5,7,8,9,10,3,2,5]
n = len(l)
for i in range(n):
    for j in range(0, n - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]  

print(l)
