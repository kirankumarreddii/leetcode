class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_bits=[]
        pd=max_=0
        for word in words:
            mask=0
            for ch in word:
                mask |=1<<(ord(ch)-ord('a'))
            word_bits.append((mask,len(word)))
        for i in range(len(word_bits)):
            for j in range(i+1,len(word_bits)):
                if word_bits[i][0] & word_bits[j][0]==0:
                    pd=word_bits[i][1]*word_bits[j][1]
                max_=max(pd,max_)
        return max_