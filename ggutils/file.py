# Copyright 2018-2019 Geek Guild Co., Ltd.
# ==============================================================================

import os
from ggutils.gg_verbosity import GGVerbosePrinting

GGPrint = GGVerbosePrinting(2)

def find_all_files_and_dirs(target_directory):
    for root, dirs, files in os.walk(target_directory):
        yield root
        for file in files:
            yield os.path.join(root, file)


if __name__ == '__main__':
    GGPrint.print('file_util')
    GGPrint.print('e.g. find_all_files_and_dirs in the current dir')

    target_directory = './'
    try:
        for file in find_all_files_and_dirs(target_directory):
            GGPrint.print('find file or dir:{}'.format(file))

    except FileNotFoundError:
        GGPrint.print('FileNotFound in the current dir')

