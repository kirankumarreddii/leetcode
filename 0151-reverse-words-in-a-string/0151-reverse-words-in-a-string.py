class Solution:
    def reverseWords(self, s: str) -> str:
        # res=[]
        # l=0
        # word=""
        # while l<len(s):
        #     if s[l]!=' ':
        #         while l<len(s) and s[l]!=' ':
        #             word+=s[l]
        #             l+=1
        #         res.append(word)
        #         word=""
        #     l+=1
        # return " ".join(res[::-1])
        res = []
        l = 0
        
        while l < len(s):
            if s[l] != ' ':
                word = []  # Use a list to build the word
                while l < len(s) and s[l] != ' ':
                    word.append(s[l])
                    l += 1
                res.append("".join(word))  # Convert list to string and add to res
            else:
                l += 1
        
        return " ".join(res[::-1])
