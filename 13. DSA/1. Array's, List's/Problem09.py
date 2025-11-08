#Find the Frequency of an Element (linear scan / counting approach)
l = [1,2,10,7,1,-5,10,2]
element = 2
n = len(l)
count = 0
for i in range(n):
    if l[i] == element:
        count = count+1
if count > 0:
    print(f"element {element} occurs {count} times")
else:
    print((f"element {element} doesn't exist"))
