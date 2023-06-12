class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = prices[0]
        profit = 0
        for i in range(1, len(prices)) :
            if x > prices[i] :
                x = prices[i]
            else :
                profit += prices[i] - x
                x = prices[i]

        return profit