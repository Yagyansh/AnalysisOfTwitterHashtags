DATETIME_FORMAT = '%a %b %d %H:%M:%S +0000 %Y'

# Keys in Twitter JSON
CREATED_AT = 'created_at'
ENTITIES = 'entities'
TEXT = 'text'
RETWEET_COUNT = 'retweet_count'
ID = 'id'
USER = 'user'
SCREEN_NAME = 'screen_name'
PLACE = 'place'
COORDINATES = 'coordinates'
HASHTAGS = 'hashtags'
MENTIONS = 'user_mentions'
URLS = 'urls'
URL = 'url'
EXPANDED_URL = 'expanded_url'
RETWEETED_STATUS = 'retweeted_status'
LOWER_ENTITY = '_id'


# Keys in MongoDB
TIMESTAMP = 'Timestamp'
TWEET = 'Tweet'
RETWEETS = 'Retweets'
USERNAME = 'Username'

VALUE = 'value'
COUNT = 'count'
PSEUDONYMS = 'pseudos'
GENERAL_ID_TAG = '_id'

# MongoDB Literals
RAW_TWEETS_DB_NAME = 'raw_tweets'
TOPIC_TWEETS_DB_NAME = 'topic_tweets'
URL_RESULTS_DB_NAME = 'url_results'

RAW_COLLECTION_PREFIX = 'raw_'
ENTITY_RESULTS_COLLECTION_PREFIX = 'entity_result_'
TEMP_RAW_COLLECTION_NAME = 'raw_temp'
TEMP_RESULTS_COLLECTION_NAME = 'result_temp'
URL_RESULTS_COLLECTION_PREFIX = 'url_result_'
TOPIC_COLLECTION_PREFIX = 'topic_'

#File Names
DATA_FILE_PREFIX = 'data'


# Directories
DATA_DIR = 'ScrapedData'
TEMP_DIR = 'Temporary'
EXTRACTOR_DIR = 'DataScraper'
PROCESSOR_DIR = 'DataProcessor'
WORKING_DIR = 'PrimaryWorker'
MAPREDUCE_DIR = 'MapReduce'

# File Extensions
JSON = '.json'

# File Constants
UTF8 = 'utf-8'
WRITE = 'w'
READ = 'r'
