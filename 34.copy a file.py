# copyfile() = copies contents of a file
# copy() = copyfile()+permission mode + destination can be a directory
# copy2 = copy()+copies metadata(File's creation and modification times)

import shutil

shutil.copyfile("test.txt","copy.txt") #source, destination


# import shutil
#
# shutil.copyfile("test.txt","C:\\Users\\User\\Desktop\\copy.txt") #source, destination