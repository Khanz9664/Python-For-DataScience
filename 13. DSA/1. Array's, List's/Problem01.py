# Find Minimum and Maximum
l = [1,2,0,7,1,-5,10]
mini = float('inf')
maxi = float('-inf')
for i in l:
    if i < mini:
        mini = i
    if i > maxi:
        maxi = i
print(f"minimum : {mini}")
print(f"maximum : {maxi}")
