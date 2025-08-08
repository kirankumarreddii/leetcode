class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        str1_count=[0]*26
        str2_count=[0]*26
        for i in range(len(s1)):
            str1_count[ord(s1[i])-ord('a')]+=1
            str2_count[ord(s2[i])-ord('a')]+=1
        if str1_count==str2_count:
            return True
        for i in range(len(s1),len(s2)):
            str2_count[ord(s2[i])-ord('a')]+=1

            str2_count[ord(s2[i-len(s1)])-ord('a')]-=1
            if str1_count==str2_count:
                return True
        return False