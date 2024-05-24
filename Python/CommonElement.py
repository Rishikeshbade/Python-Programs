def find_common_elements(array1, array2):
    common_elements = []
    for element in array1:
        if element in array2 and element not in common_elements:
            common_elements.append(element)
    return common_elements

def main():
    # Input arrays
    array1 = input("Enter elements of the first array (comma-separated): ").split(',')
    array2 = input("Enter elements of the second array (comma-separated): ").split(',')

    # Finding common elements
    common_elements = find_common_elements(array1, array2)

    # Displaying common elements
    if len(common_elements) > 0:
        print("Common elements:", ', '.join(common_elements))
    else:
        print("No common elements found.")

if __name__ == "__main__":
    main()
