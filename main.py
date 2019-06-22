from logHelper import ExecuteWithLogs
from preprocessingHelper import PerformPreprocessing
import os
import sys

os.chdir("./data")
log_file_path = "log.txt"
ExecuteWithLogs("Preprocessing", log_file_path, lambda _ = None: PerformPreprocessing(log_file_path))   

