class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <2:
            return 0
        else:
            buyinPrice = prices[0]
            res = 0
            for i in range(1, len(prices)):
                temp = prices[i] - buyinPrice
                if temp > res:
                    res = temp
                if prices[i] < buyinPrice:
                    buyinPrice = prices[i]
            return res
