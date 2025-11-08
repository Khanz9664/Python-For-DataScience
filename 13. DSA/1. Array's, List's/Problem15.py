#Find the Common Elements in Two Arrays (brute-force approach)
l1 = [1, 2, 4, 11, 17, 10]
l2 = [3, 5, 6, 11, 10]
for i in l1:
    for j in l2:
        if i == j:
            print(f"Common Element in both lists: {i}")
