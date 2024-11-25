import datetime

x = datetime.datetime.now()
print(x)

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(1998, 9, 14)
print(x)

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))