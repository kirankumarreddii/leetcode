# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         s1_len=len(s1)
#         s2_len=len(s2)
#         if s1_len + s2_len != len(s3):
#             return False
#         dp=[[False]*(s2_len+1) for _ in range(s1_len+1)]
#         dp[0][0]=True
#         for i in range(1,s1_len+1):
#             dp[i][0] = dp[i-1][0] and s1[i - 1] == s3[i - 1]

#         for j in range(1,s2_len+1):
#             dp[0][j]=(dp[0][j-1] and s2[j-1]==s3[j-1])
#         for i in range(1,s1_len+1):
#             for j in range(1,s2_len+1):
#                 dp[i][j] =(dp[i-1][j] and s3[i+j-1]==s1[i-1]) or (dp[i][j-1] and s3[i+j-1]==s2[j-1])      
#         return dp[s1_len][s2_len]
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len + s2_len != len(s3):
            return False
        
        dp = [[False] * (s1_len + 1) for _ in range(s2_len + 1)]
        dp[0][0] = True  # Base case: both s1 and s2 are empty, s3 should be empty too.
        
        for i in range(1,s1_len+1):
            if s1[i-1]==s3[i-1] and dp[0][i-1]:
                dp[0][i]=True
        
        for j in range(1,s2_len+1):
            if s2[j-1]==s3[j-1] and dp[j-1][0]:
                dp[j][0]=True
        
        # Fill the dp table for the rest of the cases.
        for i in range(1, s1_len + 1):
            for j in range(1, s2_len + 1):
                dp[j][i] = (s3[i + j - 1] == s1[i - 1] and dp[j][i - 1]) or (s3[i + j - 1] == s2[j - 1] and dp[j - 1][i])
        
        return dp[s2_len][s1_len]
