class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1] )
        deletcolumn=0
        curEnd=intervals[0][1]
        for start,end in intervals[1:]:
            if  start>=curEnd:
              curEnd=end
            else:
                deletcolumn+=1
        return deletcolumn



s=Solution()
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))

