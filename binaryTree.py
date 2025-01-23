class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None 
        self.size = 0

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            self.size += 1
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    self.size += 1
                    return
                else:
                    current = current.left 
            else: 
                if current.right is None:
                    current.right = TreeNode(value)
                    self.size += 1
                    return
                else:
                    current = current.right 

    def inorder(self, node): 
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

    def preorder(self,node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)