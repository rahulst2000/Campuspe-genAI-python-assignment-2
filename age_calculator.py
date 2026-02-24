# Simple Age Calculator (Easy Level)
# This program calculates a person's age in years, months, and days.
# The user enters birth date and current date separately.
# The program subtracts birth values from current values.
# If days or months become negative, adjustments are made.
# Each month is assumed to have 30 days for simple calculation.

birth_year = int(input("Birth year: "))
birth_month = int(input("Birth month: "))
birth_day = int(input("Birth day: "))
current_year = int(input("Current year: "))
current_month = int(input("Current month: "))
current_day = int(input("Current day: "))

age_years = current_year - birth_year
age_months = current_month - birth_month
age_days = current_day - birth_day

if age_days < 0:
    age_months -= 1
    age_days += 30  #In a each we assume month have 30 days  
if age_months < 0:
    age_years -= 1
    age_months += 12

print("Age:", age_years, "years,", age_months, "months,", age_days, "days")