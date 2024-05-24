def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_numbers_in_range(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

if __name__ == "__main__":
    start = int(input("Enter the starting number of the range: "))
    end = int(input("Enter the ending number of the range: "))

    print("Prime numbers in the range", start, "to", end, "are:")
    print(prime_numbers_in_range(start, end))
