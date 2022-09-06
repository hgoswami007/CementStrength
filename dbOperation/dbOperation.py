from Application_logging import logger
import sqlite3
class dbOperation:
    """
    This class shall be used for database operation.
    """

    def __init__(self):
        self.logger = logger.App_loger()

    def databaseConnection(self,databasename):
        """
        This method creates the database with the given name and if Database already exists then opens the connection to the DB.
        """
        try:
            conn = sqlite3.connect(databasename+'.db')
            file = open('Training_Logs/databaseLog.txt','+a')
            self.logger.log(file,'Database connection successfully')
            file.close()
        except Exception as e:
            file = open('Training_Logs/databaseLog.txt','+a')
            self.logger.log(file,'Exception occured. Error While connecting the database')
            file.close()
            raise Exception()

    def createTable(self,databasename,column_names):
        """
        """
        try:
            conn = self.databaseConnection(databasename)
            # cur = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS Good_Raw_Data;')

            for key in column_names.keys():
                type = column_names[key]
                try:
                    conn.execute('ALTER TABLE Good_Raw_data ADD COLUMN {column_name}'.format(column_names=key,dtype=type))
                except:
                    conn.execute('CREATE TABLE Good_Raw_data ({column_name} {datatype})'.format(column_names=key,datatype=type))
            conn.execute('select * from Good_Raw_data')
            conn.close()
        except Exception as e:
            raise Exception()
        
        