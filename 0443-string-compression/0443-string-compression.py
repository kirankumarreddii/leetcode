class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)<2:
            return len(chars)
        read=0
        write=0
        while read<len(chars):
            character=chars[read]

            count=0
            while read<len(chars) and chars[read]==character:
                read+=1
                count+=1
            chars[write]=character
            write+=1
            if count>1:
                for s in str(count):
                    chars[write]=s
                    write+=1
        return write