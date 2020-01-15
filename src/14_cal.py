"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime
# from datetime import date

arg = sys.argv

cur_y = datetime.now().year
cur_m = datetime.now().month
cal = calendar.TextCalendar()
# print(cur_m, cur_y)

if len(arg)==1:
  dis_cal = cal.formatmonth(cur_y, cur_m)
  print(dis_cal)
elif len(arg)==2:
  new_month = int(sys.argv[1])
  if 1<new_month < 12:
    dis_cal = cal.formatmonth(cur_y, new_month)
    print(dis_cal)
  else:
    print('please enter number between 1 and 12')
elif len(arg)==3:
  new_month = int(sys.argv[2])
  new_year = sys.argv[1]
  if len(new_year) ==4:
    n_y = int(new_year)
    dis_cal = cal.formatmonth(n_y, new_month)
    print(dis_cal)
  else:
    print('please enter value in yyyy mm format')
else:
  print('please use format yyyy mm for calendar')


  

