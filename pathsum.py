# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # base case if root does not exist return False
        if root is None:
            return False

        # decrease the root val from the targetSum
        targetSum -= root.val

        # check if target sum is 0 and current node is leaf then return True
        if (targetSum == 0) and (root.left is None and root.right is None):
            return True

        # call the funtion resursively on left and right
        left = self.hasPathSum(root.left,targetSum)
        right = self.hasPathSum(root.right,targetSum)

        # return left or right that is if either of them is true return True
        return left or right