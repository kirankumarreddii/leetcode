class Solution:
    def wiggleSort(self, num: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(num)-1):
            if i%2==0 and num[i]>num[i+1]:
                 num[i],num[i+1]= num[i+1],num[i]
            elif i%2==1 and num[i]<num[i+1]:
                num[i],num[i+1]= num[i+1],num[i]
