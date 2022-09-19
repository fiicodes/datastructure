class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visited_no=dict()
        for index,num in enumerate(nums):
            no_to_search=target-num
            if no_to_search in visited_no:
                return(index,visited_no[no_to_search])
            else:
                visited_no[num]=index
s=Solution()
print(s.twoSum(nums = [3,2,4], target = 6))