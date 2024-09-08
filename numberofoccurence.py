# User function Template for python3
class Solution:

    def count(self, arr, n, x):
        def findtarget(arr, x, first):
            l = 0
            h = len(arr) - 1
            res = -1
            while (l <= h):
                mid = (l + h) // 2
                if arr[mid] == x:
                    res = mid
                    if first:
                        h = mid - 1
                    else:
                        l = mid + 1
                elif arr[mid] < x:
                    l = mid + 1
                else:
                    h = mid - 1
            return res

        firstoccurence = findtarget(arr, x, True)
        if firstoccurence == -1:
            return 0
        secondoccurence = findtarget(arr, x, False)
        count = secondoccurence - firstoccurence + 1
        return count
