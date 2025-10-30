l = [9, 1, 2, 2, 2, 5, -100, 10, 90,-20,10,-100, 12]

def quick_sort(l):
    if len(l) <= 1:
        return l
    
    pivot = l[len(l)//2]
    left_sub = []
    right_sub = []
    pivot_sub = []
    
    for i in range(len(l)):
        if l[i] < pivot: 
            left_sub.append(l[i])
        elif l[i] > pivot:
            right_sub.append(l[i])
        else:
            pivot_sub.append(l[i])
    
    return quick_sort(left_sub) + pivot_sub + quick_sort(right_sub)

l[:] = quick_sort(l)

print(l)
