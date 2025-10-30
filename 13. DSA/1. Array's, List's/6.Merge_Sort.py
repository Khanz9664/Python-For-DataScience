l = [9,1,2,5,-5,-1,0,9,10,3,2,5]

def merge_sort(l):
    if len(l) == 1 or len(l) == 0:
        return l
    else:
        mid = len(l)//2
        left_sub = l[:mid]
        right_sub = l[mid:]
        return merge(merge_sort(left_sub), merge_sort(right_sub))

def merge(left_sub,right_sub):
    l_temp = []
    i = 0
    j = 0
    
    while i < len(left_sub) and j < len(right_sub):
        if left_sub[i] > right_sub[j]:
            l_temp.append(right_sub[j])
            j = j+1
        elif left_sub[i] < right_sub[j]:
            l_temp.append(left_sub[i])
            i = i+1
        else:
            l_temp.append(left_sub[i])
            l_temp.append(right_sub[j])
            i = i+1
            j = j+1
    
    if len(left_sub) > 0:
        l_temp.extend(left_sub[i:])
    if len(right_sub) > 0:
        l_temp.extend(right_sub[j:])
    
    return l_temp

l[:] = merge_sort(l)
print(l)
