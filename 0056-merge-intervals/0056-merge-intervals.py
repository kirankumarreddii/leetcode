class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        prev_start,prev_end=intervals[0]
        merge=[]
        for init in intervals:
            start,end=init
            if start<=prev_end:
                prev_end=max(prev_end,end)
            else:
                merge.append([prev_start,prev_end])
                prev_start,prev_end=start,end
        merge.append([prev_start,prev_end])
        return merge


