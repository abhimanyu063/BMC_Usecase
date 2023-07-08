import pandas as pd
import json
import os
from application_logging import logger

class Data_Getter:
    def __init__(self):
        # Handling prediction logs.
        self.file_object = open("prediction_logs/prediction_log.txt", 'a+')
        # Handling error logs.
        self.error_file_object = open("error_logs/error_log.txt", 'a+')
        # Logs class object.
        self.log_writer = logger.App_Logger()

    def json_load(self, file_path):
        """ Method Name: json_load
            Description: This function is loading json file and convert json into pandas dataframe.
            Output: return DataFrame
            On Failure: Logging exception in error log file """
        try:
            self.log_writer.log(self.file_object,'Start loading json file...!!')
            with open(file_path, 'r+') as json_files:
                json_data = json.load(json_files)
            
            self.log_writer.log(self.file_object,'Loaded json file - '+ os.path.basename(file_path).split('/')[-1] +'')

            if os.path.basename(file_path).split('/')[-1] == 'customer_transaction_info.json':
                df = pd.DataFrame(json_data['data'], columns=json_data['columns'])
                return df
            
            elif os.path.basename(file_path).split('/')[-1] == 'customers_info.json':
                df = pd.DataFrame(json_data)
                return df
            
            elif os.path.basename(file_path).split('/')[-1] == 'orders_returned_info.json':
                df = pd.DataFrame(json_data).transpose()
                return df
            
            elif os.path.basename(file_path).split('/')[-1] == 'product_info.json':
                df = pd.DataFrame(json_data['data'])
                df.drop(columns=['index'], axis=1, inplace=True)
                return df

        except Exception as ex:
            self.log_writer.log(self.error_file_object, str(ex), 'Class - ' +__class__.__name__+ '')

