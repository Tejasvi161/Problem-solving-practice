class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    if root is None:
        return None

    if root.data == p or root.data == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


# Create binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

p = 4
q = 5

result = lowest_common_ancestor(root, p, q)

print("Lowest Common Ancestor:", result.data)