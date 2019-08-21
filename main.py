from logHelper import ExecuteWithLogs
from preprocessingHelper import PerformPreprocessing, PerformPreprocessingForSingleFile, CalculateMaskSizeLevels
import os
import sys
import _thread

os.chdir("./data")
log_file_path = "log.txt"
files = list(filter(lambda x: x.endswith(".raw"), os.listdir(".")))  
#for file in files:
    #_thread.start_new_thread(ExecuteWithLogs("Preprocessing for {0}".format(file), log_file_path, lambda _ = None: PerformPreprocessingForSingleFile(file, log_file_path)))   
print(ExecuteWithLogs("Masks sizes calculation", log_file_path, lambda _ = None: CalculateMaskSizeLevels(20)))

