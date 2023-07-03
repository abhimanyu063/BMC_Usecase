import pandas as pd
import json
import os
from application_logging import logger


class Data_Getter:
    def __init__(self):
        self.file_object = open("prediction_logs/prediction_log.txt", 'a+')
        self.log_writer = logger.App_Logger()

    def json_load(self, file_path):
        try:
            self.log_writer.log(self.file_object,'Start loading json file...!!')
            df = pd.DataFrame()
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
                df.drop(columns=['index'], inplace=True)
                return df

        except Exception as ex:
            print('error', ex)

