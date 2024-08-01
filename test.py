import datetime

class DateObject:
    def __init__(self, todaysDate, **kwargs):
        self.date = todaysDate
        self.dateTime = todaysDate.isoformat()
        self.epoch = todaysDate.timestamp()
        self.__dict__.update(kwargs)
        for k, v in self.__dict__.items():
            setattr(self, k, todaysDate.strftime(str(v)))

now = datetime.datetime.now()
dateObj = DateObject(
    now, 
    fulldate='%Y-%m-%d', 
    year='%Y',
    month='%b',
    day='%a',
    hour='%H',
    minute='%M',
    second='%S'
)
print(dateObj.__dict__)
print(dateObj.dateTime)
print(dateObj.epoch)
print(dateObj.fulldate)
print(dateObj.year)
print(dateObj.month)
print(dateObj.day)
print(dateObj.hour)
print(dateObj.minute)
print(dateObj.second)
