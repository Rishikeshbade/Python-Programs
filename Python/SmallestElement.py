def find_second_smallest(arr):
    
    if len(arr) < 2:
        return "Array should have at least two elements"

    
    smallest = float('inf')
    second_smallest = float('inf')

    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    
    return second_smallest


arr = [12, 4, 7, 2, 9, 5]
print("Second smallest element is:", find_second_smallest(arr))
