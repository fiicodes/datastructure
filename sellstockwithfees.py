class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy=prices[0]+fee
        profit=0
        for i in range(1,len(prices)):
           if  prices[i]>buy:
              buy=prices[i]
              profit+=prices[i]-buy
           elif  buy>prices[i]+fee:
                buy=prices[i]+fee
        return profit






class Solution:
    # Time O(n) Space O(1)
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0                              # profit so far
        buy = prices[0] + fee                   # buy price
        for i in range(1, len(prices)):
            if prices[i] > buy:                 # can have profit if we sell today
                profit += prices[i] - buy       # - add the profit
                buy = prices[i]                 # - set new buy price
            elif prices[i] + fee < buy:         # last buy was a mistake, could have bought at this lower price today
                buy = prices[i] + fee           # - set new buy price
        return profit