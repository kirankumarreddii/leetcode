class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        res=[0]*(len(num1)+len(num2))
        nums1=num1[::-1]
        nums2=num2[::-1]

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                res[i+j]+=int(nums1[i])*int(nums2[j])
                res[i+j+1]+=res[i+j]//10
                res[i+j]%=10

        while len(res)>1 and res[-1]==0:
            res.pop()

        return ''.join(map(str,res[::-1]))

        

