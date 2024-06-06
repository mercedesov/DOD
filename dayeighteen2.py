def convert_time(time):
    if time[-2:] == "PM":
        time = str(int(time[:2]) + 12) + time[2:]
    if time[:2] == "12" and time[-2:] == "AM":
        time = "00" + time[2:]
    return time[:-2]

print(convert_time("11:21:30 PM"))
print(convert_time("12:12:20 AM"))

