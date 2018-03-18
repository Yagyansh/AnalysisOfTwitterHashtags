"""
  Applies the LDA algorithm using libraries.
  (Parameters are mentioned in the TuningParameters File)
  Saves the LDA model.
"""
from os.path import join

from gensim import corpora, models

from ExtraUseFiles.TuningParameters import NUMBER_OF_TOPICS, NUMBER_OF_PASSES, ALPHA
from ExtraUseFiles.Constants import *
from ExtraUseFiles.OS_Utility import get_dir
from ExtraUseFiles.DateTimeController import start_timing, stop_timing, get_time, get_today, get_date_string


TODAY = get_today()
TODAY_STRING = get_date_string(TODAY)

ROOT = get_dir(__file__)
DICTIONARY_PATH = join(ROOT, DICT_CORPUS_MODEL_DIR, DICTIONARY_PREFIX + TODAY_STRING + DICT)
CORPUS_PATH = join(ROOT, DICT_CORPUS_MODEL_DIR, CORPUS_PREFIX + TODAY_STRING + MM)
LDA_PATH = join(ROOT, DICT_CORPUS_MODEL_DIR, LDA_MODEL_PREFIX + TODAY_STRING + LDA)

CORPUS = corpora.MmCorpus(CORPUS_PATH)
DICTIONARY = corpora.Dictionary.load(DICTIONARY_PATH)


def execute():

    print 'Started LDA Model Creation at ' + get_time() + '... ',

    start_timing()

    lda = models.LdaModel(CORPUS, id2word=DICTIONARY,num_topics=NUMBER_OF_TOPICS,passes=NUMBER_OF_PASSES,
                          alpha=ALPHA)

    lda.save(LDA_PATH)

    print 'Model Created Successfully'
    stop_timing()


if __name__ == '__main__':
    execute()
