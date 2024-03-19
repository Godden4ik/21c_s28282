#Task 1

squares = [x**2 for x in range(1, 11)]
print("Task 1:", squares)

def generate_squares(start, end):
    return [x**2 for x in range(start, end+1)]

print("Task 2:", generate_squares(1, 10))