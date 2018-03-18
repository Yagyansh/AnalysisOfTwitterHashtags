from datetime import datetime, timedelta
from time import time


def get_time():
    return datetime.now().time().strftime('%H:%M:%S')


start_time = None
end_time = None


def time_taken():
    global start_time, end_time
    seconds = end_time - start_time
    minutes = seconds / 60
    hours = int(minutes / 60)
    minutes = int(minutes - hours * 60)
    seconds = int(seconds - minutes * 60 - hours * 60 * 60)

    print 'Time taken to execute = ' + str(hours) + ':' + str(minutes) + ':' + str(seconds)


def start_timing():
    global start_time
    start_time = time()


def stop_timing():
    global end_time
    end_time = time()
    time_taken()


def get_date_string(date_obj):
    date_string = date_obj.strftime('%d-%m-%Y')
    return date_string


def get_today():
    return datetime.today()

def get_prev_day(current_day):
    diff = timedelta(days=1)
    current_day -= diff
    return current_day

def get_differenced_day(current_day, days_delta):
    diff = timedelta(days=days_delta)
    differenced_day = current_day + diff
    return differenced_day
