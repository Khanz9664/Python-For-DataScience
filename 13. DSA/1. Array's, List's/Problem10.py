#Check if an Array is Sorted (Linear scan approach)

def is_sorted(l):
    # For ascending order
    is_ascending = True
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            is_ascending = False
            break
    
    # For descending order
    is_descending = True
    for i in range(len(l)-1):
        if l[i] < l[i+1]:
            is_descending = False
            break
    
  
    if is_ascending or is_descending:
        print("List is sorted")
    else:
        print("List is not sorted")

# Cases
l1 = [-5, 1, 2, 4, 4, 4, 4, 5, 6]  # Sorted in ascending order
l2 = [6, 5, 4, 4, 4, 4, 2, 1, -5]  # Sorted in descending order
l3 = [1, 2, 3, 0]  # Not sorted

is_sorted(l1)  
is_sorted(l2)  
is_sorted(l3)  
