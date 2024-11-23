class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        currenct_width=0
        lines=1
        for char in s:
            
            char_width=widths[ord(char)-97]
            if currenct_width+char_width>100:
                lines+=1
                currenct_width=char_width
            else:
                currenct_width+=char_width
        return [lines,currenct_width]
                
        

            
        