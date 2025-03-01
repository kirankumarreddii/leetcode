class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # heights_sort=sorted(heights)
        # return sum(1 for i in range(heights) if heights[i]!=heights_sort[i])
        return sum(a != b for a, b in zip(heights, sorted(heights)))