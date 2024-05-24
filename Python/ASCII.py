def convert_to_ascii(input_string):
    ascii_array = []
    for char in input_string:
        ascii_value = ord(char)
        ascii_array.append(ascii_value) 
    return ascii_array

def main():
    input_string = input("Enter a string: ")
    ascii_array = convert_to_ascii(input_string)
    print("ASCII values array:", ascii_array)

if __name__ == "__main__":
    main()
