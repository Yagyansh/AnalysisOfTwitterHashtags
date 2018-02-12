from datetime import datetime
from time import time


def get_time():
    return datetime.now().time().strftime('%H:%M:%S')

start_time = None
end_time = None


def time_taken():
    global start_time, end_time
    seconds = end_time - start_time
    minutes = seconds/60
    hours = int(minutes/60)
    minutes = int(minutes - hours*60)
    seconds = int(seconds - minutes*60 - hours*60*60)

    print 'Time to execute = ' + str(hours) + ':' + str(minutes) + ':' + str(seconds)


def start_timing():
    global start_time
    start_time = time()


def stop_timing():
    global end_time
    end_time = time()
    time_taken()

