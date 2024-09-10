import datetime

def unix_to_datetime(unix_time):
    return datetime.datetime.utcfromtimestamp(unix_time)

# Example Unix time (replace this with your Unix time)
unix_time = 1718059245

# Convert Unix time to datetime object
converted_time = unix_to_datetime(unix_time)

# Print the converted time

print(f'Converted time: {converted_time.strftime("%I:%M %p")}')
