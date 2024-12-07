class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }


        def track(index,com):
            if len(com)==len(digits):
                res.append(com)
                return
            for letter in phone_map[digits[index]]:
                track(index+1,com+letter)
        if digits:
            track(0,'')
        return res