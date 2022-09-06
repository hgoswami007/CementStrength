from flask import Flask,render_template
from flask_cors import cross_origin
from Application_logging import logger
from Data_Validation import data_validation
from dbOperation.dbOperation import dbOperation
# from data_ingestion import data_loader
app = Flask(__name__)


@app.route('/',methods=['GET'])
@cross_origin()
def homepage():
    # logger_object = logger.App_loger()
    # file_object = open('log.txt','a+')
    # getdata = data_loader.data_getter(file_object,logger_object)
    # getdata.get_data()
    # model = data_validation.raw_validation('D:\CementStrength\Training_FileFromDB')
    # model.validation_file()
    model = dbOperation()
    model.createTable('cementdata',['id','name'])
    return render_template('index.html')

PORT = 5000
if (__name__) == "__main__":
    print(f"The Application is running on: {PORT} ")
    app.run()



