"""
Calls the PreProcessor.py and then calls EntityAggregator.py
"""

from os.path import join
from ExtraUseFiles.Constants import *
from ExtraUseFiles.OS_Utility import get_dir
import sys
sys.path.insert(0, '/home/yagyansh/AnalysisOfTwitterHashTags/PrimaryWorker/DataProcessor')

from PreProcessor import execute
from EntityAggregator import Execute

ROOT = get_dir(__file__)

PREPROCESS_SCRIPT_PATH = join(ROOT, PREPROCESSOR)
POSTPROCESS_SCRIPT_PATH = join(ROOT, ENTITYAGGREGATOR)


def data_preprocess():
    execute()


def data_postprocess():
    Execute()


if __name__ == '__main__':
    data_preprocess()
    data_postprocess()
