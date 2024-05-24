def check_season(month):
    if month == 2 or month == 3:
        return "Vasanta"
    elif month == 4 or month == 5:
        return "Grishma / Summer"
    elif month == 6 or month == 7:
        return "Monsoon / Rainy"
    elif month == 8 or month == 9:
        return "Sharada"
    elif month == 10 or month == 11:
        return "Hemanta"
    elif month == 12 or month == 1:
        return "Shishira / Winter"
    else:
        return "Invalid month number"


def main():
    while True:
        try:
            month = int(input("Enter the month number (1-12): "))
            if month < 1 or month > 12:
                raise ValueError("Month number must be between 1 and 12")
            season = check_season(month)
            print(f"The season for month {month} is: {season}")
            break
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid month number.")


if __name__ == "__main__":
    main()
