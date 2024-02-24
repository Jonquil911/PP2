#ex1
from datetime import datetime, timedelta

date_5days_ago = datetime.now() - timedelta(days=5)
print(date_5days_ago)

#ex2
from datetime import datetime, timedelta

yesterday = datetime.now() - timedelta(days=1)
print("Yesterday's date: ", yesterday.strftime("%Y-%m-%d"))
today = datetime.now()
print("Today's date: ", today.strftime("%Y-%m-%d"))
tomorrow = datetime.now() + timedelta(days=1)
print("Tommorow's date: ", tomorrow.strftime("%Y-%m-%d"))

#ex3
from datetime import datetime

date = datetime.now()
date2 = date.replace(microsecond=0)
print(date2)

#ex4
from datetime import datetime

date1 = input("YYYY-MM-DD HH:MM:SS ")
date2 = input("YYYY-MM-DD HH:MM:SS ")
date11 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
date22 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")

print(abs(date22 - date11).total_seconds())