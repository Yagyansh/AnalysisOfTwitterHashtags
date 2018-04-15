"""
Preprocess the tweets for LDA:
 1.Performs Cleaning
 2.Create and save Dictionary and Corpus
"""

from os.path import join

from gensim import corpora
from pymongo import MongoClient, DESCENDING

from ExtraUseFiles.Cleaner import clean
from ExtraUseFiles.TuningParameters import NUMBER_OF_TOP_ENTITIES, TWEET_POOLING_SIZE
from ExtraUseFiles.Constants import *
from ExtraUseFiles.OS_Utility import get_dir
from ExtraUseFiles.DateTimeController import get_today, get_date_string, start_timing, stop_timing, get_time

TODAY = get_today()
TODAY_STRING = get_date_string(TODAY)
COLLECTION_DAY = TODAY
COLLECTION_DAY_STRING = get_date_string(COLLECTION_DAY)

ROOT = get_dir(__file__)
DICTIONARY_PATH = join(ROOT, DICT_CORPUS_MODEL_DIR, DICTIONARY_PREFIX + TODAY_STRING + DICT)
CORPUS_PATH = join(ROOT, DICT_CORPUS_MODEL_DIR, CORPUS_PREFIX + TODAY_STRING + MM)

COLLECTION_NAME = RAW_COLLECTION_PREFIX + COLLECTION_DAY_STRING
RESULTS_COLLECTION_NAME = ENTITY_RESULTS_COLLECTION_PREFIX + COLLECTION_DAY_STRING

client = MongoClient()
raw_db = client[RAW_TWEETS_DB_NAME]
raw_collection = raw_db[COLLECTION_NAME]
results_coll = raw_db[RESULTS_COLLECTION_NAME]


def get_documents():
    documents = []
    results = results_coll.find(limit=NUMBER_OF_TOP_ENTITIES, no_cursor_timeout=True) \
        .sort([(VALUE + '.' + COUNT, DESCENDING)])
    for result in results:
        entities = result[VALUE][PSEUDONYMS]
        for entity in entities:
            cnt = 0
            document = ''
            for tweet in raw_collection.find({ENTITIES: entity}):
                cnt += 1
                document += tweet[TWEET] + ' '  # Pooling tweets
                if cnt == TWEET_POOLING_SIZE:
                    documents.append(document)
                    document = ''
                    cnt = 0
            if document != '':
                documents.append(document)
    results.close()

    return documents


def execute():
    print 'Starting Pre-processing for LDA at ' + get_time() + '... ',
    start_timing()

    documents = get_documents()
    print documents
    tokenized_documents = clean(documents)
    print tokenized_documents

    dictionary = corpora.Dictionary([doc for doc in tokenized_documents])
    #print dictionary
    dictionary.compactify()  # Assign new word ids to all words, shrinking gaps.
    print dictionary
    dictionary.save(DICTIONARY_PATH)

    # Convert document into the bag-of-words (BoW) format = list of (token_id, token_count).
    corpus = [dictionary.doc2bow(doc) for doc in tokenized_documents]

    # Serialize corpus with offset metadata, allows to use direct indexes after loading.
    corpora.MmCorpus.serialize(CORPUS_PATH, corpus)

    print '\nFinished at  ' + get_time()
    stop_timing()

    client.close()


if __name__ == '__main__':
    execute()
