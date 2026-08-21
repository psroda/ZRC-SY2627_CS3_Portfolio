def isLeapYear(year):
    """Return True if `year` is a leap year, else False."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


if __name__ == "__main__":
    year = int(input("Enter a year: "))
    if isLeapYear(year):
        print(f"{year} is a Leap year")
    else:
        print(f"{year} is not a Leap year")
