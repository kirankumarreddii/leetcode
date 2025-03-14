class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        count1=count2=0
        candidate1=candidate2=None
        for num in nums:
            if candidate1==num:
                count1+=1
            elif candidate2==num:
                count2+=1
            elif  count1==0:
                candidate1=num
                count1=1
            elif count2==0:
                candidate2=num
                count2=1
            else:
                count1-=1
                count2-=1

        
        return [num for num in (candidate1,candidate2) if nums.count(num)>len(nums)//3]
