

# Uses two loops to find the maximum value in a list
def find_max_repeated_scanning(lst):
    max_value = lst[0]
    for x in lst:
        # Scan the entire list to confirm it's the largest
        if all(x >= y for y in lst):
            max_value = x
    return max_value


numbers = [3, 5, 7, 2, 8, 10, 6]

# Resource-intensive algorithm
max_repeated = find_max_repeated_scanning(numbers)
print(f"Max using repeated scanning: {max_repeated}")
