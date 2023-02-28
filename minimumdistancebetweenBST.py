# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
      flattened=[]

      def inOrder(root):
        if not root:
          return
        inOrder(root.left)
        flattened.append(root.val)
        inOrder(root.right)
      inOrder(root)
      ans=float("inf")
      for i in range(1,len(flattened)):
            ans=min(ans,flattened[i]-flattened[i-1])
      return ans



