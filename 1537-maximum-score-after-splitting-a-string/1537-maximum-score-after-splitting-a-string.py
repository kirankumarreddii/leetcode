class Solution:
    def maxScore(self, s: str) -> int:
        count_1=0
        count_0=0
        score=0
        for num in s:
            if num=='1':
                count_1+=1
        for i in range(len(s)-1):
            if s[i]=='0':
                count_0+=1
            else:
                count_1-=1
            score=max(score,count_0+count_1)
        count_1+count_1
        return score
