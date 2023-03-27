class Solution():
    def  checkIsFibonacci(self,arr, n) :

        if (n == 1 or n == 2) :
            return True
        arr.sort()
        for i in range(2,n):
            if arr[i-1]+arr[i-2]!=arr[i]:
                return False
        return True
obj=Solution()
print(obj.checkIsFibonacci([ 2, 3, 5, 11 ],4))



