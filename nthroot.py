#User function Template for python3

class Solution:
 def NthRoot(self, n, m):

    # Code here
    l = 1
    h = m
    while (l <= h):
        mid = (l + h) // 2
        if mid ** n < m:
            l = mid + 1
        elif mid ** n > m:
            h = mid - 1
        else:
            return mid
    return -1

