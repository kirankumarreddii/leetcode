class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len=len(s1)
        s2_len=len(s2)
        if s1_len + s2_len != len(s3):
            return False
        dp=[[False]*(s2_len+1) for _ in range(s1_len+1)]
        dp[0][0]=True
        for i in range(1,s1_len+1):
            dp[i][0] = dp[i-1][0] and s1[i - 1] == s3[i - 1]

        for j in range(1,s2_len+1):
            dp[0][j]=(dp[0][j-1] and s2[j-1]==s3[j-1])
        for i in range(1,s1_len+1):
            for j in range(1,s2_len+1):
                dp[i][j] =(dp[i-1][j] and s3[i+j-1]==s1[i-1]) or (dp[i][j-1] and s3[i+j-1]==s2[j-1])      
        return dp[s1_len][s2_len]
# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         s1_len = len(s1)
#         s2_len = len(s2)
        
       
        
#         # DP table initialization
#         dp = [[False] * (s2_len + 1) for _ in range(s1_len + 1)]
#         dp[0][0] = True
        
#         # Initialize first row: Can we match s1's prefix with s3?
#         for i in range(1, s1_len + 1):
#             dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        
#         # Initialize first column: Can we match s2's prefix with s3?
#         for j in range(1, s2_len + 1):
#             dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        
#         # Fill the DP table for all other positions
#         for i in range(1, s1_len + 1):
#             for j in range(1, s2_len + 1):
#                 dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
#                            (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        
#         return dp[s1_len][s2_len]

