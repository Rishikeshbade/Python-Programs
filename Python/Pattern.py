def print_pattern(rows):
    # Outer loop to iterate through each row
    for i in range(1, rows + 1):
        # Inner loop to print the stars in each row
        for j in range(1, i + 1):
            print("*", end=" ")  # Printing the star without a newline
        print()  # Moving to the next line after printing stars in a row

# Example usage:
num_rows = 5
print_pattern(num_rows)
