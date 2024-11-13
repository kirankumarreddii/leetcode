class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dist={idx:i for i,idx in enumerate(nums2)}

        for idx,num in enumerate(nums1):
            if num in dist:

                nums1[idx]=dist[num]
        return nums1
    #     for idx, num in enumerate(nums1):
    #     # Use the value `num` to look up the index in the dictionary `dist`
    #     if num in dist:
    #         nums1[idx] = dist[num]
    
    # return nums1