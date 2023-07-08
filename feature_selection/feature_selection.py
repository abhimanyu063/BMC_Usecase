from feature_engineering import feature_engineering
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
import pandas as pd
from application_logging import logger


class FeatureSelection:
    def __init__(self):
        self.file_object = open("prediction_logs/prediction_log.txt", 'a+')
        self.error_file_object = open("error_logs/error_log.txt", 'a+')
        self.log_writer = logger.App_Logger()

    def __split_feature(self):
        """ Method Name: __split_feature
            Description: This function is splitting feature into X and y for training the model.
            Output: return X, y
            On Failure: Logging exception in error log file """
        try:
            objfeature_engineering = feature_engineering.FeatureEngineering()
            self.final_dataFrame = objfeature_engineering._encode_categorical_columns()
            
            self.log_writer.log(self.file_object,'Start spliting features as X and y...!!')
            X = self.final_dataFrame.drop(['Target'], axis=1)
            y = self.final_dataFrame['Target']
            self.log_writer.log(self.file_object,'End spliting features as X and y...!!')
            return X, y

        except Exception as ex:
            self.log_writer.log(self.error_file_object, str(ex), 'Class - ' +__class__.__name__+ '')

    def __feature_seletion(self, X, y):
        """ Method Name: __feature_seletion
            Description: This function is selecting the important features for model building.
            Output: return important feature in terms of plotting graph.
            On Failure: Logging exception in error log file """
        try:
            self.log_writer.log(self.file_object,'Start features selection based on ExtraTreesClassifier...!!')
            # Model based feature selection.
            model = ExtraTreesClassifier()
            # model.fit(input_feature, target)
            # plt.figure(figsize=(5,5))
            # feat_importances = pd.Series(model.feature_importances_, index= input_feature.columns)
            # feat_importances.nlargest(50).plot(kind='barh')
            # plt.show()
            self.log_writer.log(self.file_object,'End features selection based on ExtraTreesClassifier...!!')

            self.log_writer.log(self.file_object,'Start features selection based on RandomForestClassifier...!!')
            # model = RandomForestClassifier(n_estimators= 400)
            # model.fit(input_feature, target)
            # feat_importance = model.feature_importances_
            # final_df = pd.DataFrame({'features': pd.DataFrame(input_feature).columns, 'Importance': feat_importance})
            # final_df.set_index('Importance')
            # final_df = final_df.sort_values('Importance')
            # final_df.plot.bar(color='teal')
            # plt.show()
            self.log_writer.log(self.file_object,'End features selection based on RandomForestClassifier...!!')

        except Exception as ex:
            self.log_writer.log(self.error_file_object, str(ex), 'Class - ' +__class__.__name__+ '')

    def _drop_features(self):
        """ Method Name: _drop_features
            Description: This function is dropping the unnecessary features after using feature selection algorithms.
            Output: return important feature in terms of X and y.
            On Failure: Logging exception in error log file."""
        try:
            X, y = self.__split_feature()
            self.__feature_seletion(X, y)
            self.log_writer.log(self.file_object,'Start feature dropping which is not relevant to model...!!')
            # Droping feature which is not important for model training.
            drop_cols = ['Sub-Category', 'Category', 'Country']
            X.drop(columns= drop_cols, axis= 1, inplace= True)
            self.log_writer.log(self.file_object,'Dropped features which is not relevant to model')
            return X, y

        except Exception as ex:
            self.log_writer.log(self.error_file_object, str(ex), 'Class - ' +__class__.__name__+ '')
