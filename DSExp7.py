class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def getHeight(self, node):
        if node is None:
            return 0
        return node.height

    def getBalance(self, node):
        if node is None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rightRotate(self, y):
        x = y.left
        temp = x.right

        x.right = y
        y.left = temp

        y.height = 1 + max(
            self.getHeight(y.left),
            self.getHeight(y.right)
        )

        x.height = 1 + max(
            self.getHeight(x.left),
            self.getHeight(x.right)
        )

        return x

    def leftRotate(self, x):
        y = x.right
        temp = y.left

        y.left = x
        x.right = temp

        x.height = 1 + max(
            self.getHeight(x.left),
            self.getHeight(x.right)
        )

        y.height = 1 + max(
            self.getHeight(y.left),
            self.getHeight(y.right)
        )

        return y

    def insert(self, root, key):

        if root is None:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(
            self.getHeight(root.left),
            self.getHeight(root.right)
        )

        balance = self.getBalance(root)

        # LL Case
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)

        # RR Case
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)

        # LR Case
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # RL Case
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.key, end=" ")
            self.inorderTraversal(root.right)


avl = AVLTree()

values = [20, 15, 30, 10, 25, 50]

root = None

for value in values:
    root = avl.insert(root, value)

print("Inorder Traversal of Balanced AVL Tree:")
avl.inorderTraversal(root)
