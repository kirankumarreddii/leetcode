class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width=width
        self.height=height
        self.snake=deque([(0,0)])
        self.snake_set={(0,0)}
        self.directions={
            "U":(-1,0),
            "D":(1,0),
            "L":(0,-1),
            "R":(0,1)
        }
        self.count=0
        self.food=food
    def move(self, direction: str) -> int:
        r,c=self.directions[direction]
        snake_row,snake_col=self.snake[-1]
        new_head_row=snake_row+r
        new_head_col=snake_col+c
        new_head=(new_head_row,new_head_col)
        if not (0 <= new_head_row < self.height and 0 <= new_head_col < self.width):

            return -1
        
        eating = self.count < len(self.food) and self.food[self.count] == [new_head_row, new_head_col]
        if not eating:
            tail=self.snake.popleft()
            self.snake_set.remove(tail)
        if new_head in self.snake_set:
            return -1
        self.snake.append(new_head)
        self.snake_set.add(new_head)
        if eating:
            self.count+=1
        return len(self.snake) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)