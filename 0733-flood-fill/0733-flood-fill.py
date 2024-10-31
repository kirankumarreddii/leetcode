class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        same = image[sr][sc]
        r, c = len(image), len(image[0])
        stack=[(sr,sc)]
        # If the starting pixel already has the target color, no need to proceed
        if same == color:
            return image

        while stack:
            i,j=stack.pop()
            if 0<=i<r and 0<=j<c and image[i][j]==same:
                image[i][j]=color
                stack.append((i+1,j))
                stack.append((i-1,j))
                stack.append((i,j+1))
                stack.append((i,j-1))
        
        return image
