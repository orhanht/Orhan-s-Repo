"""
Instructions:

Calculate the date of meetups.
Typically meetups happen on the same day of the week. In this exercise, you will take a description of a meetup date, and return the actual meetup date.

Examples of general descriptions are:
The first Monday of January 2017
The third Tuesday of January 2017
The wednesteenth of January 2017
The last Thursday of January 2017
The descriptors you are expected to parse are: 
first, second, third, fourth, fifth, last, monteenth, tuesteenth, wednesteenth, thursteenth, friteenth, saturteenth, sunteenth
Note that "monteenth", "tuesteenth", etc are all made up words. There was a meetup whose members realized that there are exactly 7 numbered days in a month that end in '-teenth'. 
Therefore, one is guaranteed that each day of the week (Monday, Tuesday, ...) will have exactly one date that is named with '-teenth' in every month.
Given examples of a meetup dates, each containing a month, day, year, and descriptor calculate the date of the actual meetup. For example, if given "The first Monday of January 2017", the correct meetup date is 2017/1/2.
"""

from datetime import date
import calendar


class MeetupDayException(Exception):
    pass


def meetup(year, month, week, day_of_week):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    first_day_of_month = date(year, month, 1).weekday()
    if week == "teenth":
        first_day_of_teenth = date(year, month, 13).weekday()
        diff = (weekdays.index(day_of_week) - first_day_of_teenth) % 7
        return date(year, month, 13 + diff)
    elif week == "1st":
        diff = (weekdays.index(day_of_week) - first_day_of_month) % 7
        return date(year, month, 1 + diff)
    elif week == "2nd":
        diff = (weekdays.index(day_of_week) - first_day_of_month) % 7
        return date(year, month, 8 + diff)
    elif week == "3rd":
        diff = (weekdays.index(day_of_week) - first_day_of_month) % 7
        return date(year, month, 15 + diff)
    elif week == "4th":
        diff = (weekdays.index(day_of_week) - first_day_of_month) % 7
        return date(year, month, 22 + diff)
    elif week == "5th":
        diff = (weekdays.index(day_of_week) - first_day_of_month) % 7
        if 29 + diff > calendar.monthrange(year, month)[1]:
            raise MeetupDayException("Invalid date")
        return date(year, month, 29 + diff)
    elif week == "last":
        last_day_of_month = sum(calendar.monthrange(year, month)) % 7
        diff = (last_day_of_month - weekdays.index(day_of_week) - 1) % 7
        return date(year, month, calendar.monthrange(year, month)[1] - diff)
