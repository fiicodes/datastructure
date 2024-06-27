class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        result = []
        for i in nums:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)

        for a, b in zip(pos, neg):
            result.append(a)
            result.append(b)
        return result
