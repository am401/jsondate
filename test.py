import datetime
import pytz
from zoneinfo import ZoneInfo

class DateObject:
    def __init__(self, todaysDate, **kwargs):
        self.dateTime = todaysDate.isoformat()
        self.epoch = todaysDate.timestamp()
        self.__dict__.update(kwargs)
        for k, v in self.__dict__.items():
            setattr(self, k, todaysDate.strftime(str(v)))

nowUTC = datetime.datetime.now(pytz.utc)
nowCDT = datetime.datetime.now(pytz.timezone('America/Chicago'))
dateObjUTC = DateObject(
    nowUTC, 
    fulldate='%Y-%m-%d', 
    year='%Y',
    month='%b',
    day='%a',
    hour='%H',
    minute='%M',
    second='%S'
)
print(dateObjUTC.__dict__)
print(dateObjUTC.dateTime)
print(dateObjUTC.epoch)
print(dateObjUTC.fulldate)
print(dateObjUTC.year)
print(dateObjUTC.month)
print(dateObjUTC.day)
print(dateObjUTC.hour)
print(dateObjUTC.minute)
print(dateObjUTC.second)
dateObjCDT = DateObject(
    nowCDT, 
    fulldate='%Y-%m-%d', 
    year='%Y',
    month='%b',
    day='%a',
    hour='%H',
    minute='%M',
    second='%S'
)
print(dateObjCDT.__dict__)
print(dateObjCDT.dateTime)
print(dateObjCDT.epoch)
print(dateObjCDT.fulldate)
print(dateObjCDT.year)
print(dateObjCDT.month)
print(dateObjCDT.day)
print(dateObjCDT.hour)
print(dateObjCDT.minute)
print(dateObjCDT.second)
