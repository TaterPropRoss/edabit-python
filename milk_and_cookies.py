def time_for_milk_and_cookies(date):
    Month = date.month
    Day = date.day
    if (Month == 12 and Day == 24):
        return True
    else:
        return False
#is it christmas eve? 

import datetime
print(time_for_milk_and_cookies(datetime.date(2013, 12, 24)))