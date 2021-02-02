# s3_access.py
# S3 Access module
# Copyright 2018-2020 Geek Guild Co., Ltd.
#


import os
from pathlib import Path
import argparse

# from ggutils import get_logger_module

# logger = get_logger_module()

class GGVerbosePrinting:
    
    def __init__(self, verbosity = None):
        self.verbosity = verbosity
        if verbosity == None:
            self.verbosity = 3
        self.default_verbosity = 0
    
    def print(self, data, verbosity_threshold = None):
        if verbosity_threshold == None:
            verbosity_threshold = self.default_verbosity
        if self.verbosity >= verbosity_threshold:
            print('{}'.format(data))


if __name__ == '__main__':
    verbose_test = GGVerbosePrinting(2)
    verbose_test.print("verbosity mapped 0",0)
    verbose_test.print("verbosity mapped 1",1)
    verbose_test.print("verbosity mapped 2",2)
    verbose_test.print("verbosity mapped 3",3)