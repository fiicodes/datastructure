# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root) -> list[int]:
      def dfs(node):

        if not node: return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)


        return 
      res=[]
      dfs(root)
      return res


root = TreeNode(1)

root.right     = TreeNode(2)

root.right.left     = TreeNode(3)
print(preorderTraversal(root))
