class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        index = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    index.append((i, j))
                else:
                    continue

        return len(index)
