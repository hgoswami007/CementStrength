import pandas as pd

class data_getter():
    """
    This class shall be used for obtaining the data from the source for training.
    """ 

    def __init__(self,file_object,logger_object):
        self.training_file = 'Training_FileFromDB/InputFile.csv'
        self.file_object = file_object
        self.logger_object = logger_object

    def get_data(self):
        """
        This methods read the data from source
        """

        self.logger_object.log(self.file_object,'Enter the get_data method of the data_getter class')
        try:
            self.data = pd.read_csv(self.training_file)
            self.logger_object.log(self.file_object,'Data Load successfully')
            print(self.data.head())
            return self.data
        except Exception as e:
            self.logger_object.log(self.file_object,'Excecption occured in get data method' + str(e))
            self.logger_object.log(self.file_object,'Data Load unsuccessfull')            

            return Exception()

