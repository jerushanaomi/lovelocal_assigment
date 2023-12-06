"""Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = build(nums[:mid])
    root.right = build(nums[mid + 1 :])
    return root


def bfs(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

    return result


def display_tree(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        '''else:
            result.append("null")
            if not any(queue):
                break'''

    return result


nums = list(
    map(int, input("Enter the sorted array elements separated by commas: ").split(","))
)
root = build(nums)
output = display_tree(root)
print("Output:", output)
