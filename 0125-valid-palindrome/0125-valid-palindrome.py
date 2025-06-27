class Solution:
    def isPalindrome(self, s: str) -> bool:
    #     s=''.join(char.lower() for char in s if char.isalnum())
    #     # filtered_str = ''.join([char.lower() for char in s if char.isalnum()])
    #     l=0
    #     r=len(s)-1
    #     if s == " ":
    #         return False
    #     # while(l<r):
    #     #     if s[l] != s[r]:
    #     #         return False
               
    #     #     r-=1
    #     #     l+=1
    #     # return True
    #     return s==s[::-1]

        left=0
        right=len(s)-1
        while left<=right:
            while left<right and not s[left].isalnum():
                left+=1
            while left<right and not s[right].isalnum():
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
            
        return True

        