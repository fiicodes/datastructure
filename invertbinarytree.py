class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree( root):
        if not root:
            return None
        temp=root.left
        root.left=root.right
        root.right=temp
        invertTree(root.left)
        invertTree(root.right)
        return root

root = TreeNode(4)
root.left = TreeNode(7)
root.right = TreeNode(2)
root.left.left = TreeNode(9)
root.left.right = TreeNode(6)
root.right.left = TreeNode(3)
root.right.right = TreeNode(1)
print(invertTree(root))