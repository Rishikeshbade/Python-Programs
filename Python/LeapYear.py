def is_leap_year(year):


    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

years_to_check = [1900, 2000, 2004, 2020, 2021, 2100, 2024, 2025, 2030]

for year in years_to_check:
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
