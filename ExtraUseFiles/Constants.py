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

def TOPIC_COLLECTION_NAME(topic_id):
    return TOPIC_COLLECTION_PREFIX + str(topic_id)

# MongoDB Operators
LESS_THAN = '$lt'
GREATER_THAN_OR_EQUAL = '$gte'

#File Names
DATA_FILE_PREFIX = 'data'
PREPROCESSOR = 'PreProcessor.py'
ENTITYAGGREGATOR = 'EntityAggregator.py'
TOPIC_FILE_PREFIX = 'Topic'


# Directories
DATA_DIR = 'ScrapedData'
TEMP_DIR = 'Temporary'
EXTRACTOR_DIR = 'DataScraper'
PROCESSOR_DIR = 'DataProcessor'
WORKING_DIR = 'PrimaryWorker'
MAPREDUCE_DIR = 'MapReduce'
DICT_CORPUS_MODEL_DIR = 'DictionaryANDCorpusANDModel'
TOPICS_DATA_DIR = 'ResultingTopics'
TOPIC_MODELLER_DIR = 'Topic_Modeller'
TSV_DIR = 'TopicTSVs'

# LDA Files
DICTIONARY_PREFIX = 'dictionary_'
CORPUS_PREFIX = 'corpus_'
LDA_MODEL_PREFIX = 'model_'


# File Extensions
JSON = '.json'
MM = '.mm'
DICT = '.dict'
LDA = '.lda'
TXT = '.txt'
TSV = '.tsv'


# File Constants
UTF8 = 'utf-8'
WRITE = 'w'
READ = 'r'
