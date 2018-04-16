from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from ExtraUseFiles.TuningParameters import NUMBER_OF_TOPICS
import re
from os.path import join
from ExtraUseFiles.DateTimeController import start_timing, stop_timing, get_time

TopicFilesPath = join('/home/yagyansh/AnalysisOfTwitterHashtags/PrimaryWorker/TopicModeller/ResultingTopics/')
FIRST_LINE = 23
top_tweets = []
temporary_topics = [] #List of lists(of every topic file)
indexofentities = []

def extract_top_tweets():
    for i in range(NUMBER_OF_TOPICS):
        with open(join(TopicFilesPath,'Topic%d.txt' %(i))) as input_data:
           temporary_topics.append(input_data.readlines())

    for i in range(len(temporary_topics)):
        indexofentities.append(temporary_topics[i].index('Entities:\n'))

    for i in range(len(temporary_topics)):
        array = temporary_topics[i][FIRST_LINE:indexofentities[i]]
        lala = ''.join(array)
        top_tweets.append(re.sub('[^ a-zA-Z0-9]', '', lala))


def tfidf_vector_similarity(sentence_1, sentence_2):
    corpus = [sentence_1, sentence_2]
    vectorizer = TfidfVectorizer(min_df=1)
    vec_1 = vectorizer.fit_transform(corpus).toarray()[0]
    vec_2 = vectorizer.fit_transform(corpus).toarray()[1]
    sim = np.dot(vec_1, vec_2.T) / (np.linalg.norm(vec_1) * np.linalg.norm(vec_2))
    return sim

if __name__ == '__main__':
    print 'Started Calculating TFIDF Similarity at ' + get_time() + '... ',
    start_timing()

    extract_top_tweets()
    filehandler = open('TFIDFSimilarities.txt', 'a')
    for i in range(len(top_tweets)):
        for j in range(len(top_tweets)):
            filehandler.write("Similarity between %d and %d is - " % (i, j) + str(
                tfidf_vector_similarity(top_tweets[i], top_tweets[j])) + "\n")

    print '\nFinished at  ' + get_time()
    stop_timing()

