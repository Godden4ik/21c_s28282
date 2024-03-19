#Task 1

squares = [x**2 for x in range(1, 11)]
print("Task 1:", squares)

def generate_squares(start, end):
    return [x**2 for x in range(start, end+1)]

print("Task 2:", generate_squares(1, 10))

class SquareGenerator:
    def generate_squares(self, start, end):
        return [x**2 for x in range(start, end+1)]

print("Task 3:", SquareGenerator().generate_squares(1, 10))

import math

class SquareGenerator:
    def generate_squares(self, start, end):
        squares = [x**2 for x in range(start, end+1)]
        return [math.sqrt(x) for x in squares]

print("Task 4:", SquareGenerator().generate_squares(1, 10))