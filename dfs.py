class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key
def printpreorder(root):
        if root:
            print(root.value)
            printpreorder(root.left)

            printpreorder(root.right)

def printinorder(root):
        if root:
            printinorder(root.left)
            print(root.value)
            printinorder(root.right)

def printpostorder(root):
        if root:
            printpostorder(root.left)
            printpostorder(root.right)
            print(root.value)

root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left  = Node(4)
root.left.right  = Node(5)
print ("Preorder traversal of binary tree is")
printpreorder(root)

print( "\nInorder traversal of binary tree is")
printinorder(root)

print ("\nPostorder traversal of binary tree is")
printpostorder(root)