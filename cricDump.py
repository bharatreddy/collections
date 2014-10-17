import yaml
import os
# Directory of ipl data
iplDir = '/Users/bharat/Desktop/cric/ipl/'
# get all the 'yaml' files in the directory
iplFiles = [ f for f in os.listdir(iplDir) \
if os.path.isfile(os.path.join(iplDir,f)) and 'yaml' in f ]
# Loop throught the files and parse them.
for i in iplFiles:
    print i
    break