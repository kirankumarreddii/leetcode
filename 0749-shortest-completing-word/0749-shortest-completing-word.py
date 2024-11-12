class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        st=''.join([char.lower() for char in licensePlate if char.isalpha()])
        count_st=Counter(st)
        result=None
        for word in words:
            word_count=Counter(word.lower())

            if all(word_count[char]>=count_st[char] for char in count_st):
                if result is None or len(result)>len(word):
                    result=word
        return result

                

