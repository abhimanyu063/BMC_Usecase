from data_ingestion import data_merger
from application_logging import logger

class DataPreprocessing:
    def __init__(self):
        self.file_object = open("prediction_logs/prediction_log.txt", 'a+')
        self.error_file_object = open("error_logs/error_log.txt", 'a+')
        self.log_writer = logger.App_Logger()

    def _preprocessing(self):
        """ Method Name: preprocessing
            Description: This function is doing preprocessing the data.
            Output: return final DataFrame
            On Failure: Logging exception in error log file """
        try:
            objdata_mergers = data_merger.DataMerger()
            self.final_dataFrame = objdata_mergers._dataframe_merger()

            self.log_writer.log(self.file_object,'Start data preprocessing...!!')
            self.final_dataFrame['Target'] = self.final_dataFrame['Product Name'].apply(lambda x: 1 if 'Printer' in x else 0)
            self.log_writer.log(self.file_object,'End data preprocessing...!!')
            return self.final_dataFrame
        
        except Exception as ex:
            self.log_writer.log(self.error_file_object, str(ex), 'Class - ' +__class__.__name__+ '')
