class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        sell=buy+1
        max_profit=0
        while sell<=len(prices)-1:
            if prices[buy]<prices[sell]:
                profit = prices[sell]-prices[buy]
                max_profit = max_profit+profit
                buy=sell
            else:
                buy=sell
            sell+=1
        return max_profit