age = input("What is your current age?")

years_until_90 = 90 - int(age)
days_left = years_until_90 * 365
weeks_left = years_until_90 * 52
months_left = years_until_90 * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
