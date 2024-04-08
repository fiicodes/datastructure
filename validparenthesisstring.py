class Solution:
    def checkValidString(self, s: str) -> bool:
        o_stack = []
        s_stack = []

        for index, char in enumerate(s):
            if char == '(':
                o_stack.append(index)
            elif char == ')':
                if o_stack:
                    o_stack.pop()
                elif s_stack:
                    s_stack.pop()
                else:
                    return False
            else:
                s_stack.append(index)

        while o_stack and s_stack:
            if o_stack.pop() > s_stack.pop():
                return False

        return not o_stack