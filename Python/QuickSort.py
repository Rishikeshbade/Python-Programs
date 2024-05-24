import random
import time

# Method to generate random floating-point numbers
def generate_numbers():
    return [random.uniform(1.0, 100.0) for _ in range(100000)]

# Selection Sort algorithm
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Quick Sort algorithm
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Performance comparison method
def compare_performance():
    numbers = generate_numbers()

    # Copy of numbers for sorting
    numbers_selection_sort = numbers.copy()
    numbers_quick_sort = numbers.copy()

    # Measure selection sort execution time
    start_time = time.time()
    selection_sort(numbers_selection_sort)
    selection_sort_time = (time.time() - start_time) * 1000

    # Measure quick sort execution time
    start_time = time.time()
    quick_sort(numbers_quick_sort)
    quick_sort_time = (time.time() - start_time) * 1000

    print("Selection Sort Time: {:.3f} milliseconds".format(selection_sort_time))
    print("Quick Sort Time: {:.3f} milliseconds".format(quick_sort_time))

    # Performance comparison
    if selection_sort_time < quick_sort_time:
        faster_algorithm = "Selection Sort"
        percentage_difference = ((quick_sort_time - selection_sort_time) / quick_sort_time) * 100
    else:
        faster_algorithm = "Quick Sort"
        percentage_difference = ((selection_sort_time - quick_sort_time) / selection_sort_time) * 100

    print("{} is faster by {:.2f}%".format(faster_algorithm, percentage_difference))

# Main method
if __name__ == "__main__":
    compare_performance()

