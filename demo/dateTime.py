from datetime import datetime


def strptime():
    edit_date = "11.01.2022"
    parsed_date = datetime.strptime(edit_date, "%d.%m.%Y")
    today = datetime.today()

    time_passed_since_edited = today - parsed_date

    print(f"Parsed date is: {parsed_date}")
    print(f"Type of parsed date is: {type(parsed_date)}")

    print(f"Edited {time_passed_since_edited.days} days ago")
