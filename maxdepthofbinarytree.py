# Definition for a binary tree TreeNode.
#using DFS
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root) -> int:
#         if root is None:
#             return 0
#         return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# ob=Solution()
# print(ob.maxDepth(root))

#Using BFS
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth( root) -> int:
        if   root is None :
            return 0
        level=0
        queue=[]
        queue.append(root)

        while queue:


            for i in range(len(queue)):
                node=queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:

                    queue.append(node.right)
            level+=1

        return level

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(maxDepth(root))
