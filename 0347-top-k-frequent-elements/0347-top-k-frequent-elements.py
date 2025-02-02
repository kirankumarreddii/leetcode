class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq={i:0 for i in set(nums)}
        # for num in nums:
        #     freq[num]+=1
        # freq={num: nums.count(num) for num in set(nums)}
        freq=Counter(nums)
        min_heap=[]
        for num,count in freq.items():
            heapq.heappush(min_heap,(count,num))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return [num for _,num in min_heap]

