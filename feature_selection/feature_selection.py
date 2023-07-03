from feature_engineering import feature_engineering
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
import pandas as pd


class FeatureSelection:
    def __init__(self):
        objfeature_engineering = feature_engineering.FeatureEngineering()
        self.final_dataFrame = objfeature_engineering._encode_categorical_columns()

    def __split_feature(self):
        try:
            X = self.final_dataFrame.drop(['Returned'], axis=1)
            y = self.final_dataFrame['Returned']
            return X, y

        except Exception as ex:
            print('error', ex)

    def __feature_seletion(self, X, y):
        try:
            # Model based feature selection.
            model = ExtraTreesClassifier()
            # model.fit(input_feature, target)
            # plt.figure(figsize=(5,5))
            # feat_importances = pd.Series(model.feature_importances_, index= input_feature.columns)
            # feat_importances.nlargest(50).plot(kind='barh')
            # plt.show()
            
            # model = RandomForestClassifier(n_estimators= 400)
            # model.fit(input_feature, target)
            # feat_importance = model.feature_importances_
            # final_df = pd.DataFrame({'features': pd.DataFrame(input_feature).columns, 'Importance': feat_importance})
            # final_df.set_index('Importance')
            # final_df = final_df.sort_values('Importance')
            # final_df.plot.bar(color='teal')
            # plt.show()

        except Exception as ex:
            print('error', ex)

    def _drop_features(self):
        try:
            X, y = self.__split_feature()
            self.__feature_seletion(X, y)
            
            # Droping feature which is not important for model training.
            drop_cols = ['Product Name', 'Sub-Category', 'Category', 'Country']
            X.drop(columns= drop_cols, axis= 1, inplace= True)
            return X, y

        except Exception as ex:
            print('error', ex)
