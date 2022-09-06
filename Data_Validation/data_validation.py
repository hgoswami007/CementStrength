from genericpath import isdir
import os
from Application_logging import logger
import shutil

class raw_validation:
    def __init__(self,path):
        self.Batch_Directory = path
        self.logger = logger.App_loger()

    def createDirectory(self):
        """
        This function method create directories for good data and bad data
        after validation the training data.
        """

        try:
            path = os.path.join('Training_Raw_files_validated/','Good_Raw')
            if not os.path.isdir(path):
                os.makedirs(path)
            path = os.path.join('Training_Raw_files_validated/','Bad_Raw')
            if not os.path.isdir(path):
                os.makedirs(path)
            
        except Exception as e:
            file = open('Training_Logs/GeneralLog.txt','+a')
            self.logger.log(file,'Error while creating the directory'+str(e))
            file.close()
            raise Exception()

    def deleteDirectory(self):
        """
        This function method delete directories for good data and bad data
        after validation the training data.
        """ 

        try:
            path = os.path.join('Training_Raw_files_validated/')
            file = open('Training_Logs/GeneralLog.txt','a+')
            if os.path.isdir(path + 'Good_Raw/'):
                shutil.rmtree(path + 'Good_Raw/')
                self.logger.log(file,'GoodRaw directory deleted successfully')
            elif os.path.isdir(path + 'Bad_Raw/'):
                shutil.rmtree(path + 'Bad_Raw/')
                self.logger.log(file,'Bad_Raw directory deleted successfully')
            file.close()

        except Exception as e:
            file = open('Training_Logs/GeneralLog.txt','a+')
            self.logger.log(file,'Exception occurs directory could not delete successfully'+ str(e))
            raise Exception()





    def validation_file(self):
        """
        This function validate the training file.
        """
        self.deleteDirectory()
        self.createDirectory()
        onlyfile = [f for f in os.listdir(self.Batch_Directory)]
        try:
            f = open("Training_Logs/FileValidation.txt","a+")
            for filename in onlyfile:
                splitDot = filename.split('.')
                # print('SplitDot=====>',splitDot)
                if splitDot[1] == 'csv':
                    shutil.copy('Trining_Batch_file/' + filename, 'Training_Raw_files_validated/Good_Raw')
                    self.logger.log(f,'Valid File extention!! File moved to Good Raw Folder')
                    
                else:
                    shutil.copy('Trining_Batch_file/' + filename, 'Training_Raw_files_validated/Bad_Raw')
                    self.logger.log(f,'InValid File extention!! File moved to Bad Raw Folder')
            f.close()
        except Exception as e:
            raise Exception()



