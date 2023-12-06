'''You are given an array of integers nums, there is a sliding window of size k 
which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.
from collections import deque
Return the max sliding window'''
from collections import deque
def max_sliding_window(nums, k):
    result = []
    window = deque()

    for i, num in enumerate(nums):
        while window and window[0] < i - k + 1:
            window.popleft()
        while window and nums[window[-1]] < num:
            window.pop()
        window.append(i)
        if i >= k - 1:
            result.append(nums[window[0]])
    return result

nums = list(map(int, input("Enter the array elements separated by commas: ").split(',')))
k = int(input("Enter the window size: "))
result = max_sliding_window(nums, k)
print("The max sliding window is:", result)
