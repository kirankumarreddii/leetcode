class Solution:
    def betterCompression(self, compressed: str) -> str:
        char={}
        n=len(compressed)
        i=0
        j=n-1
        while i<n:
            if compressed[i].isalpha():
                s=compressed[i]
                i+=1
                count=0
                while i < n and compressed[i].isdigit():
                    count=count*10+int(compressed[i])
                    i+=1
            char[s]=char.get(s,0)+count
        return ''.join(ch+str(char[ch]) for ch in sorted(char))