from logHelper import ExecuteWithLogs
from preprocessingHelper import PerformPreprocessing, SliceListEvenly
import os
import sys
import _thread

os.chdir("./data")
log_file_path = "log.txt"
files = list(SliceListEvenly(list(filter(lambda x: x.endswith(".raw"), os.listdir("."))), 2))   
for files_sublist in files:
    _thread.start_new_thread(ExecuteWithLogs("Preprocessing", log_file_path, lambda _ = None: PerformPreprocessing(files_sublist, log_file_path)))   

