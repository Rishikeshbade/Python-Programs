def take_input_and_form_array():
    num_array = []
    print("Enter 10 integer numbers:")
    for i in range(10):
        num = int(input(f"Enter number {i + 1}: "))
        num_array.append(num)
    return num_array

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    
    numbers = take_input_and_form_array()

    
    bubble_sort(numbers)

    
    print("Sorted array:")
    for num in numbers:
        print(num, end=" ")

if __name__ == "__main__":
    main()
