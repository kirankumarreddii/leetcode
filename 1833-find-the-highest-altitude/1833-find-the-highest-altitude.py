class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_lenth=0
        s=0
        for num in gain:
            s+=num
            max_lenth=max(max_lenth,s)
        return max_lenth
