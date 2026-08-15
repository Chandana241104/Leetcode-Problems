class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_buy_price=prices[0]
        max_sell_price=0
        for i in range(n):
            if prices[i]<min_buy_price:
                min_buy_price=prices[i]
            curr_profit=prices[i]-min_buy_price
            if curr_profit>max_sell_price:
                max_sell_price=curr_profit
        return max_sell_price
        