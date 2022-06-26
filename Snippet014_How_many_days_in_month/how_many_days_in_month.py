def is_leap(l_year):
    if l_year % 4 == 0:
        if l_year % 100 == 0:
            if l_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(d_year, d_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    number_of_days = month_days[d_month - 1]
    if month > 12 or month < 1:
        return "Invalid month"
    if is_leap(d_year) and month == 2:
        number_of_days += 1
        return number_of_days
    return number_of_days


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












