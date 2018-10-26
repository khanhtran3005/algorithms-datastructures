def timeConversion(s):
    hour = s[:2]
    isNoon = s[len(s) - 2:] == 'PM'

    if isNoon and hour != '12':
        hour = str(int(hour) + 12)
    elif not isNoon and hour == '12':
        hour = '00'

    return hour+s[2:len(s)-2]

print(timeConversion('12:05:45PM'))
print(timeConversion('02:05:45PM'))
print(timeConversion('12:05:45AM'))