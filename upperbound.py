class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        arr.sort()
    
        l,h=0,len(arr)-1
        flo=-1 if x<arr[0] else arr[0]
        ceil=-1 if x>arr[h] else arr[h]
        
        while l<=h:
            m=(l+h)//2
            if arr[m]==x:
                #flo,ceil=x,x
                ceil=min(ceil,arr[m])
                flo=max(flo,arr[m])
                return (flo,ceil)
            elif arr[m]>x:
                ceil=min(ceil,arr[m])
                h=m-1
            else:
                flo=max(flo,arr[m])
                l=m+1
        return(flo,ceil)
