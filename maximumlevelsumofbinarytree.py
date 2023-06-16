# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxLevelSum(self,root):
        if not root:
            return 0

        maxSum = float('-inf')
        maxLevel = 0
        level = 1
        queue = deque([root])

        while queue:
            levelSum = 0
            levelSize = len(queue)

            for _ in range(levelSize):
                node = queue.popleft()
                levelSum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if levelSum > maxSum:
                maxSum = levelSum
                maxLevel = level

            level += 1

        return maxLevel

        