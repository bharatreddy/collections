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
        # create the match table
        mtchStr = """
                    CREATE TABLE Match (
                        ID INT PRIMARY KEY NOT NULL,
                        Date DATE NOT NULL,
                        Type VARCHAR(50) NOT NULL,
                        Venue VARCHAR(50) NOT NULL,
                        Competition VARCHAR(50),
                        Overs FLOAT
                        )
                    """
        self.cursor.execute(mtchStr)

        self.conn.commit()