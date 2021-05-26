####################### Restructure data ############################
# StudentID(1,21) -> theme(anger,student_well_being, network,       #
#                    climate_change, impuls, garbage_is_nonexistent)#
#                 -> photos numbered (1,567).                       #
################ ONLY RUN ONCE OR IT OVERWRITES #####################
import os

rootdir = '/home/tim/Documents/scriptie/data'
photonumber = 0
for i in range(1,22):
    student = i
    studentdir = rootdir + '/' + str(i)
    for subdir, dirs, files in os.walk(studentdir):
        if subdir is not studentdir:
            for file in files:
                old = subdir + '/' + str(file)
                new = subdir + '/' + str(photonumber) + '.' + file.split(".")[-1]
                os.rename(old, new)
                photonumber += 1