l = [5,7,8,9,10,3,2,5]
e = 2
for i in range(len(l)):
    if l[i] == e:
        print(f"element {e} found at index {i}")
        break
else:
    print(f"Element {e} not found")
