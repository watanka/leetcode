class Solution:
    def maxProfit(self, prices: List[int]) -> int :
        # input : prices = List[int]
        # pick buydate, selldate 
        # prices[selldate] - prices[buydate] = profit
        # max(profit) 
        # buydate < selldate

        # [7, 1, 5, 3, 6, 4]  maxVal = 7
        # 7, maxVal 6 -1
        # 1, maxVal 6 5
        # maxVal

        # maxVal = 7
        # buydate = 0, # buyprice = 7 maxVal = 6
        # answer = max(0, 6 - 7) = 0
        # buydate = 1, buyprice = 1, maxVal = 6
        # answer max(0, 5) = 5
        # ...

        # maxVal = 7
        # buydate = 0 # buyprice = 7 maxVal = 6
        # answer = max(0, 6 -7) = -1
        # ...

        
        # buy = 항상 최소값. sell = buy 후에 위치하고, 항상 최대값이 되야함
        buydate, selldate = 0, 1
        maxprofit = 0

        while selldate < len(prices) :
            if prices[buydate] < prices[selldate] :
                maxprofit = max(maxprofit, prices[selldate] - prices[buydate])
            else :
                buydate = selldate

            selldate += 1

        return maxprofit





