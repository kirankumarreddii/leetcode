class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aieou")
        count=0
        max_lenth=0
        for i in range(k):
            if s[i] in vowels:
                count+=1
            max_lenth=max(max_lenth,count)
        for i in range(k,len(s)):
            if s[i] in vowels:
                count+=1
            if s[i-k] in vowels:
                count-=1
            max_lenth=max(max_lenth,count)
        return max_lenth