from data_preprocessing import preprocessing
from application_logging import logger
import numpy as np
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt

class FeatureEngineering:
    def __init__(self) -> None:
       
        self.file_object = open("prediction_logs/prediction_log.txt", 'a+')
        self.error_file_object = open("error_logs/error_log.txt", 'a+')
        self.log_writer = logger.App_Logger()

    def __droping_feature(self):
        """ Method Name: __droping_feature
            Description: This function is dropping the feature which is not relevant to models.
            Output: return DataFrame
            On Failure: Logging exception in error log file """
        try:
            objDataPrepro = preprocessing.DataPreprocessing()
            self.final_dataFrame = objDataPrepro._preprocessing()

            self.log_writer.log(self.file_object,'Start dropping features...!!')
            drop_cols = ['Order ID', 'Order Date', 'Ship Date', 'Customer ID',
                         'Product ID', 'Customer Name', 'Postal Code', 'Returned', 'Product Name']
            self.final_dataFrame.drop(columns= drop_cols, axis= 1, inplace= True)
            self.log_writer.log(self.file_object,'Droped features...!!')
            return self.final_dataFrame

        except Exception as ex:
            self.log_writer.log(self.error_file_object, str(ex), 'Class - ' +__class__.__name__+ '')

    def _encode_categorical_columns(self):
        """ Method Name: _encode_categorical_columns
            Description: This function is doing categorical imputation.
            Output: return DataFrame
            On Failure: Logging exception in error log file """
        try:
            self.log_writer.log(self.file_object,'Start encoding categorical features...!!')
            self.encoding_cat_feature = self.__droping_feature()
            # Removing outliers
            self.__handle_outlier(self.final_dataFrame, ['Sales', 'Profit'])

            label_encoder = LabelEncoder()
            label_encoder.fit(self.encoding_cat_feature['Ship Mode'])
            self.encoding_cat_feature['Ship Mode'] = label_encoder.transform(self.encoding_cat_feature['Ship Mode'])

            label_encoder.fit(self.encoding_cat_feature['Segment'])
            self.encoding_cat_feature['Segment'] = label_encoder.transform(self.encoding_cat_feature['Segment'])

            label_encoder.fit(self.encoding_cat_feature['Region'])
            self.encoding_cat_feature['Region'] = label_encoder.transform(self.encoding_cat_feature['Region'])

            label_encoder.fit(self.encoding_cat_feature['Category'])
            self.encoding_cat_feature['Category'] = label_encoder.transform(self.encoding_cat_feature['Category'])

            label_encoder.fit(self.encoding_cat_feature['Sub-Category'])
            self.encoding_cat_feature['Sub-Category'] = label_encoder.transform(self.encoding_cat_feature['Sub-Category'])

            label_encoder.fit(self.encoding_cat_feature['State'])
            self.encoding_cat_feature['State'] = label_encoder.transform(self.encoding_cat_feature['State'])

            label_encoder.fit(self.encoding_cat_feature['City'])
            self.encoding_cat_feature['City'] = label_encoder.transform(self.encoding_cat_feature['City'])

            label_encoder.fit(self.encoding_cat_feature['Country'])
            self.encoding_cat_feature['Country'] = label_encoder.transform(self.encoding_cat_feature['Country'])
            
            self.log_writer.log(self.file_object,'End encoding categorical features...!!')
            return self.encoding_cat_feature

        except Exception as ex:
            self.log_writer.log(self.error_file_object, str(ex), 'Class - ' +__class__.__name__+ '')

    def __handle_outlier(self, df, cols):
        """ Method Name: __handle_outlier
            Description: This function is removing outlier.
            Output: return None
            On Failure: Logging exception in error log file """
        try:
            for i in cols:

                Q1 = df[cols].quantile(0.25)
                Q3 = df[cols].quantile(0.75)
                IQR = Q3 - Q1
                upper_limit = Q3 + 1.5 * IQR
                lower_limit = Q1 - 1.5 * IQR
                df[df[cols] > upper_limit]
                df[df[cols] < lower_limit]
                df[cols] = np.where(
                    df[cols] > upper_limit,
                    upper_limit,
                    np.where(
                    df[cols] < lower_limit,
                    lower_limit,
                    df[cols]
                    )
                )
                
        except Exception as ex:
            self.log_writer.log(self.error_file_object, str(ex), 'Class - ' +__class__.__name__+ '')

    def __check_outlier(self, df, cols):
            try:
                for c in cols:
                    sns.boxplot(y=df[cols], data=df, color='b')
                    plt.show()

            except Exception as ex:
                self.log_writer.log(self.error_file_object, str(ex), 'Class - ' +__class__.__name__+ '')