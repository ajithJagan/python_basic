import datetime as dt

today = dt.datetime.now() # current date and time
UTC = dt.datetime.now(dt.timezone.utc) # current UTC time (recommended way)
print(today)
print(UTC)
print(today.year)
print(today.month)
print(today.day)

print(today.hour)
print(today.minute)
print(today.second)


