# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def bfs(root):
            res=[]
            if not root:
                return
            res.append(root.val)
            self.dfs(root.left)
            self.dfs(root.right)
            return res
        l=0
        r=len(self.res)-1
        while(l<=r):
            val=self.res[l]+self.res[r]
            if val<k:
                l+=1
            elif val>k:
                r-=1
            else:
                return True
            return False
        







