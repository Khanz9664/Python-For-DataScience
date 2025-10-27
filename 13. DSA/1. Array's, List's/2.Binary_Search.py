l = [5,7,8,9,10,3,2,5]
e = 10
l.sort() #sorting list using list method
print(f"sorted list : {l}")
low = 0
high = len(l) - 1
while low<=high:
    mid = (low + high) // 2
    if l[mid]==e:
        print(f"Element {e} found at index {mid}")
        break
    elif l[mid]<e:
        low = mid + 1
    else:
        high = mid - 1
else:
    print(f"Element {e} not found")
