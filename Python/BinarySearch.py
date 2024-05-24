def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # If we reach here, the target is not present in the array
    return -1

# Test cases
arr1 = [2, 3, 5, 7, 9]
target1 = 7
result1 = binary_search(arr1, target1)
if result1 != -1:
    print(f"Element found at Index {result1}")
else:
    print("Element Not Found")

arr2 = [1, 4, 5, 8, 9]
target2 = 7
result2 = binary_search(arr2, target2)
if result2 != -1:
    print(f"Element found at Index {result2}")
else:
    print("Element Not Found")