#Find the Largest and Second Largest Elements (single-pass linear scan)
l = [1,2,10,7,1,-5,10,10]
largest = float("-inf")
largest_2nd = float("-inf")
for i in l:
    if i > largest:
        largest_2nd = largest
        largest = i
    elif i > largest_2nd and i < largest:
        largest_2nd = i
print(f"largest : {largest}")
print(f"2nd largest : {largest_2nd}")       
