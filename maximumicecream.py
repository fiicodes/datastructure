class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        count=0
        sum=0
        costs.sort()
        for i in costs:
             sum+=i
             count+=1
             if sum==coins:
                return count
             if sum>coins:
                return count-1






s=Solution()
print(s.maxIceCream([1,3,2,4,1],7))


#efficient code

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        costs.sort()
        res = 0
        for price in costs:
            if price<=coins:
                res += 1
                coins -= price
            else:
                break
        return res