"""
Calls the LDA_Preprocessor, LDA and TweetSegregator.
"""
from ExtraUseFiles.OS_Utility import get_dir

from PrimaryWorker.TopicModeller import LDA_Preprocessor
from PrimaryWorker.TopicModeller import TweetSegregator
from PrimaryWorker.TopicModeller import LDA

ROOT = get_dir(__file__)


def lda_preprocess():
    LDA_Preprocessor.execute()


def lda_process():
    LDA.execute()


def _tweet_segregation():
    TweetSegregator.execute()


if __name__ == '__main__':
    lda_preprocess()
    lda_process()
    _tweet_segregation()
