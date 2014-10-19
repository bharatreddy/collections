if __name__ == "__main__":
    import cricDB
    dbo = cricDB.DbUtils()


class DbUtils(object):
    """
    A utilities class to store/retrieve data into/from the mysql Db
    """

    def __init__(self):
        import mysql.connector
        # set up connections to the DB
        self.conn = mysql.connector.Connect(host='localhost',user='root',\
                                password='',database='cricdata')
        self.cursor = self.conn.cursor()

    def create_main_tables(self):
        # create the Match table
        mtchStr = """
                    CREATE TABLE Match (
                        Id INT PRIMARY KEY NOT NULL,
                        Date DATE NOT NULL,
                        Type VARCHAR(50) NOT NULL,
                        Venue VARCHAR(50) NOT NULL,
                        Competition VARCHAR(50),
                        Overs FLOAT
                        )
                    """
        self.cursor.execute(mtchStr)
        # create the Toss table
        tossStr = """
                    CREATE TABLE Toss (
                        MatchId INT ,
                        Winner VARCHAR(100) NOT NULL,
                        Decision VARCHAR(50) NOT NULL,
                        FOREIGN KEY (MatchId) REFERENCES Match(Id)
                        )
                    """
        self.cursor.execute(tossStr)
        # create the Teams table
        teamsStr = """
                    CREATE TABLE Teams (
                        MatchId INT ,
                        Team1 VARCHAR(100) NOT NULL,
                        Team2 VARCHAR(100) NOT NULL,
                        FOREIGN KEY (MatchId) REFERENCES Match(Id)
                        )
                    """
        self.cursor.execute(teamsStr)
        # create the Umpires table
        umpiresStr = """
                    CREATE TABLE Umpires (
                        MatchId INT ,
                        Umpire1 VARCHAR(100) NOT NULL,
                        Umpire2 VARCHAR(100) NOT NULL,
                        FOREIGN KEY (MatchId) REFERENCES Match(Id)
                        )
                    """
        self.cursor.execute(umpiresStr)
        # create the PlayerOfMatch table
        playerOfMatchStr = """
                    CREATE TABLE PlayerOfMatch (
                        MatchId INT ,
                        Player VARCHAR(100) NOT NULL,
                        FOREIGN KEY (MatchId) REFERENCES Match(Id)
                        )
                    """
        self.cursor.execute(playerOfMatchStr)
        # create the Outcome table
        outComeStr = """
                    CREATE TABLE Outcome (
                        MatchId INT ,
                        Winner VARCHAR(100) NOT NULL,
                        Innings INT NULL,
                        Runs INT NULL,
                        Wickets INT NULL,
                        FOREIGN KEY (MatchId) REFERENCES Match(Id)
                        )
                    """
        self.cursor.execute(playerOfMoutComeStratchStr)
        self.conn.commit()