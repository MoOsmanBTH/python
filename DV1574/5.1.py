import datetime

def convert_to_datetime(date_string):
    ret_date = datetime.datetime.strptime(date_string, "%b %d %Y %I:%M%p")

    return ret_date.strftime("%Y-%m-%d %H:%M:%S")

print(convert_to_datetime("Jul 1 2014 2:43PM"))