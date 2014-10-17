import yaml
import os
# Directory of ipl data
iplDir = '/Users/bharat/Desktop/cric/ipl/'
# get all the 'yaml' files in the directory
iplFiles = [ f for f in os.listdir(iplDir) \
if os.path.isfile(os.path.join(iplDir,f)) and 'yaml' in f ]
# Loop throught the files and parse them.
for i in iplFiles:
    stream = open(iplDir+i, 'r')
    matchDict = yaml.load(stream)
    print "--------------info--------------"
    print matchDict['info'].keys()
    print "--------------info--------------"
    print "--------------info-city--------------"
    print matchDict['info']['city']
    print "--------------info-city--------------"
    print "--------------info-dates--------------"
    print matchDict['info']['dates']
    print "--------------info-dates--------------"
    print "--------------info-match_type--------------"
    print matchDict['info']['match_type']
    print "--------------info-match_type--------------"
    print "--------------info-toss--------------"
    print matchDict['info']['toss']
    print "--------------info-toss--------------"
    print "--------------info-venue--------------"
    print matchDict['info']['venue']
    print "--------------info-venue--------------"
    print "--------------info-competition--------------"
    print matchDict['info']['competition']
    print "--------------info-competition--------------"
    print "--------------info-teams--------------"
    print matchDict['info']['teams']
    print "--------------info-teams--------------"
    print "--------------info-umpires--------------"
    print matchDict['info']['umpires']
    print "--------------info-umpires--------------"
    print "--------------info-player_of_match--------------"
    print matchDict['info']['player_of_match']
    print "--------------info-player_of_match--------------"
    print "--------------info-outcome--------------"
    print matchDict['info']['outcome']
    print "--------------info-outcome--------------"
    print "--------------info-overs--------------"
    print matchDict['info']['overs']
    print "--------------info-overs--------------"
    break