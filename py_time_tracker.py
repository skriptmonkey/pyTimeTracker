import time, math, sys, os
from os.path import expanduser

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

    def format_time(num):
        num = math.floor(num)
        if x < 10:
            str_num = "0" + str(num)
        else:
            str_num = str(num)
        return str_num

    def start_tracking(self, entry_name):
        print("Starting " + entry_name)
        start = time.perf_counter()
        input("Press enter to stop " + entry_name + "...")
        elapsed = (time.perf_counter() - start)

        elapsed_time = format_time(elapsed/60) + ":" + format_time(elapsed%60)

