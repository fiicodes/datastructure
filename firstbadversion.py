class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r=1,n
        result=1
        while(l<=r):
            mid=(l+r)//2
            if isBadVersion(mid)==False:
                l=mid+1
            else:
                r=mid-1
                result=mid
        return result

