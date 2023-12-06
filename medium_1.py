'''Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”'''
class tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_bst(nums):
    if not nums or nums[0].lower() == "null":
        return None

    root = tree(int(nums[0]))
    queue = [root]
    i = 1

    while queue and i < len(nums):
        current = queue.pop(0)

        left_val = nums[i]
        i += 1
        if left_val.lower() != "null":
            current.left = tree(int(left_val))
            queue.append(current.left)

        if i < len(nums):
            right_val = nums[i]
            i += 1
            if right_val.lower() != "null":
                current.right = tree(int(right_val))
                queue.append(current.right)

    return root

def find_lca(root, p, q):
    if not root:
        return None

    if p.val < root.val and q.val < root.val:
        return find_lca(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return find_lca(root.right, p, q)
    else:
        return root

bst_elements = [val.strip() for val in input("Enter the elements of the binary search tree separated by commas (use 'null' for empty nodes): ").split(",")]

bst_root = build_bst(bst_elements)

p_val = int(input("Enter the value of node p: "))
q_val = int(input("Enter the value of node q: "))

p = tree(p_val)
q = tree(q_val)

lca_node = find_lca(bst_root, p, q)

if lca_node:
    print(f"The lowest common ancestor of nodes {p_val} and {q_val} is: {lca_node.val}")
else:
    print("Nodes not found in the BST.")
