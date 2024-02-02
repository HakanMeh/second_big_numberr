def second_largest(numbers):
    if len(numbers) < 2:
        return "List should have at least two elements"

    largest = second = float('-inf')

    for number in numbers:
        if number > largest:
            second = largest
            largest = number
        elif number > second and number != largest:
            second = number

    if second == float('-inf'):
        return "There is no second largest element"
    else:
        return second

# Example usage:
numbers = [2, 3, 6, 6, 5]
result = second_largest(numbers)
print("Second largest number:", result)
