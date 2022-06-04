import datetime
def check_friday_13(yr, mon):
    date = 13
    day = datetime.date(yr, mon, date)
    if day.isoweekday() == 5:
        return day , True
    else: return day, False