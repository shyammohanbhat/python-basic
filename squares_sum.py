import time

def sum_of_squares(numbers)
    total = 0
    for num in numbers:
        total += num ** 2
    return total

# Generate a large list of numbers
numbers = list(range(1, 1000001))

# Measure the performance
start_time = time.time()
result = sum_of_squares(numbers)
end_time = time.time()

print("Sum of squares:", result)
print("Unoptimized execution time:", end_time - start_time, "seconds")
