class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            # Step 1: Flip the row by reversing it
            row.reverse()
            
            # Step 2: Invert the row by replacing 1 with 0 and 0 with 1
            for i in range(len(row)):
                row[i] = 1 - row[i]
                
        return image