from datetime import datetime

def datetime_to_str(datetime_object):
    return datetime_object.strftime('%d/%m/%Y, %H:%M:%S')

def str_to_datetime(time_str):
    return datetime.strptime(time_str, '%d/%m/%Y, %H:%M:%S')