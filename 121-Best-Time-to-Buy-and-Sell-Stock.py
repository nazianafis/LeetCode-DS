class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l == 0:
            return 0
        max_profit, low = 0, prices[0]
        for i in range(1, l):
            if low > prices[i]:
                low = prices[i]
            else:
                temp = prices[i] - low
                if temp > max_profit:
                    max_profit = temp
        return max_profit
