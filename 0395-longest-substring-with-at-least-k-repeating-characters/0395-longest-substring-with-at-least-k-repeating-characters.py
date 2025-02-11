class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s or len(s)<k:
            return 0
        freq={ch: s.count(ch) for ch in set(s)}

        for i in range(len(s)):
            if freq[s[i]]<k:
                left=self.longestSubstring(s[:i],k)
                right=self.longestSubstring(s[i+1:],k)
                return max(left,right)
        return len(s)