class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count0=0
        # count1=0
        # count2=0
        # n=len(nums)
        # for i in range(n):
        #     if nums[i]==0:
        #         count0+=1
        #     elif nums[i]==1:
        #         count1+=1
        #     else:
        #         count2+=1
        # for i in range(0,count0):
        #     # print(i)
        #     nums[i]=0
        # for i in range(count0,count1+count0):
        #     print(i)
        #     nums[i]=1
        # for i in range(count1+count0,n):
        #     print(i)
        #     nums[i]=2
        low,mid,high=0,0,len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                mid+=1
                low+=1
            elif nums[mid]==2:
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1
            else:
                mid+=1

