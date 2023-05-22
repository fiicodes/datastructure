class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedheight=sorted(heights)
        count=0
        for i in range(len(heights)):
            if heights[i]!=sortedheight[i]:
                count+=1
        return count


        