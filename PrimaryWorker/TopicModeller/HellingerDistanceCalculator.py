from os.path import join

import gensim
from gensim import corpora, models
import numpy
from six import iteritems, itervalues
import scipy

from ExtraUseFiles.Constants import *
from ExtraUseFiles.OS_Utility import get_dir
from ExtraUseFiles.DateTimeController import get_today, get_date_string

TODAY = get_today()
TODAY_STRING = get_date_string(TODAY)

ROOT = get_dir(__file__)
DICTIONARY_PATH = join(ROOT, DICT_CORPUS_MODEL_DIR, DICTIONARY_PREFIX + TODAY_STRING + DICT)
CORPUS_PATH = join(ROOT, DICT_CORPUS_MODEL_DIR, CORPUS_PREFIX + TODAY_STRING + MM)
LDA_PATH = join(ROOT, DICT_CORPUS_MODEL_DIR, LDA_MODEL_PREFIX + TODAY_STRING + LDA)

CORPUS = corpora.MmCorpus(CORPUS_PATH)
DICTIONARY = corpora.Dictionary.load(DICTIONARY_PATH)
lda = models.LdaModel.load(LDA_PATH)

# topic0,topic1=lda.show_topics()[0:2]
# print topic0[1]
# print lda.print_topics(-1)
topics = []
# for i in range(len(lda.show_topics(-1))):
topics.append(lda.show_topics(-1))
""" Format of topics to use now is topics[0][TopicNumber][1], 1 for getting words and probabilities. """

# print len(topics)
# print topics
# print topics[0][1][1]

"""Takes the string returned by LDAmodel.show_topics() """
def bow_of_topics(topic):
    # Split on strings to get topics and the probabilities
    topic = topic.split('+')
    # print topic
    topic_bow = []
    for word in topic:
        prob, word = word.split('*')  # Split probability and word
        # print word
        word = word.replace(" ", "")  # Remove the spaces
        word = word.replace('"', '')
        # print "final",
        # print word
        # print [word]
        # print "BOW is",
        # print lda.id2word.doc2bow([word])
        word = lda.id2word.doc2bow([word])[0][0]  # Convert to word_type
        topic_bow.append((word, float(prob)))
    return topic_bow


def sparse2full(doc, length):
    """
    Converts a document in sparse document format (=sequence of 2-tuples) into a dense
    numpy array (of size `length`).
    """
    result = numpy.zeros(length, dtype=numpy.float32)  # fill with zeroes (default value)
    doc = dict(doc)
    # overwrite some of the zeroes with explicit values
    result[list(doc)] = list(itervalues(doc))
    return result


"""Hellinger distance is a distance metric to quanitfy the similarity between two probability distributions.
   Similarity between distributions will be a number between <0,1>, where 0 is maximum similarity and 1 is minimum similarity.
"""
def hellinger(vec1, vec2, lda=None, bow=False, num_of_docs=None):
    """
    If the distribution draws from a certain number of docs, that value must be passed.
    If input is an LDA vector, lda model must be passed.
    If the input is in the form of bag of words, this must be mentioned.
    Input must be a sequence of 2-tuples.
    """
    if bow is True:
        vec1, vec2 = dict(vec1), dict(vec2)
        if len(vec2) < len(vec1):
            vec1, vec2 = vec2, vec1
        sim = numpy.sqrt(
            0.5 * sum((numpy.sqrt(value) - numpy.sqrt(vec2.get(index, 0.0))) ** 2 for index, value in iteritems(vec1)))
        return sim
    elif lda is None:
        if scipy.sparse.issparse(vec1) and scipy.sparse.issparse(vec2):
            vec1 = vec1.todense().tolist()
            vec2 = vec2.todense().tolist()
            max_len = max(len(vec1), len(vec2), num_of_docs)
            dense1 = sparse2full(vec1, max_len)
            dense2 = sparse2full(vec2, max_len)
            sim = numpy.sqrt(0.5 * ((numpy.sqrt(dense1) - numpy.sqrt(dense2)) ** 2).sum())
            return sim
        elif isinstance(vec1, numpy.ndarray) and isinstance(vec2, numpy.ndarray):
            vec1 = vec1.tolist()
            vec2 = vec2.tolist()
            max_len = max(len(vec1), len(vec2), num_of_docs)
            dense1 = sparse2full(vec1, max_len)
            dense2 = sparse2full(vec2, max_len)
            sim = numpy.sqrt(0.5 * ((numpy.sqrt(dense1) - numpy.sqrt(dense2)) ** 2).sum())
            return sim
        elif type(vec1) is list and type(vec2) is list:
            max_len = max(len(vec1), len(vec2), num_of_docs)
            dense1 = sparse2full(vec1, max_len)
            dense2 = sparse2full(vec2, max_len)
            sim = numpy.sqrt(0.5 * ((numpy.sqrt(dense1) - numpy.sqrt(dense2)) ** 2).sum())
            return sim
    elif isinstance(lda, gensim.models.ldamodel.LdaModel):
        dense1 = sparse2full(vec1, lda.num_topics)
        dense2 = sparse2full(vec2, lda.num_topics)
        sim = numpy.sqrt(0.5 * ((numpy.sqrt(dense1) - numpy.sqrt(dense2)) ** 2).sum())
    return sim


# topicdist0 = bow_of_topics(topics[0][1][1])
# topicdist1 = bow_of_topics(topics[1][1][1])


# if __name__ == '__main__':
#     topicdist0 = bow_of_topics(topics[0][1][1])
#     topicdist6 = bow_of_topics(topics[0][10][1])
#     topicdist4 = bow_of_topics(topics[0][17][1])
#     print topics[0][10][1]
#     print topics[0][17][1]
#     similarity = hellinger(topicdist6,topicdist4,bow=True)
#     print similarity