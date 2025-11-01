# Reverse the list
l = [1,2,0,7,1,-5,10,2]
i = 0
j = len(l)-1
while i <= (len(l)-1)//2 and i<j:
    l[i],l[j] = l[j],l[i]
    i = i+1
    j = j-1
print(f"reversed list: {l}")
