from collections import Counter
class Solution:

    def longestArithSeqLength(self, nums: list[int]) -> int:
        diff=[]
        for i in range(len(nums)-1):
            diff.append(nums[i+1]-nums[i])
        for d in diff:

            counter = Counter(diff)
            most_common = counter.most_common(1)
            if most_common:
                d, count = most_common[0]
                return count+1
            else:
                return 0












ob=Solution()
print(ob.longestArithSeqLength([3,6,9,12]))