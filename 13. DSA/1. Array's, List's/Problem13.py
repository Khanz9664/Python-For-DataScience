# Move Zeros to the End (manual in-place shifting approach)
l = [1, 0, 10, 0, 7, -5, 13, 12, 11]
n = len(l)
i = 0
while i<n:
    if l[i] == 0:
        temp = l[i]
        for j in range(i, n-1):
            l[j] = l[j+1]
        l[n-1] = temp
        n = n-1
    else:
        i = i+1
print(l)
