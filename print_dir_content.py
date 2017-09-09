"""
show all the content of the director
"""
import os

class Solution(object):
    def print_dir_content(self, dirPath):
        if os.listdir(dirPath) is not None:
            dirChildPath = os.path.join(dirPath, dirChildPath)
            if os.isdir(dirChildPath):
                print_dir_content(self, dirChildPath)
            else:
                print(dirChildPath)

