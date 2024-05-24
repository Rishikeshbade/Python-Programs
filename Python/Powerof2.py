import sys

def power_of_2_table(n):
    try:
        n = int(n)
        if n < 0:
            raise ValueError("n must be a non-negative integer.")
    except ValueError as e:
        print("Error:", e)
        return

    print("Powers of 2 up to 2^{}:".format(n))
    print("Power\tValue")
    for i in range(n + 1):
        power_of_2 = 2 ** i
        print("{}\t{}".format(i, power_of_2))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python PowerOf2.py <n>")
    else:
        power_of_2_table(sys.argv[1])
