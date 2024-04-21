class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        prices.sort()
        if (prices[0] + prices[1]) <= money:
            return (money - (prices[0] + prices[1]))
        else:
            return money
