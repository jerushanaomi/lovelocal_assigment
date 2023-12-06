'''Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.'''
from collections import Counter

def occurring(nums):
    n = len(nums)
    div = n // 3
    counter = Counter(nums)
    res = [x for x in counter if counter[x] > div]
    return res

nums = list(map(int, input("Enter the array elements separated by commas: ").split(',')))
result = occurring(nums)
print(f"The elements that appear more than ⌊ n/3 ⌋ times are: {result}")

