from machine import Pin, I2C
from ds3231 import DS3231

i2c = I2C(0)
ds = DS3231(i2c)

week_days = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday"
    ]
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
    ]
date_time = ds.datetime()
day = date_time[2]
weekday = date_time[3]

month = date_time[1]
year = date_time[0]

hour = date_time[4]
minute = date_time[5]
second = date_time[6]

print(f'date: {week_days[weekday - 1]} {months[month]} {day}, {year}')
print(f'time: {hour}:{minute}')