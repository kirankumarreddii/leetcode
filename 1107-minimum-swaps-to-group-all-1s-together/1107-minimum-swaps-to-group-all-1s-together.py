class Solution:
    def minSwaps(self, data: List[int]) -> int:
        count=data.count(1)
        swaps=sum(1 for i in range(count) if data[i]==0)
        min_swap=swaps
        for i in range(count,len(data)):
            if data[i]==0:
                swaps+=1
            if data[i-count]==0:
                swaps-=1

            min_swap=min(min_swap,swaps)
        return min_swap