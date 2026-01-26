import calendar


def return_day(month, day, year):
    """
    Find the day of the week for a given date.

    Args:
        month: Month (1-12)
        day: Day of month (1-31)
        year: Year (1900-2999)

    Returns:
        Day name in uppercase (e.g., "MONDAY")

    Time Complexity: O(1) - calendar.weekday() is constant time
    Space Complexity: O(1) - fixed list of 7 days
    """
    # Get weekday number (0=Monday, 1=Tuesday, ..., 6=Sunday)
    weekday_num = calendar.weekday(year, month, day)

    # Map weekday number to day name
    days = [
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    weekday_name = days[weekday_num]

    return weekday_name


def main():
    # Parse input: "08 05 2015" → month=8, day=5, year=2015
    month, day, year = map(int, input().split())
    result = return_day(month, day, year)
    print(result)


if __name__ == "__main__":
    main()
