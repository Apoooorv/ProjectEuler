import datetime

date = datetime.date(1901,1,1)
enddate = datetime.date(2000,12,31)

count = 0

while date != enddate:
    if date.weekday() == 6 and date.day == 1:
        count+=1
    date += datetime.timedelta(days=1)
    
print count