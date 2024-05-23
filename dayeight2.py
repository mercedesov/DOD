from datetime import datetime

date_format = "%Y-%m-%d %H:%M:%S"

try:
    first_date_input = input("Enter the first date and time (YYYY-MM-DD HH:MM:SS): ")
    second_date_input = input("Enter the second date and time (YYYY-MM-DD HH:MM:SS): ")

    first_date = datetime.strptime(first_date_input, date_format)
    second_date = datetime.strptime(second_date_input, date_format)

    difference = second_date - first_date
    print(f"Difference is {difference.days} days")

except ValueError:
    print("Error: string is not a date or format incorrect")
