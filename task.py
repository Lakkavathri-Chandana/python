def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# Test the function2024
year = int(input("Enter a year: "))
if leap_year(year):
    print(" it is a leap year.")
else:
    print("it is not a leap year.")