# Find the Longest Subarray with Sum Zero
l = [1, -1, 1, 11, 17, -28, 10]
n = len(l)

s_summ = {}      # dictionary to store prefix_sum -> first index
s_sum = 0        # running (prefix) sum
max_len = 0      # length of longest subarray
start_index = -1 # to store where that subarray starts

for i in range(n):
    s_sum = s_sum + l[i]

    # Case 1: subarray from start to current index has sum 0
    if s_sum == 0:
        max_len = i + 1
        start_index = 0

    # Case 2: prefix sum seen before
    elif s_sum in s_summ:
        prev_index = s_summ[s_sum]
        current_len = i - prev_index
        if current_len > max_len:
            max_len = current_len
            start_index = prev_index + 1

    # Case 3: first time we see this prefix sum → store it
    else:
        s_summ[s_sum] = i

# Extract subarray using indices
if max_len > 0:
    subarray = l[start_index : start_index + max_len]
    print(f"Longest subarray with sum 0 is {subarray}")
else:
    print("No subarray with sum 0 found.")
