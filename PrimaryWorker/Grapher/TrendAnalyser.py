"""
Calculates frequency of tweet in each minute of the day.
Total 24*60 data points
Stores in a .tsv file
"""

import os
from os.path import join

from pymongo import MongoClient

from ExtraUseFiles.TuningParameters import DAY_START, APPROXIMATION_RANGE, NUMBER_OF_TOPICS
from ExtraUseFiles.Constants import *
from ExtraUseFiles.OS_Utility import get_dir, get_files_in_dir
from ExtraUseFiles.DateTimeController import get_today, get_datetime_from_string, get_next_day, \
    get_date_time_string, localize_datetime, get_differenced_day

ROOT = get_dir(__file__)
TSV_DIR_PATH = join(ROOT, TSV_DIR)
START_DATE = get_differenced_day(get_today(), -16)
print START_DATE
client = MongoClient()
topics_db = client['tweets']

entities = []


def remove_previous_data():
    tsv_files = get_files_in_dir(TSV_DIR_PATH, TSV)
    for tsv_file in tsv_files:
        os.remove(join(TSV_DIR_PATH, tsv_file))


def init_writer(tid):
    filename = TOPIC_FILE_PREFIX + str(tid) + TSV
    file_path = join(TSV_DIR_PATH, filename)

    x = open(file_path, WRITE)

    x.write('datetime\tcount\n')
    return x


def close_writer(writer):
    writer.close()


def make_entry(writer, obj, count):
    writer.write(get_date_time_string(obj) + '\t' + str(count) + '\n')


def generate_graph_data_for_day(coll_name, day, next_day_start, writer):
    coll = topics_db[coll_name]
    lower = get_datetime_from_string(day, DAY_START)
    upper = lower + APPROXIMATION_RANGE
    while upper <= next_day_start:
        tweet_count = coll.find({TIMESTAMP: {GREATER_THAN_OR_EQUAL: lower, LESS_THAN: upper}}).count()
        make_entry(writer, lower, tweet_count * 100)
        lower += APPROXIMATION_RANGE
        upper += APPROXIMATION_RANGE


def generate_graph_data(tid):
    writer = init_writer(tid)
    day = START_DATE
    day = localize_datetime(day)
    coll_name = TOPIC_COLLECTION_NAME(tid)
    next_day = get_next_day(day)
    next_day_start = get_datetime_from_string(next_day, DAY_START)
    generate_graph_data_for_day(coll_name, day, next_day_start, writer)

    close_writer(writer)


if __name__ == '__main__':
    remove_previous_data()
    for topic_id in range(NUMBER_OF_TOPICS):
        print 'Generating data points for topic: ' + str(topic_id) + ' ... ',
        generate_graph_data(topic_id)
        print 'Done'
    client.close()
