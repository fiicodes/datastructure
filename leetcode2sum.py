# class Solution:
#     def maxProfit(self, prices: list) :
       
#             day_to_buy=prices.index(min(prices))+1
#             day_to_sell=prices.index(max(prices))+1
#             if day_to_sell==1:
#                 prices.pop(0)
#                 #[1,5,3,6,4]
             
#                 day_to_sell=prices.index(max(prices))+2
           
#             if day_to_buy<day_to_sell:
#                 # print('day to buy and sell is {0} and the profit is {1}'.format({day_to_buy,day_to_sell},{prices[day_to_sell-2]-prices[day_to_buy-2]}))
#                 return prices[day_to_sell-2]-prices[day_to_buy-2]

#             else:
#                 return 0
# ob=Solution()
# print(ob.maxProfit( [7,6,4,3,1]))







class Solution:
    def maxProfit(self,price,n) :
        buy=price[0]
        max_profit=0
        for i in range(1,n):
            if buy>price[i]:
                buy=price[i]   
            elif price[i]-buy>max_profit:
                max_profit=price[i]-buy
        return max_profit
ob=Solution()
       
 
prices =[7,6,4,3,1]
n = len(prices)
max_profit =ob.maxProfit(prices, n)
print(max_profit)
print(type(Solution))



# [0,1,2,3]




        