class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        high=num/2
        l=2
        while(l<=high):
            mid=(l+high)//2
            if mid*mid==num:
                return True
            elif mid*mid<num:
                l=mid+1
            else:
                high=mid-1
        return False