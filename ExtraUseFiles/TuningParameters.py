from datetime import timedelta


CONSUMER_KEY="yh63OUHxeLm2OuUh484AzM6bC"
CONSUMER_SECRET="vAdsaxY3Umj1m25as8JeZQ64xWHmXkgClhFViPfnfkQjROLpTD"
ACCESS_TOKEN="553373769-2JykSrbsY4p4iZgGun41DtsLaN9du6r24erJIHFs"
ACCESS_TOKEN_SECRET="SOkR5hZpEOqC6hhaftqeWG6FUWA6FeHbYIVbDYAz62FXk"

# General
PYTHON_VERSION = '2.7.10'
TIMEZONE = 'Asia/Kolkata'


# time constants
SECONDS = 1
MINUTES = 60 * SECONDS
HOURS = 60*MINUTES


# Preprocessor
PROCESSOR_SLEEP_TIME = 10*MINUTES


# Tweets Extractor
MAX_TWEETS_IN_FILE = 10000
DISPLAY_COMPLETED_TWEETS_INTERVAL = 1000

FILE_NUMBER_RESET_VALUE = 1000
FILE_NAME_SUFFIX_DIGITS = len(str(FILE_NUMBER_RESET_VALUE - 1))  # number of digits in the suffix
FILE_NAME_FORMATTER = '%0' + str(FILE_NAME_SUFFIX_DIGITS) + 'd'

# The top 20 most used keywords from the following URL:
# http://techland.time.com/2009/06/08/the-500-most-frequently-used-words-on-twitter/
FILTER_KEYWORDS = ["a", "the", "i", "you", "to", "and", "is", "in", "u", "of", "it"]
ENGLISH = 'en'
