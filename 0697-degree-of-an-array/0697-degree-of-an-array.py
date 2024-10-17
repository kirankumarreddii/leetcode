class Solution:
    # def findShortestSubArray(self, nums: List[int]) -> int:
    #     def call(key):
    #         left=0
    #         right=len(nums)-1
    #         li=0
    #         while nums[left]!=key:
    #             left+=1
    #         while nums[right]!=key:
    #             right-=1
    #         return right-left+1     
    #     dist={}
    #     for n in nums:
    #         if n not in dist:
    #             dist[n]=1
    #         else:
    #             dist[n]+=1
    #     degree = max(dist.values())
    #     length=float('inf')
    #     for key,val in dist.items():
    #         if val==degree:
    #             fun=call(key)
    #             length=min(fun,length)
    #     return length
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = {}
        max_freq = 0
        first_occurance = {}
        l = len(nums)

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
                first_occurance[nums[i]] = i
            else:
                freq[nums[i]]+=1

            if freq[nums[i]]>max_freq:
                max_freq = freq[nums[i]]
                min_sub_length = i - first_occurance[nums[i]]+1
            elif freq[nums[i]]==max_freq:
                min_sub_length = min(min_sub_length, i - first_occurance[nums[i]]+1)

        return min_sub_length