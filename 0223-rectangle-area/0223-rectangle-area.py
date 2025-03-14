class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1=(ax2-ax1)*(ay2-ay1)
        area2=(bx2-bx1)*(by2-by1)
        overlap_h=max(min(bx2,ax2)-max(ax1,bx1),0)
        overlap_w=max(min(ay2,by2)-max(ay1,by1),0)
        overlap_a=overlap_w*overlap_h
        return area1+area2-overlap_a