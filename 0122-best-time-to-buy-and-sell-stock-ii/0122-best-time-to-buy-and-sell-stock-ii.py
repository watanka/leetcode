class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_hold, cur_not_hold = -float('inf'), 0

        for stock_price in prices :

            prev_hold, prev_not_hold = cur_hold, cur_not_hold

            cur_hold = max(prev_hold, prev_not_hold - stock_price)
            cur_not_hold = max(prev_not_hold, prev_hold + stock_price)

        return cur_not_hold