class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Serialize the binary tree
def serialize(root):
    if root is None:
        return "None"

    return (str(root.data) + "," +
            serialize(root.left) + "," +
            serialize(root.right))


# Deserialize the binary tree
def deserialize(data):
    values = iter(data.split(","))

    def build_tree():
        val = next(values)

        if val == "None":
            return None

        node = Node(int(val))
        node.left = build_tree()
        node.right = build_tree()

        return node

    return build_tree()


# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

# Serialize
data = serialize(root)
print("Serialized Tree:", data)

# Deserialize
new_root = deserialize(data)
print("Deserialized Tree Root:", new_root.data)