month = input("Enter the name of the month: ").lower()

days_in_month = {
    'january': 31,
    'february': 28,
    'march': 31,
    'april': 30,
    'may': 31,
    'june': 30,
    'july': 31,
    'august': 31,
    'september': 30,
    'october': 31,
    'november': 30,
    'december': 31
}

if month in days_in_month:
    print(f"The number of days in {month.capitalize()} is {days_in_month[month]}.")
else:
    print("Error: Invalid month name.")
