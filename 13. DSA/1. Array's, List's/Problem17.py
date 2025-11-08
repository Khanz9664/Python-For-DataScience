#Subarray with Given Sum (Sliding Window)
l = [1, 2, 1, 11, 17, 10]
summ = 14
n = len(l)
found = False
for i in range(len(l)):
    s = 0
    sub = []
    j = i
    while j < len(l):
        s += l[j]
        sub.append(l[j])
        while s > summ:
            s = s-sub[0]
            sub.pop(0)
        if s == summ:
            found = True
            break
        j = j+1
    if found:
        break

print(f"sub-array with sum {summ} is {sub}")
