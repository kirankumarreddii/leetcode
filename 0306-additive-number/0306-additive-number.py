class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n=len(num)
        for i in range(1,n):
            for j in range(i+1,n):
                num1=num[:i]
                num2=num[i:j]

                if (len(num1)>1 and num1[0]=='0') or (len(num2)>1 and num2[0]=='0'):
                    continue
                while j<n:
                    sum1=str(int(num1)+int(num2))
                    if not num.startswith(sum1,j):
                        break
                    j+=len(sum1)

                    num1, num2 = num2, sum1
                if j==n:
                    return True
        return False
                