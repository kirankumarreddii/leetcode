class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        def compare(x,y):
            if x+y>y+x:
                return -1
            elif x+y<y+x:
                return 1
            else:
                return 0
        nums.sort(key=cmp_to_key(compare))
        
        return str(int("".join(nums)))