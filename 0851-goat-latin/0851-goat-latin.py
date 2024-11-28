class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        sent=''
        lst=sentence.split()
        for i, word in enumerate(lst):
            if word[0].lower() in vowels:
                sent+=word+'ma'+'a'*(i+1)
            else:
                sent+=word[1:]+word[0]+'ma'+'a'*(i+1)
            if i!=len(lst)-1:
                sent+=' '

            
        return sent
        
            
