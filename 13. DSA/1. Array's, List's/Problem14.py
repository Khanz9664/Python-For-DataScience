#Find the Missing Number in an Array (sequential difference check)
l = [1, 2, 3, 5, 7, 8, 9, 12, 13, 15]

for i in range(0, len(l)-1):
    if l[i+1] != l[i] + 1:
        diff = l[i+1] - l[i]
        for j in range(1, diff):
            print(f"missing number is : {l[i] + j}")
