# Task 1
squares = [x ** 2 for x in range(1, 11)]
print("Task 1:", squares)


# Task 2
def generate_squares(start, end):
    return [x ** 2 for x in range(start, end + 1)]


print("Task 2:", generate_squares(1, 10))


# Task 3
class SquareGenerator:
    def generate_squares(self, start, end):
        return [x ** 2 for x in range(start, end + 1)]


print("Task 3:", SquareGenerator().generate_squares(1, 10))

# Task 4
import math


class SquareGenerator:
    def generate_squares(self, start, end):
        squares = [x ** 2 for x in range(start, end + 1)]
        return [math.sqrt(x) for x in squares]


print("Task 4:", SquareGenerator().generate_squares(1, 10))


# Task 5
class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("Task 5: End of range cannot be less than start.")
        squares = [x ** 2 for x in range(start, end + 1)]
        return [math.sqrt(x) for x in squares]


# Testing Task 5
try:
    print("Task 5:", SquareGenerator().generate_squares(10, 1))
except ValueError as e:
    print(e)


# Task 8
class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of range cannot be less than start.")
        return [x ** 3 for x in range(start, end + 1)]


# Testing Task 8
print("Task 8:", CubicGenerator().generate_squares(1, 5))


# Task 9
class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("Task 9 (cubes):End of range cannot be less than start.")
        return [x ** 3 for x in range(start, end + 1)]

    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("Task 9: (squares) End of range cannot be less than start.")
        return [x ** 2 for x in range(start, end + 1)]


# Testing Task 9
try:
    print("Task 9 (Cubic):", CubicGenerator().generate_squares(10, 1))
except ValueError as e:
    print(e)
