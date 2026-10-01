class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,root,key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left,key)
        else:
            root.right = self.insert(root.right,key)

        return root

    def search(self,root,key):
        if root is None:
            return False

        if root.key == key:
            return True

        if key < root.key:
            return self.search(root.left,key)
        else:
            return self.search(root.right,key)

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.key,end = " ")
            self.inorder(root.right)
            


bst = BST()
values = [50, 30, 20, 40, 70, 60, 80]

for value in values:
    bst.root = bst.insert(bst.root, value)

print("Inorder Traversal of BST: ")
bst.inorder(bst.root)


print("\nSearch 40:", "Found" if bst.search(bst.root, 40) else "Not Found")
print("Search 100:", "Found" if bst.search(bst.root, 100) else "Not Found")
