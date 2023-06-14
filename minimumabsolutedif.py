class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDiffInBST(root: TreeNode) -> int:
    prev = None
    min_diff = float('inf')

    def inorder(node: TreeNode):
        nonlocal prev, min_diff
        if node is None:
            return
        inorder(node.left)
        if prev is not None:
            min_diff = min(min_diff, abs(node.val - prev.val))
        prev = node
        inorder(node.right)

    inorder(root)
    return min_diff
