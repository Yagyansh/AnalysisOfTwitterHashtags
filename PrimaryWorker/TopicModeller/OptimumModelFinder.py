from os.path import join
import gensim
from gensim import corpora, models
import matplotlib.pyplot as plt

from ExtraUseFiles.Cleaner import clean
from ExtraUseFiles.TuningParameters import NUMBER_OF_TOPICS, NUMBER_OF_PASSES, ALPHA
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


def compute_coherence_values(dictionary, corpus, texts, limit, start=2, step=3):
    """
    Compute c_v coherence for various number of topics

    Parameters:
    ----------
    dictionary : Gensim dictionary
    corpus : Gensim corpus
    texts : List of input texts
    limit : Max num of topics

    Returns:
    -------
    model_list : List of LDA topic models
    coherence_values : Coherence values corresponding to the LDA model with respective number of topics
    """
    coherence_values = []
    model_list = []
    for num_topics in range(start, limit, step):
        model = models.LdaModel(corpus=corpus, num_topics=num_topics, id2word=DICTIONARY, passes=NUMBER_OF_PASSES,
                                alpha=ALPHA)
        model_list.append(model)
        coherencemodel = models.CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
        coherence_values.append(coherencemodel.get_coherence())

    return model_list, coherence_values

# if __name__ == '__main__':

print 'Started Finding Best LDA Model at ' + get_time() + '... \n',

start_timing()

model_list, coherence_values = compute_coherence_values(dictionary=DICTIONARY, corpus=CORPUS, texts=tokenized_documents,
                                                        start=2, limit=40, step=6)

print 'Completed Successfully'
stop_timing()

limit = 40;
start = 2;
step = 6;
x = range(start, limit, step)
plt.plot(x, coherence_values)
plt.xlabel("Number of Topics")
plt.ylabel("Coherence Score")
plt.title('Coherence Values for Different Number of Topics')
plt.legend(("coherence_values"), loc='best')
# plt.show()
plt.savefig('/home/yagyansh/AnalysisOfTwitterHashtags/PrimaryWorker/TopicModeller/CoherenceScores/Coherence_Values.png')

filehandler = open('/home/yagyansh/AnalysisOfTwitterHashtags/PrimaryWorker/TopicModeller/CoherenceScores/OptimumTopics.txt','a')

OPTIMAL_MODEL = model_list[4]
for m, cv in zip(x, coherence_values):
    filehandler.write("Number of Topics = %d" %(m) + " has Coherence Value of " + str(round(cv, 4)) + "\n")

def best_model():
    return model_list