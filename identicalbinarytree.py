


class Solution:

    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
def isSameTree( p,  q) -> bool:
      if p is None and q is None:
        return True
      if p  is not None and q is not None:
        return(p.val==q.val) and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
      else:
        return False

root1 = Solution(1)
root2 = Solution(1)
root1.left = Solution(2)
root1.right = Solution(3)
root1.left.left = Solution(4)
root1.left.right = Solution(5)

root2.left = Solution(2)
root2.right = Solution(3)
root2.left.left = Solution(4)
root2.left.right = Solution(5)

# Function call
if __name__ == "__main__":
  if isSameTree(root1, root2):
      print("Both trees are identical")
  else:
      print("Trees are not identical")