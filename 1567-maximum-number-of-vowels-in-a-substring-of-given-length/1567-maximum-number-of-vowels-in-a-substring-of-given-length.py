class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','i','e','o','u'}
        count=max_lenth=0

        for i in range(len(s)):
            if s[i] in vowels:
                count+=1
            if i>=k and s[i-k] in vowels:
                count-=1
            max_lenth=max(max_lenth,count)
        return max_lenth