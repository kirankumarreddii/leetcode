class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        ranks=[]
        count=0
        dist={}
        sort_list=sorted(set(arr))
        for i in range(len(sort_list)):
            count+=1
            dist[sort_list[i]]=count
        return [dist[num] for num in arr]