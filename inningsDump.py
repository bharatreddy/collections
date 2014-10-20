if __name__ == "__main__":
    import inningsDump
    dbo = inningsDump.InnData()
    dbo.populate_tables(iplData=True)

class InnData(object):
    """
    A utilities class to populate innings/deliveries data from the yaml files to the DB.
    """

    def __init__(self):
        import mysql.connector
        # set up connections to the DB
        self.conn = mysql.connector.Connect(host='localhost',user='root',\
                                password='',database='cricdata')
        self.cursor = self.conn.cursor()

    def populate_tables(self, iplData=False, allData=False):
        """
        popluate ipl data into main tables

        #### INPUTS ####
        iplData : populate data from ipl matches folder
        allData : populate data from all matches folder
        #### INPUTS ####
        """
        import yaml
        import os
        # Directory of ipl data
        iplDir = '/Users/bharat/Desktop/cric/ipl/'
        allDir = '/Users/bharat/Desktop/cric/all/'
        # get all the 'yaml' files in the directory
        cricFiles = []
        # we also need a list of the file names (not including the dir)
        fnList = []
        if iplData:
            iplFiles = [ iplDir+f for f in os.listdir(iplDir) \
            if os.path.isfile(os.path.join(iplDir,f)) and 'yaml' in f ]
            fnList += [ f for f in os.listdir(iplDir) \
            if os.path.isfile(os.path.join(iplDir,f)) and 'yaml' in f ]
            cricFiles += iplFiles
        if allData:
            allFiles = [ allDir+f for f in os.listdir(allDir) \
            if os.path.isfile(os.path.join(allDir,f)) and 'yaml' in f ]
            fnList += [ f for f in os.listdir(allDir) \
            if os.path.isfile(os.path.join(allDir,f)) and 'yaml' in f ]
            cricFiles += allFiles
        # Loop throught the files and parse them.
        loopCntr = 1 # just a counter to keep track of num files looped
        for i,j in zip(cricFiles,fnList):
            print "curr File->", j, loopCntr
            loopCntr += 1
            stream = open(i, 'r')
            matchDict = yaml.load(stream)
            print len(matchDict['innings'])
            print matchDict['innings'][1].keys()
            print matchDict['innings'][0]['1st innings']['deliveries'][10]
            # print matchDict['innings'][0]['2nd innings']['deliveries'], matchDict['innings'][0]['2nd innings']['team']
            break
