class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.key, end=" ")
        printInorder(root.right)


arr = list(map(int, input("Enter N positive integers separated by space: ").split()))

root = None

for value in arr:
    root = insert(root, value)

print("Inorder Traversal of BST:")
printInorder(root)
