from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.x = defaultdict(lambda: defaultdict(int))
        self.y = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.x[point[0]][point[1]] += 1
        self.y[point[1]][point[0]] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        count = 0

        for y2, point_count in self.x[x1].items():            
            side_length = abs(y1 - y2)
            if side_length == 0:
                continue

            if self.y[y1][x1 + side_length] > 0 and self.y[y2][x1 + side_length] > 0:
                count += (
                    self.y[y1][x1 + side_length] 
                    * self.y[y2][x1 + side_length]
                    * self.y[y2][x1]
                )

            if self.y[y1][x1 - side_length] > 0 and self.y[y2][x1 - side_length] > 0:
                count += (
                    self.y[y1][x1 - side_length] 
                    * self.y[y2][x1 - side_length]
                    * self.y[y2][x1]
                )


        return count

