class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p,a=0,0
        left=0
        right=1
        while(right<len(prices)):
            if prices[left] < prices[right]:
                max_p=max(prices[right] - prices[left],max_p)
            else:
                left=right
            right+=1
        return max_p

        