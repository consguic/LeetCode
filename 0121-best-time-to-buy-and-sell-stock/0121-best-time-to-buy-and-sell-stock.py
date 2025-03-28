class Solution(object):
    def maxProfit(self, prices):
        min_price = 10e5
        max_profit = 0
        for i in prices:
            if  min_price > i:
                min_price = i
            if  max_profit < i-min_price :
                max_profit = i-min_price
        return max_profit
        