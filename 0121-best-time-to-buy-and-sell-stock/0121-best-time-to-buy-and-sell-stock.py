class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxi = 0
        # for i in range(len(prices)-1):
        #     j = i+1
        #     while j<len(prices):
        #       if prices[j] - prices[i] > maxi:
        #         maxi = prices[j]-prices[i]
        #       j+=1
        # return maxi
        Max_profit =0
        Min_val = prices[0]
        for i in range(1,len(prices)):
            if Max_profit < prices[i] -  Min_val:
                Max_profit = prices[i]-Min_val
            if Min_val > prices[i]:
                Min_val = prices[i]
        return Max_profit

