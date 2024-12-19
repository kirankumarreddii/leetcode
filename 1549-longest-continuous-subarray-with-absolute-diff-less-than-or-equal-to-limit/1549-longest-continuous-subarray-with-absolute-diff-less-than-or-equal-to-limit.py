class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start=0
        minDeque=deque([])
        maxDeque=deque([])
        maxlen=0
        for end in range(len(nums)):
            while maxDeque and nums[maxDeque[-1]]<nums[end]:
                maxDeque.pop()
            while minDeque and nums[minDeque[-1]]>nums[end]:
                minDeque.pop()
            maxDeque.append(end)
            minDeque.append(end)
            if nums[maxDeque[0]]-nums[minDeque[0]]>limit:
                start+=1
                if maxDeque[0]<start:
                    maxDeque.popleft()
                if minDeque[0]<start:
                    minDeque.popleft()
            maxlen=max(maxlen,end-start+1)
        return maxlen
 