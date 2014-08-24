import datetime
from os.path import expanduser
import sys, os

class py_Time_Tracker(object):
    """
    Python Time Tracker.
    """
    def __init__(self):
        self.tracker_entry = []

    def getDate():
        return datetime.datetime.now()

    def check_folder(mFolder):
        pass

    def is_a_dir(self, mPath):
        if not os.path.isdir(mPath):
            os.makedirs(mPath)

    def start_tracking(self, entry_name):

        
