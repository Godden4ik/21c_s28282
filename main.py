#Task 1

squares = [x**2 for x in range(1, 11)]

print("List of squares of numbers from 1 to 10:")
print(squares)

def generate_squares(start, end):
    return [x**2 for x in range(start, end+1)]

print(generate_squares(1, 10))
