class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findTarget(nums, target, first):
            l = 0
            h = len(nums) - 1
            result = -1
            while (l <= h):
                mid = (l + h) // 2

                if nums[mid] == target:
                    result = mid
                    if first:

                        h = mid - 1

                    else:

                        l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    h = mid - 1
            return result

        firstoccur = findTarget(nums, target, True)
        if firstoccur == -1:
            return [-1, -1]
        secondoccur = findTarget(nums, target, False)
        return [firstoccur, secondoccur]


