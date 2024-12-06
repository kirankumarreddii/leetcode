class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff=float('INF')
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            while l<r:
                three=nums[i]+nums[r]+nums[l]
                print(three)
                if three==target:
                    return three
                if abs(diff-target)>abs(target-three):
                        diff=three
                if three>target:
                    r-=1
                else:
                    l+=1
        return diff