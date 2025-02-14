class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1=set(nums1)
        num2=set(nums2)
        res1=[]
        res2=[]
        for num in num1:
            if num not in num2:
                res2.append(num)
        
        for num in num2:
            if num not in num1:
                res1.append(num)
        return [res2,res1]