from os import listdir
from Application_logging import logger
import pandas as pd

class dataTransfor:
    
    """
    This class shall be used for transforming the Good raw Training data before loading it in database!!
    """

    def __init__(self):
        self.goodDataPath = 'Training_Raw_files_validated/Good_Raw'
        self.logger = logger.App_loger()

    def replaceMissingWithNull(self):

        """
        This method replace missing value with null value.
        """
        file = open('Training_Logs/dataTransformLog.txt','+a')
        try:
            onlyFiles = [f for f in listdir(self.goodDataPath)]
            for files in onlyFiles:
                csv = pd.read_csv(self.goodDataPath +"/"+files)
                csv.fillna('NULL',inplace=True)
            self.logger.log(file,'File Transform successfull!!')
        
        except Exception as e:
            self.logger.log(file,'Data Transformation failed!!')
            raise Exception()

        file.close()


    