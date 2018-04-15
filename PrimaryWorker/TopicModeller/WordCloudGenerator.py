from os.path import join

from gensim import models
from pytagcloud import create_tag_image, make_tags
from pytagcloud.colors import COLOR_SCHEMES
from pytagcloud.lang.counter import get_tag_counts

from ExtraUseFiles.Constants import *
from ExtraUseFiles.OS_Utility import get_dir
from ExtraUseFiles.DateTimeController import start_timing, stop_timing, get_today, get_date_string, get_time

TODAY = get_today()
TODAY_STRING = get_date_string(TODAY)

ROOT = get_dir(__file__)
PROJECT_ROOT = get_dir(get_dir(ROOT))

LDA_PATH = join(ROOT, DICT_CORPUS_MODEL_DIR, LDA_MODEL_PREFIX + TODAY_STRING + LDA)
MODEL_DATA_PATH = join(ROOT, TOPICS_DATA_DIR)
WORDCLOUD_PATH = join(ROOT, TOPICS_DATA_DIR)

LDA_MODEL = models.LdaModel.load(LDA_PATH)


def normalize(arr):
    sum = 0
    for i in arr:
        sum += i
    for i in range(len(arr)):
        arr[i] = arr[i]/sum


def create_wordcloud(topic_id):
    word_tuples = LDA_MODEL.show_topic(topic_id, 20)
    # array of words with their frequencies
    words_arr = []
    freq_arr = []
    for word_tuple in word_tuples:
        try:
            word = str(word_tuple[0])
            words_arr.append(word)
            freq_arr.append(word_tuple[1])

        except:
            continue
    print words_arr
    normalize(freq_arr)
    print freq_arr
    #Generating word cloud
    word_count = len(words_arr)
    text = ""
    counts = []
    for i in range(word_count):
        counts.append((words_arr[i], int(freq_arr[i]*100)))
    for i in range(0, word_count):
        for j in range(0, (int)(freq_arr[i] * 100)):
            text = text + words_arr[i] + " "

    tags = make_tags(counts, minsize=20, maxsize=60, colors=COLOR_SCHEMES['audacity'])

    output = join(WORDCLOUD_PATH, 'cloud' + str(topic_id) + '.png')

    create_tag_image(tags=tags, output=output,
                     size=(500, 333),
                     background=(255, 255, 255, 255),
                     layout=3, fontname='PT Sans Regular', rectangular=True)


def execute():
    print 'Started Word Cloud Generation at ' + get_time() + '...\n',
    start_timing()

    hot_topics = [1,2,3,4,5,6,7, 8,9,10,11,12,13,14,15,16, 17]
    for topic in hot_topics:
        create_wordcloud(topic)
    print 'Word Cloud Successfully Created'
    stop_timing()


if __name__ == '__main__':
    execute()