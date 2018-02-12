from os import rename
from os.path import join

from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import sys
sys.path.insert(0, '/home/yagyansh/AnalysisOfTwitterHashTags/ExtraUseFiles')

from ExtraUseFiles.TuningParameters import *
from ExtraUseFiles.Constants import *
from ExtraUseFiles.Percentage_JsonChecker import is_json
from ExtraUseFiles.OS_Utility import get_dir
from ExtraUseFiles.DateTimeController import get_time


display_number = DISPLAY_COMPLETED_TWEETS_INTERVAL

file_number = 1
tweet_count = 0
total_tweet_count = 0

ROOT = get_dir(__file__)

FILE_PATH = join(ROOT, DATA_DIR)
TEMP_PATH = join(ROOT, TEMP_DIR)


def get_filename(directory, number):
    return join(directory, DATA_FILE_PREFIX + FILE_NAME_FORMATTER % number + JSON)


def change_file():
    global tweets_file, file_name, file_number

    tweets_file.close()
    rename(file_name, get_filename(TEMP_PATH, file_number))  #Moving to Temporary Folder

    file_number += 1
    if file_number == FILE_NUMBER_RESET_VALUE:
        file_number = 1

    file_name = get_filename(FILE_PATH, file_number)
    tweets_file = open(file_name, WRITE)


class StdOutListener(StreamListener):

    def on_data(self, data):

        if not is_json(data):  # checking for invalid tweet
            return True
        global tweet_count, file_number, tweets_file, file_name, display_number, total_tweet_count

        tweet_count += 1
        total_tweet_count += 1
        tweets_file.write(data)

        if total_tweet_count == display_number:  # Check for Updating # of Downloaded Tweets
            print '\r',
            print str(display_number) + ' Tweets Downloaded',
            display_number += DISPLAY_COMPLETED_TWEETS_INTERVAL

        if tweet_count == MAX_TWEETS_IN_FILE:
            tweet_count = 0
            change_file()

        return True

    def on_error(self, status):
        print 'Error: ' + status


if __name__ == '__main__':

    file_name = get_filename(FILE_PATH, file_number)
    tweets_file = open(file_name, WRITE)

    print "Started extracting tweets at " + get_time() + "... "

    while True:  # ensures continuous stream extraction

        try:
            # Twitter Authentication

            l = StdOutListener()
            auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

            stream = Stream(auth, l)
            stream.filter(languages=[ENGLISH], track=FILTER_KEYWORDS)

        except:  # TODO
            continue
