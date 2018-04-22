"""
  Applies the LDA algorithm using libraries.
  (Parameters are mentioned in the TuningParameters File)
  Saves the LDA model.
"""
from os.path import join

import gensim
from gensim import corpora, models
from gensim.models import CoherenceModel

# Plotting tools

import pyLDAvis
import pyLDAvis.gensim  # don't skip this
import matplotlib.pyplot as plt

# Enable logging for gensim - optional
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)

from ExtraUseFiles.Cleaner import clean
from ExtraUseFiles.TuningParameters import NUMBER_OF_TOPICS, NUMBER_OF_PASSES, ALPHA
from ExtraUseFiles.Constants import *
from ExtraUseFiles.OS_Utility import get_dir
from ExtraUseFiles.DateTimeController import start_timing, stop_timing, get_time, get_today, get_date_string
from PrimaryWorker.TopicModeller.LDA_Preprocessor import get_documents
# from PrimaryWorker.TopicModeller.OptimumModelFinder import best_model



TODAY = get_today()
TODAY_STRING = get_date_string(TODAY)

ROOT = get_dir(__file__)
DICTIONARY_PATH = join(ROOT, DICT_CORPUS_MODEL_DIR, DICTIONARY_PREFIX + TODAY_STRING + DICT)
CORPUS_PATH = join(ROOT, DICT_CORPUS_MODEL_DIR, CORPUS_PREFIX + TODAY_STRING + MM)
LDA_PATH = join(ROOT, DICT_CORPUS_MODEL_DIR, LDA_MODEL_PREFIX + TODAY_STRING + LDA)

CORPUS = corpora.MmCorpus(CORPUS_PATH)
DICTIONARY = corpora.Dictionary.load(DICTIONARY_PATH)
documents = get_documents()
tokenized_documents = clean(documents)

# OPTIMAL_MODEL = best_model()[4]

def execute():

    print 'Started LDA Model Creation at ' + get_time() + '... \n',

    start_timing()

    lda = models.LdaModel(CORPUS, id2word=DICTIONARY,num_topics=NUMBER_OF_TOPICS,passes=NUMBER_OF_PASSES,
                           alpha=ALPHA)
    # lda = OPTIMAL_MODEL
    lda.save(LDA_PATH)

    #Visulaizing the Topics
    visualization = pyLDAvis.gensim.prepare(lda, CORPUS, DICTIONARY)
    pyLDAvis.save_html(visualization,'/home/yagyansh/AnalysisOfTwitterHashtags/PrimaryWorker/TopicModeller/Similarities/Topics_Visualization')

    #Computing Coherence Score
    coherence_model_lda = CoherenceModel(model=lda, texts=tokenized_documents, dictionary=DICTIONARY, coherence='c_v')
    coherence_lda = coherence_model_lda.get_coherence()
    filehandler = open("/home/yagyansh/AnalysisOfTwitterHashtags/PrimaryWorker/TopicModeller/CoherenceScores/CoherenceScore.txt", 'a')
    filehandler.write("Coherence Score Of LDA with %d topics is: " %(NUMBER_OF_TOPICS) + str(coherence_lda) + "\n")

    # mallet_path = '/home/yagyansh/AnalysisOfTwitterHashtags/PrimaryWorker/TopicModeller/mallet-2.0.8/'
    # ldamallet = gensim.models.wrappers.LdaMallet(mallet_path, corpus=CORPUS, num_topics=NUMBER_OF_TOPICS, id2word=DICTIONARY)
    # coherence_model_ldamallet = CoherenceModel(model=ldamallet, texts=tokenized_documents, dictionary=DICTIONARY,
    #                                            coherence='c_v')
    # coherence_ldamallet = coherence_model_ldamallet.get_coherence()
    # filehandler.write("Coherence Score of LDA Mallet is: " + str(coherence_ldamallet))

    print 'Model Created Successfully'
    stop_timing()


if __name__ == '__main__':
    execute()
