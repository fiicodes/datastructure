# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def isleafnode(self,root):
            if not root:
                return False
            else:
                if  not root.left and not root.right:
                    return True
                return False



    def sumOfLeftLeaves(self, root) -> int:
            res=0
            if root is not None:
                if self.isleafnode(root.left):
                    res+=root.left.val
                else:
                    res+=self.sumOfLeftLeaves(root.left)
                res+=self.sumOfLeftLeaves(root.right)
            return res








