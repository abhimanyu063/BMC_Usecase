from data_ingestion import data_merger
from application_logging import logger

class DataPreprocessing:
    def __init__(self):
        objdata_mergers = data_merger.DataMerger()
        self.final_dataFrame = objdata_mergers.dataframe_merger()
        self.file_object = open("prediction_logs/prediction_log.txt", 'a+')
        self.log_writer = logger.App_Logger()

    def preprocessing(self):
        try:
            self.log_writer.log(self.file_object,'Start data preprocessing...!!')
            self.final_dataFrame['Returned'] = self.final_dataFrame['Returned'].apply(lambda x: 1 if x == 'Yes' else 0)
            self.log_writer.log(self.file_object,'End data preprocessing...!!')
            return self.final_dataFrame
        except Exception as ex:
            print('error', ex)
