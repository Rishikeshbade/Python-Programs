def sum_of_digits(number):
    # Initialize sum to 0
    total = 0
    # Convert number to a string to iterate through its digits
    number_str = str(number)
    # Iterate through each digit in the number
    for digit in number_str:
        # Convert the digit back to an integer and add it to the total
        total += int(digit)
    # Return the total sum of digits
    return total

# Example usage:
given_number = 23
print("The sum of digits in", given_number, "is:", sum_of_digits(given_number))
