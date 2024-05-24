def print_initials(initials):
    alphabet = {
        'A': ["  *  ", " * * ", "*   *", "*****", "*   *", "*   *", "*   *"],
        'B': ["**** ", "*   *", "*   *", "**** ", "*   *", "*   *", "**** "],
        'C': [" ****", "*    ", "*    ", "*    ", "*    ", "*    ", " ****"],
        'D': ["**** ", "*   *", "*    *", "*    *", "*    *", "*   *", "**** "],
        'E': ["*****", "*    ", "*    ", "**** ", "*    ", "*    ", "*****"],
        'F': ["*****", "*    ", "*    ", "**** ", "*    ", "*    ", "*    "],
        'G': ["*****", "*    ", "*    ", "* ***", "*   *", "*   *", "*****"],
        'H': ["*   *", "*   *", "*   *", "*****", "*   *", "*   *", "*   *"],
        'I': ["*****", "  *  ", "  *  ", "  *  ", "  *  ", "  *  ", "*****"],
        'J': ["*****", "    *", "    *", "    *", "    *", "*   *", " *** "],
        'K': ["*   *", "*  * ", "* *  ", "**   ", "* *  ", "*  * ", "*   *"],
        'L': ["*    ", "*    ", "*    ", "*    ", "*    ", "*    ", "*****"],
        'M': ["*   *", "** **", "* * *", "*   *", "*   *", "*   *", "*   *"],
        'N': ["*   *", "**  *", "* * *", "*  **", "*   *", "*   *", "*   *"],
        'O': [" *** ", "*   *", "*   *", "*   *", "*   *", "*   *", " *** "],
        'P': ["**** ", "*   *", "*   *", "**** ", "*    ", "*    ", "*    "],
        'Q': [" *** ", "*   *", "*   *", "*   *", "* * *", "*  **", " *** "],
        'R': ["**** ", "*   *", "*   *", "**** ", "* *  ", "*  * ", "*   *"],
        'S': [" ****", "*    ", "*    ", " *** ", "    *", "    *", "**** "],
        'T': ["*****", "  *  ", "  *  ",  "  *  ", "  *  ", "  *  ", "  *  "],
        'U': ["*   *", "*   *", "*   *", "*   *", "*   *", "*   *", " *** "],
        'V': ["*   *", "*   *", "*   *", "*   *", " * * ", " * * ", "  *  "],
        'W': ["*   *", "*   *", "*   *", "*   *", "* * *", "** **", "*   *"],
        'X': ["*   *", "*   *", " * * ", "  *  ", " * * ", "*   *", "*   *"],
        'Y': ["*   *", "*   *", "*   *", " *** ", "  *  ", "  *  ", "  *  "],
        'Z': ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*****"],
        ' ': ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
    }

    for i in range(7):
        for initial in initials:
            print(alphabet[initial][i], end='  ')
        print()

if __name__ == "__main__":
    user_input = input("Enter initials: ").upper()
    print_initials(user_input)