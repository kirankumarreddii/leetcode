class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res=[]
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            decode=''
            for char in word:
                decode+=code[ord(char)-97]
            if decode not in res:
                res.append(decode)
        return len(res)
