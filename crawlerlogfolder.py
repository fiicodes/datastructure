class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count_stack = []
        for l in logs:
            if l == "../":
                if count_stack:
                    count_stack.pop()
            elif l != "./":
                count_stack.append(log)
        return len(count_stack)








