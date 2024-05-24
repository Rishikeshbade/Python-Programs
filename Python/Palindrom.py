def is_palindrome(number):
    # Convert the number to a string to easily reverse it
    number_str = str(number)
    # Reverse the number string
    reversed_str = number_str[::-1]
    # Compare the original and reversed strings
    if number_str == reversed_str:
        return True
    else:
        return False

# Example usage:
given_number = 6
if is_palindrome(given_number):
    print(f"{given_number} is a palindrome.")
else:
    print(f"{given_number} is not a palindrome.")
