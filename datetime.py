import time

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)


# What is TimeTuple: Many of Python's time functions handle time as a tuple of 9 numbers:

'''
Index 	Field 	                        Values
------------------------------------------------------------------------------------
0 	    4-digit year (tm_year) 	        2008
1 	    Month (tm_mon) 		            1 to 12
2 	    Day (tm_mday) 		            1 to 31
3 	    Hour (tm_hour) 	                0 to 23
4 	    Minute (tm_min) 		        0 to 59
5 	    Second (tm_sec) 		        0 to 61 (60 or 61 are leap-seconds)
6 	    Day of Week (tm_wday) 		    0 to 6 (0 is Monday)
7 	    Day of year (tm_yday) 		    1 to 366 (Julian day)
8 	    Daylight savings (tm_isdst) 	-1, 0, 1  (-1 means library determines DST)
'''

localtime = time.localtime(time.time())
print("Local current time :", localtime)
# Ausgabe:
# time.struct_time(tm_year=2020, tm_mon=9, tm_mday=2, tm_hour=13, tm_min=11, tm_sec=42, tm_wday=2, tm_yday=246, tm_isdst=1)

# asctime: Accepts a time-tuple and returns a readable 24-character string such as 'Tue Dec 11 18:07:14 2008'.
localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)

print("time.ctime() : %s" % time.ctime())

gmtime = time.gmtime()
print(gmtime)

# localtime() is similar to gmtime() but it converts number of seconds to local time
localtime = time.localtime()
print(localtime)

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
secs = time.mktime(t)
print("%f" % secs)
print("%s" % time.asctime(time.localtime(secs)))


# print("Start : %s" % time.ctime())
# time.sleep(5)  # 5 Seconds
# print("End : %s" % time.ctime())

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
t = time.mktime(t)
print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))
print(time.strftime("Germany: %d.%m.%Y %H:%M:%S", time.localtime()))
'''
    %a - abbreviated weekday name
    %A - full weekday name
    %b - abbreviated month name
    %B - full month name
    %c - preferred date and time representation
    %C - century number (the year divided by 100, range 00 to 99)
    %d - day of the month (01 to 31)
    %D - same as %m/%d/%y
    %e - day of the month (1 to 31)
    %g - like %G, but without the century
    %G - 4-digit year corresponding to the ISO week number (see %V).
    %h - same as %b
    %H - hour, using a 24-hour clock (00 to 23)
    %I - hour, using a 12-hour clock (01 to 12)
    %j - day of the year (001 to 366)
    %m - month (01 to 12)
    %M - minute
    %n - newline character
    %p - either am or pm according to the given time value
    %r - time in a.m. and p.m. notation
    %R - time in 24 hour notation
    %S - second
    %t - tab character
    %T - current time, equal to %H:%M:%S
    %u - weekday as a number (1 to 7), Monday=1. Warning: In Sun Solaris Sunday=1
    %U - week number of the current year, starting with the first Sunday as the first day of the first week
    %V - The ISO 8601 week number of the current year (01 to 53), where week 1 is the first week that has at least 4 days in the current year, and with Monday as the first day of the week
    %W - week number of the current year, starting with the first Monday as the first day of the first week
    %w - day of the week as a decimal, Sunday=0
    %x - preferred date representation without the time
    %X - preferred time representation without the date
    %y - year without a century (range 00 to 99)
    %Y - year including the century
    %Z or %z - time zone or name or abbreviation
    %% - a literal % character
'''
