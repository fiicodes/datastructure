class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        stack = []
        for i in range(0, len(intervals)):
            if stack and stack[0][1] >= intervals[i][0]:
                stack[0][1] = max(stack[0][1], intervals[i][1])
            else:
                stack.insert(0, intervals[i])
        return stack
