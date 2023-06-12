from typing import List

def findMissingRanges(nums: List[int]) -> List[str]:
    result = []
    n = len(nums)
    i = 0

    while i < n:
        start = nums[i]
        end = start

        # Find the end of the consecutive range
        while i < n - 1 and nums[i+1] == nums[i] + 1:
            i += 1
            end = nums[i]

        if start != end:
            result.append(f"{start}->{end}")
        else:
            result.append(str(start))

        i += 1

    return result
