class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxi=0
        while left<right:
            mini=min(height[left],height[right])
            result=mini*(right-left)
            maxi=max(maxi,result)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxi
