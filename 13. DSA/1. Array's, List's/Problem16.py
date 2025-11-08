#Rearrange Array Alternating Positive and Negative
l = [1, 2, 3, -3, 4, -1, -2, -4, -7, 7, -8, -9, -10]
positive = []
negative = []
for i in l:
    if i >= 0:
        positive.append(i)
    else:
        negative.append(i)

if len(positive) < len(negative):
    n = len(positive)
    m = len(negative)
else:
    n = len(negative)
    m = len(positive)

j = 0
temp = []
while j<n :
    temp.append(positive[j])
    temp.append(negative[j])
    j = j+1
if m == len(negative):
    for k in range(j, m):
        temp.append(negative[k])
else:
    for k in range(j, m):
        temp.append(positive[k])  

print(temp)
