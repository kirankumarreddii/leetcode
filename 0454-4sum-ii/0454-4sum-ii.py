class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        AB_Sum={}
        for a in nums1:
            for b in nums2:
                s=a+b
                if s in AB_Sum:
                    AB_Sum[s]+=1
                else:
                     AB_Sum[s]=1
        count=0
        for a in nums3:
            for b in nums4:
                count+=AB_Sum.get(-(a+b),0)
        return count
