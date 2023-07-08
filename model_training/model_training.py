from feature_selection import feature_selection
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc, roc_auc_score
from sklearn.ensemble import RandomForestClassifier
import xgboost as Xgb
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from application_logging import logger
import warnings
warnings.filterwarnings('ignore')

class ModelTraining:
    def __init__(self):
        self.file_object = open("prediction_logs/prediction_log.txt", 'a+')
        self.error_file_object = open("error_logs/error_log.txt", 'a+')
        self.log_writer = logger.App_Logger()

    def model_train(self):
        """ Method Name: model_train
            Description: This function is doing model training, standard scalling, cross validation and building models.
            Output: return model accuracy, ROC AUC and details.
            On Failure: Logging exception in error log file """
        try:
            objfeature_selection = feature_selection.FeatureSelection()
            self.final_fetures = objfeature_selection._drop_features()
        
            X, y = self.final_fetures
            self.log_writer.log(self.file_object,'Start model training...!!')
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
            self.log_writer.log(self.file_object,'End model training...!!')
            
            self.log_writer.log(self.file_object,'Start StandardScaler...!!')
            sc = StandardScaler()
            X_train_transformed = pd.DataFrame(sc.fit_transform(X_train),index=X_train.index, columns=X_train.columns)
            X_test_transformed = pd.DataFrame(sc.transform(X_test),index=X_test.index, columns=X_test.columns)
            self.log_writer.log(self.file_object,'End StandardScaler...!!')
            
            self.log_writer.log(self.file_object,'Start KFold cross validation...!!')
            KFold_cv = KFold(n_splits= 5, random_state= 5, shuffle= True)
            self.log_writer.log(self.file_object,'End KFold cross validation...!!')

            self.log_writer.log(self.file_object,'Start building LogisticRegression model...!!')
            logistic_model = LogisticRegression(C= 0.23357214690901212, max_iter= 100, penalty= 'l2', solver= 'lbfgs')
            logistic_model.fit(X_train_transformed, y_train)
            scores = cross_val_score(logistic_model, X_train_transformed, y_train, cv= KFold_cv)
            train_predictions = logistic_model.predict(X_train_transformed)
            test_predictions = logistic_model.predict(X_test_transformed)
            classifi_report = classification_report(y_train, train_predictions)

            # Calculate accuracy scores
            train_accuracy = accuracy_score(y_train, train_predictions)
            test_accuracy = accuracy_score(y_test, test_predictions)
            print('Logistic Regression Model')
            print("Training accuracy:", train_accuracy)
            print("Test accuracy:", test_accuracy)
            print("cross_val_score:", scores)
            print("classification_report:", classifi_report)
            print('=========================================')
            print()
            self.log_writer.log(self.file_object,'End building LogisticRegression model with classification_report ' + classifi_report  +'')

            self.log_writer.log(self.file_object,'Start building RandomForestClassifier model...!!')
            RFmodel = RandomForestClassifier()
            RFmodel.fit(X_train_transformed, y_train)
            scores = cross_val_score(RFmodel, X_train_transformed, y_train, cv=KFold_cv)
            classifi_report = classification_report(y_train, train_predictions)
            train_predictions = RFmodel.predict(X_train_transformed)
            test_predictions = RFmodel.predict(X_test_transformed)

            # Calculate accuracy scores
            train_accuracy = accuracy_score(y_train, train_predictions)
            test_accuracy = accuracy_score(y_test, test_predictions)

            print('RandomForestClassifier')
            print("Training accuracy:", train_accuracy)
            print("Test accuracy:", test_accuracy)
            print("cross_val_score:", scores)
            print("classification_report:", classifi_report)
            print('=========================================')
            print()
            self.log_writer.log(self.file_object,'End building RandomForestClassifier model with classification_report ' + classifi_report  +'')

            self.log_writer.log(self.file_object,'Start building XGBClassifier model...!!')
            Xgb_model = Xgb.XGBClassifier(base_score= 0.2, booster= 'gbtree', gamma= 1, learning_rate= 0.01, 
                                          n_estimators= 500, reg_alpha= 1, reg_lambda= 0.5)
            Xgb_model.fit(X_train_transformed, y_train)
            # make predictions for test data
            score = cross_val_score(Xgb_model, X_train_transformed, y_train, cv= KFold_cv)
            train_predictions = Xgb_model.predict(X_train_transformed)
            test_predictions = Xgb_model.predict(X_test_transformed)
            classifi_report = classification_report(y_train, train_predictions)

            # Calculate accuracy scores
            train_accuracy = accuracy_score(y_train, train_predictions)
            test_accuracy = accuracy_score(y_test, test_predictions)

            print('XGBClassifier')
            print("Training accuracy:", train_accuracy)
            print("Test accuracy:", test_accuracy)
            print("cross_val_score:", scores)
            print("classification_report:", classifi_report)
            print('=========================================')
            print()
            self.log_writer.log(self.file_object,'End building XGBClassifier model with classification_report ' + classifi_report  +'')


            y_pred = logistic_model.predict_proba(X_test_transformed)[:, 1]
            fpr, tpr, _ = roc_curve(y_test, y_pred)
            auc = round(roc_auc_score(y_test, y_pred), 4)
            plt.plot(fpr,tpr,label="Logistic Regression, AUC= "+str(auc))
            self.log_writer.log(self.file_object,'Logistic Regression, AUC= ' + str(auc))

            y_preds = Xgb_model.predict_proba(X_test_transformed)[:, 1]
            fprs, tprs, __ = roc_curve(y_test, y_preds)
            aucs = round(roc_auc_score(y_test, y_preds), 4)
            plt.plot(fprs,tprs,label="XgBoost, AUC= "+str(aucs))
            self.log_writer.log(self.file_object,'XGBClassifier, AUC= ' + str(aucs))

            y_preds_ = RFmodel.predict_proba(X_test_transformed)[:, 1]
            fprs_, tprs_, _ = roc_curve(y_test, y_preds_)
            aucs_ = round(roc_auc_score(y_test, y_preds_), 4)
            plt.plot(fprs_,tprs_,label="RandomForest, AUC= "+str(aucs_))
            self.log_writer.log(self.file_object,'RandomForestClassifier, AUC= ' + str(aucs_))

            plt.plot([0,1],[0,1],'r--')
            plt.xlim([-0.1,1.1])
            plt.ylim([-0.1,1.1])
            plt.ylabel('True Positive Rate')
            plt.xlabel('False Positive Rate')
            plt.legend(loc='lower right')
            plt.show()

        except Exception as ex:
            self.log_writer.log(self.error_file_object, str(ex), 'Class - ' +__class__.__name__+ '')