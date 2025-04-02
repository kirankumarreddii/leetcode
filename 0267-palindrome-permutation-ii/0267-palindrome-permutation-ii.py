class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        frequency=Counter(s)
        halfstring=[]
        count=0
        char_mid=''
        for char,co in frequency.items():
            if co%2==1:
                count+=1
                char_mid=char
            halfstring.extend([char]*(co//2))
        
        if count>1:
            return []

        permut=set(permutations(halfstring))
        generate=[]
        for stng in permut:
            half_string=''.join(stng)
            if char_mid:
                generate.append(half_string+char_mid+ half_string[::-1])
            else:
                 generate.append(half_string+ half_string[::-1])
        return generate