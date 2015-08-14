import os

#
# return 15/08/13/17/51/09
#
def date_time_to_path(date_time):
    result = os.path.join(date_time.strftime('%y'),
                          date_time.strftime('%m'),
                          date_time.strftime('%d'),
                          date_time.strftime('%H'),
                          date_time.strftime('%M'),
                          date_time.strftime('%S'))

    return result