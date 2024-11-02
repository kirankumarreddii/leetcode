class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if ord(i)>ord(target):
                return i
            elif i==target:
                continue
        return letters[0]