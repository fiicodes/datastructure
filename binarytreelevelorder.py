class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder( root ) -> list[list[int]]:
        if root is None:
            return
        res=[]



        queue=[]
        queue.append(root)
        while queue:
            qlen=len(queue)
            level=[]
            for i in range(qlen):


                node=queue.pop(0)
                if node:
                    level.append(node.val)

                    queue.append(node.left)

                    queue.append(node.right)
            if level:
                res.append(level)
        return res

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print(levelOrder(root))