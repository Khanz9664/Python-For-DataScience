#Find the First and Last Occurrence of an Element (linear scan approach)
l = [1,2,10,1,1,1,7,1,-5,10,2]
element = 1
n = len(l)
first = -1
last = -1

for i in range(n):
    if l[i] == element:
        if first == -1:
            first = i
        else:
            last = i
if first > -1:
    print(f"element {element} first found at index {first}")
if last > -1:
    print(f"element {element} last found at index {last}")

