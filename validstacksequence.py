class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        p=0
        stack=[]
        for i in pushed:
            stack.append(i)
            while p<len(popped) and stack and stack[-1]==popped[p]:
                stack.pop()
                p+=1
        return True if not stack else False

