# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return
        queue=[]
        average=[]
        queue.append(root)
        while(len(queue)>0):
            qlen=len(queue)
            list1=[]
            for i in range((qlen)):
                node=queue.pop(0)
                if node:
                    list1.append(node.val)

                    queue.append(node.left)
                    queue.append(node.right)
            if list1:
                average.append(sum(list1)/len(list1))
        return average



