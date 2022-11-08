class Solution:
     def isValid(self, expr: str) -> bool:
        stack=[]
        closetoopen={")":"(",
        "]":"[",
        "}":"{"}
        for i in expr:
            if i in closetoopen:
                if stack and stack[-1]==closetoopen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

o=Solution()
print(o.isValid("[{}}]"))