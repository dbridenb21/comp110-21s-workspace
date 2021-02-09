"""A vaccination calculator."""

__author__ = "730231060"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

population: int = int(input("Enter population:"))
doses_admin: int = int(input("Enter doses administered:"))
doses_day: int = int(input("Enter doses per day:"))
target_pct: int = int(input("Enter target percent vaccinated:"))

doses_req: float = ((population * 2) * (target_pct / 100))
days_rem: float = ((doses_req - doses_admin) / doses_day)

today: datetime = datetime.today()
today.strftime("%B %d, %Y")
days_delta: timedelta = timedelta (round(days_rem))
goal_date: datetime = today + days_delta
print("We will reach " + str(target_pct) + "% vaccination in " + str(round(days_rem)) + " days, which falls on " + goal_date.strftime("%B %d, %Y")) 
