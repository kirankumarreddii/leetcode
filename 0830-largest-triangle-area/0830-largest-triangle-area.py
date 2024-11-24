class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area=0
        def com(p1,p2,p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

        for p1,p2,p3 in combinations(points,3):
            area=com(p1,p2,p3)
            max_area=max(area,max_area)
        return max_area