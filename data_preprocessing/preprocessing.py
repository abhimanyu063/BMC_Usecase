from data_ingestion import data_merger

class DataPreprocessing:
    def __init__(self):
        objdata_mergers = data_merger.DataMerger()
        self.final_dataFrame = objdata_mergers.dataframe_merger()
        

    def preprocessing(self):
        try:
            self.final_dataFrame['Returned'] = self.final_dataFrame['Returned'].apply(lambda x: 1 if x == 'Yes' else 0)
            return self.final_dataFrame
        except Exception as ex:
            print('error', ex)
