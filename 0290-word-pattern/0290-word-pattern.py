class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        hash1={}
        # hash2={}
        if len(words)!=len(pattern):
            return False
        if len(set(words))!= len(set(pattern)):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in hash1:
                if hash1[pattern[i]]!=words[i]:
                    return False
            else:
                hash1[pattern[i]]=words[i]
            # if words[i] in hash2:
            #     if hash2[words[i]]!=pattern[i]:
            #         return False
            # else:
            #     hash2[words[i]]=pattern[i]

        return True

                