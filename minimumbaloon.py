class Solution:
    def findMinArrowShots(self, points:list[list[int]]) -> int:
        points.sort(key=lambda x:x[1])
        res,curEnd=1,points[0][1]
        for start,end in points:
            if curEnd<start:
                res+=1
                curEnd=end
        return res

o=Solution()
print(o.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
