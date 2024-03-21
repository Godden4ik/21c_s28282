import math


class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("Task 6: End of range cannot be less than start.")
        squares = [x ** 2 for x in range(start, end + 1)]
        return [math.sqrt(x) for x in squares]


try:
    print("Task 6 and 7:", SquareGenerator().generate_squares(1, 10))
except ValueError as e:
    print(e)
