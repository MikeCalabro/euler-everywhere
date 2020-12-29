# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
year = 1900
day = 1
dows = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
dowcount = 0
monthcount = 0
sundaycount = 0

while year < 2001:
  if year > 1900 and day == 1 and dows[dowcount % 7] == 'Sun':
    sundaycount += 1
  print(dows[dowcount % 7], months[monthcount % 12], day, year)
  day += 1
  dowcount += 1
  if months[monthcount % 12] in ['Sep', 'Apr', 'Jun', 'Nov'] and day == 31:
    day = 1
    monthcount += 1
  if months[monthcount % 12] in ['Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec'] and day == 32:
    if months[monthcount % 12] == 'Dec':
      year += 1
    day = 1
    monthcount += 1
  if months[monthcount % 12] == 'Feb':
    if year % 4 == 0 and year != 1900 and day == 30:
      day = 1
      monthcount += 1
    elif year == 1900 and day == 29:
      day = 1
      monthcount += 1
    elif year % 4 != 0 and day == 29:
      day = 1
      monthcount += 1

print(sundaycount)