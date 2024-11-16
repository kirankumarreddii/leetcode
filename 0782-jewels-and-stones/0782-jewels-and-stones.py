class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dst={char: stones.count(char)   for char in stones}
        res=0

        for char in jewels:
            if char in dst:
                res+=dst[char]

        return res