#Rotate an Array by k steps (manual element-shifting approach)
l = [1, 2, 10, 7, 1, -5, 10, 10]
steps = 2
k = steps
# Cases where steps > len(l)
steps = steps % len(l)

while steps > 0:
    temp = l[len(l)-1]     
    j = len(l)-1
    while j > 0:           
        l[j] = l[j-1]
        j -= 1
    l[0] = temp 
    steps -= 1

print(f"Array after {k} steps : {l}")
