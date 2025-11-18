#given an integer array nums return an array answer such that answer[i] is equal to 
#product of all numbers in nums except nums[i]
nums = [2,4,5,7]
answer = []

for i in range(len(nums)):
    product = 1
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            product = product * nums[j]
    answer.append(product)

print(answer)
