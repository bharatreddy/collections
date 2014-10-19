if __name__ == "__main__":
    import cricDB
    dbo = cricDB.DbUtils()
    dbo.create_main_tables()
    dbo.close()

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
        import mysql.connector
        # create the Match table
        mtchStr = """
                    CREATE TABLE Game(
                        Id INT NOT NULL,
                        MatchDate DATETIME NOT NULL,
                        Type VARCHAR(50) NOT NULL,
                        Venue VARCHAR(50) NOT NULL,
                        Competition VARCHAR(50),
                        Overs FLOAT,
                        PRIMARY KEY (Id)
                        )
                    """
        self.cursor.execute(mtchStr)
        # create the Toss table
        tossStr = """
                    CREATE TABLE Toss(
                        MatchId INT NOT NULL,
                        Winner VARCHAR(100) NOT NULL,
                        Decision VARCHAR(50) NOT NULL,
                        FOREIGN KEY (MatchId) REFERENCES Game(Id)
                        )
                    """
        self.cursor.execute(tossStr)
        # create the Teams table
        teamsStr = """
                    CREATE TABLE Teams(
                        MatchId INT NOT NULL,
                        Team1 VARCHAR(100) NOT NULL,
                        Team2 VARCHAR(100) NOT NULL,
                        FOREIGN KEY (MatchId) REFERENCES Game(Id)
                        )
                    """
        self.cursor.execute(teamsStr)
        # create the Umpires table
        umpiresStr = """
                    CREATE TABLE Umpires(
                        MatchId INT NOT NULL,
                        Umpire1 VARCHAR(100) NOT NULL,
                        Umpire2 VARCHAR(100) NOT NULL,
                        FOREIGN KEY (MatchId) REFERENCES Game(Id)
                        )
                    """
        self.cursor.execute(umpiresStr)
        # create the PlayerOfMatch table
        playerOfMatchStr = """
                    CREATE TABLE PlayerOfMatch(
                        MatchId INT NOT NULL,
                        Player VARCHAR(100) NOT NULL,
                        FOREIGN KEY (MatchId) REFERENCES Game(Id)
                        )
                    """
        self.cursor.execute(playerOfMatchStr)
        # create the Outcome table
        outComeStr = """
                    CREATE TABLE Outcome(
                        MatchId INT NOT NULL,
                        Winner VARCHAR(100) NOT NULL,
                        Innings INT NULL,
                        Runs INT NULL,
                        Wickets INT NULL,
                        FOREIGN KEY (MatchId) REFERENCES Game(Id)
                        )
                    """
        self.cursor.execute(outComeStr)
        self.conn.commit()

    def close(self):
        """
        Disconnect from DB
        """
        self.cursor.close()
        self.conn.close()