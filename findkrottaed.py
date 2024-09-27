class Solution:
    def findKRotation(self, arr):
        l = 0
        h = len(arr) - 1
        if arr[l] <= arr[h]:
            return l
        while (l <= h):
            mid = (l + h) // 2
            if mid > 0:
                if arr[mid] < arr[mid - 1]:
                    return mid
            if mid < len(arr) - 1:
                if arr[mid] > arr[mid + 1]:
                    return mid + 1
            if arr[mid] >= arr[l]:
                l = mid + 1
            else:

                h = mid - 1


