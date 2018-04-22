import pandas as pd
from os.path import join
import gensim
from gensim import corpora, models
import matplotlib.pyplot as plt

from ExtraUseFiles.Cleaner import clean
from ExtraUseFiles.Constants import *
from ExtraUseFiles.OS_Utility import get_dir
from ExtraUseFiles.DateTimeController import start_timing, stop_timing, get_time, get_today, get_date_string
from PrimaryWorker.TopicModeller.LDA_Preprocessor import get_documents

TODAY = get_today()
TODAY_STRING = get_date_string(TODAY)

ROOT = get_dir(__file__)
DICTIONARY_PATH = join(ROOT, DICT_CORPUS_MODEL_DIR, DICTIONARY_PREFIX + TODAY_STRING + DICT)
CORPUS_PATH = join(ROOT, DICT_CORPUS_MODEL_DIR, CORPUS_PREFIX + TODAY_STRING + MM)
LDA_PATH = join(ROOT, DICT_CORPUS_MODEL_DIR, LDA_MODEL_PREFIX + TODAY_STRING + LDA)

CORPUS = corpora.MmCorpus(CORPUS_PATH)
# print CORPUS
DICTIONARY = corpora.Dictionary.load(DICTIONARY_PATH)
documents = get_documents()
tokenized_documents = clean(documents)

LDA_MODEL = models.LdaModel.load(LDA_PATH)

def format_topics_sentences(ldamodel=LDA_MODEL, corpus=CORPUS, texts=tokenized_documents):
    # Init output
    sent_topics_df = pd.DataFrame()

    # Get main topic in each document
    for i, row in enumerate(ldamodel[corpus]):
        row = sorted(row, key=lambda x: (x[1]), reverse=True)
        # Get the Dominant topic, Perc Contribution and Keywords for each document
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0:  # => dominant topic
                wp = ldamodel.show_topic(topic_num)
                topic_keywords = ", ".join([word for word, prop in wp])
                sent_topics_df = sent_topics_df.append(pd.Series([int(topic_num), round(prop_topic,4), topic_keywords]), ignore_index=True)
            else:
                break
    sent_topics_df.columns = ['Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']

    # Add original text to the end of the output
    contents = pd.Series(texts)
    sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)
    return(sent_topics_df)


df_topic_sents_keywords = format_topics_sentences(ldamodel=LDA_MODEL, corpus=CORPUS, texts=tokenized_documents)

# Format
df_dominant_topic = df_topic_sents_keywords.reset_index()
df_dominant_topic.columns = ['Document_Number', 'Dominant_Topic', 'Topic_Perc_Contrib', 'Keywords', 'Text']

# Show
print df_dominant_topic.tail(20)