class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices)<2:
            return 0
        Sum=0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                Sum+=prices[i+1]-prices[i]
        return Sum
