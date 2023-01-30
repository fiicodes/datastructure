class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        ans=[]
        for i in  range(1,n+1):
            if (i%3==0) and (i%5==0):
              
                ans.append("FizzBuzz")
                continue
            if i%3==0 :
                ans.append("Fizz")
                continue
            if i%5==0 :
                ans.append("Buzz")
                continue

            ans.append(i)
        return ans

o=Solution()
print(o.fizzBuzz(16))