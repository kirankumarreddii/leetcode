class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        same = image[sr][sc]
        r, c = len(image), len(image[0])
        
        # If the starting pixel already has the target color, no need to proceed
        if same == color:
            return image

        def paint(i,j):
            if i<0 or i>=r or j<0 or j>=c or image[i][j]!= same:
                return
            image[i][j]=color
            paint(i+1,j)
            paint(i-1,j)
            paint(i,j+1)
            paint(i,j-1)



        paint(sr,sc)
        return image
