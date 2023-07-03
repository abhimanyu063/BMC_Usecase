from data_preprocessing import preprocessing
from application_logging import logger

class FeatureEngineering:
    def __init__(self) -> None:
        objDataPrepro = preprocessing.DataPreprocessing()
        self.final_dataFrame = objDataPrepro.preprocessing()
        self.file_object = open("prediction_logs/prediction_log.txt", 'a+')
        self.log_writer = logger.App_Logger()

    def __droping_feature(self):
        try:
            self.log_writer.log(self.file_object,'Start dropping features...!!')
            drop_cols = ['Order ID', 'Order Date', 'Ship Date', 'Customer ID',
                         'Product ID', 'Customer Name', 'Postal Code']
            self.final_dataFrame.drop(columns= drop_cols, axis= 1, inplace= True)
            self.log_writer.log(self.file_object,'Droped features...!!')
            return self.final_dataFrame

        except Exception as ex:
            print('error', ex)

    def _encode_categorical_columns(self):
        try:
            self.log_writer.log(self.file_object,'Start encoding categorical features...!!')
            self.encoding_cat_feature = self.__droping_feature()
            self.encoding_cat_feature['Ship Mode'] = self.encoding_cat_feature['Ship Mode'].map({'First Class': 1, 'Same Day' : 2, 'Second Class' : 3, 'Standard Class' : 4})
            self.encoding_cat_feature['Segment'] = self.encoding_cat_feature['Segment'].map({'Consumer' : 1, 'Corporate' : 2, 'Home Office' : 3})
            self.encoding_cat_feature['Country'] = self.encoding_cat_feature['Country'].map({'United States' : 1})
            self.encoding_cat_feature['Region'] = self.encoding_cat_feature['Region'].map({'Central' : 1, 'East' : 2, 'South' : 3, 'West' : 4})
            self.encoding_cat_feature['Category'] = self.encoding_cat_feature['Category'].map({'Technology' : 1})
            self.encoding_cat_feature['Sub-Category'] = self.encoding_cat_feature['Sub-Category'].map({'Machines' : 1})
            self.encoding_cat_feature['Product Name'] = "Printer"
            self.encoding_cat_feature['Product Name'] = self.encoding_cat_feature['Product Name'].map({'Printer' : 1})
            self.encoding_cat_feature['State'] = self.encoding_cat_feature['State'].map({'Alabama' : 1, 'Arizona' : 2,'California' : 3,'Colorado' : 4,'Connecticut' : 5,'Delaware' : 6,'Florida' : 7,'Georgia' : 8,'Idaho' : 9,'Illinois' : 10,'Indiana' : 11,'Iowa' : 12,'Kansas' : 13, 
                                                                                         'Kentucky' : 14,'Maryland' : 15,'Massachusetts' : 16,'Michigan' : 17,'Minnesota' : 18,'Mississippi' : 19,'Missouri' : 20,'Nebraska' : 21,'Nevada' : 22,'New Hampshire' : 23,'New Jersey' : 24,'New Mexico' : 25,'New York' : 26, 
                                                                                         'North Carolina' : 27,'Ohio' : 28,'Oklahoma' : 29,'Oregon' : 30,'Pennsylvania' : 31,'Rhode Island' : 32,'South Carolina' : 33,'Tennessee' : 34,'Texas' : 35,'Utah' : 36,'Virginia' : 37,'Washington' : 38,'West Virginia' : 39,'Wisconsin' : 40})
            self.encoding_cat_feature['City'] = self.encoding_cat_feature['City'].map({'Akron' : 1,'Alexandria' : 2,'Allentown' : 3,'Anaheim' : 4,'Andover' : 5,'Ann Arbor' : 6,'Apopka' : 7,'Arlington' : 8,'Aurora' : 9,'Austin' : 10,'Baltimore' : 11,'Bedford' : 12,'Bloomington' : 13,'Brentwood' : 14,'Bristol' : 15,'Broken Arrow' : 16,'Bullhead City' : 17,'Burbank' : 18,'Burlington' : 19,'Canton' : 20, 
                                                                                         'Carrollton' : 21,'Chandler' : 22,'Charlotte' : 23,'Chattanooga' : 24,'Chesapeake' : 25,'Chicago' : 26,'Cleveland' : 27,'Columbia' : 28,'Columbus' : 29,'Concord' : 30,'Corpus Christi' : 31,'Costa Mesa' : 32,'Cranston' : 33,'Dallas' : 34,'Decatur' : 35,'Deer Park' : 36,'Deltona' : 37,'Denver' : 38,'Des Moines' : 39,'Detroit' : 40,
                                                                                         'Dublin' : 41,'Durham' : 42,'Eagan' : 43,'Edinburg' : 44,'El Paso' : 45,'Evanston' : 46,'Everett' : 47,'Fayetteville' : 48,'Florence' : 49,'Fort Collins' : 50,'Franklin' : 51,'Fremont' : 52,'Glendale' : 53,'Grand Prairie' : 54,'Grand Rapids' : 55,'Green Bay' : 56,'Greensboro' : 57,'Greenville' : 58,'Gresham' : 59,'Hampton' : 60,  
                                                                                         'Hempstead' : 61,'Henderson' : 62,'Hendersonville' : 63,'Hialeah' : 64,'Highland Park' : 65,'Hillsboro' : 66,'Homestead' : 67,'Houston' : 68,'Huntington Beach' : 69,'Huntsville' : 70,'Jackson' : 71,'Jacksonville' : 72,'Kenosha' : 73,'Kent' : 74,'Knoxville' : 75,'La Mesa' : 76,'La Porte' : 77,'Lafayette' : 78,'Lakeville' : 79,'Lakewood' : 80, 
                                                                                         'Lancaster' : 81,'Las Cruces' : 82,'Las Vegas' : 83,'Lawrence' : 84,'Lawton' : 85,'Lewiston' : 86,'Long Beach' : 87,'Los Angeles' : 88,'Louisville' : 89,'Lubbock' : 90,'Manhattan' : 91,'Maple Grove' : 92,'Mason' : 93,'Mcallen' : 94,'Medford' : 95,'Miami' : 96,'Midland' : 97,'Milford' : 98,'Milwaukee' : 99,'Minneapolis' : 100,'Mission Viejo' : 101, 
                                                                                         'Mobile' : 102,'Modesto' : 103,'Monroe' : 104,'Montgomery' : 105,'Moorhead' : 106,'Morristown' : 107,'Murray' : 108,'Naperville' : 109,'Nashville' : 110,'New Bedford' : 111,'New Rochelle' : 112,'New York City' : 113,'Newark' : 114,'Newport News' : 115,'Noblesville' : 116,'Norwich' : 117,'Oceanside' : 118,'Oklahoma City' : 119,'Orange' : 120,'Orem' : 121, 
                                                                                         'Orlando' : 122,'Oxnard' : 123,'Palm Coast' : 124,'Pasadena' : 125,'Perth Amboy' : 126,'Philadelphia' : 127,'Phoenix' : 128,'Pico Rivera' : 129,'Plainfield' : 130,'Plano' : 131,'Pomona' : 132,'Portland' : 133,'Providence' : 134,'Provo' : 135,'Pueblo' : 136,'Raleigh' : 137,'Reading' : 138,'Redmond' : 139,'Renton' : 140,'Revere' : 141,'Richmond' : 142,'Rio Rancho' : 143, 
                                                                                         'Rochester' : 144,'Rock Hill' : 145,'Rockford' : 146,'Roseville' : 147,'Sacramento' : 148,'Saint Charles' : 149,'Saint Louis' : 150,'Saint Petersburg' : 151,'San Angelo' : 152,'San Antonio' : 153,'San Bernardino' : 154,'San Diego' : 155,'San Francisco' : 156,'San Jose' : 157,'Santa Barbara' : 158,'Santa Clara' : 159,'Seattle' : 160,'Skokie' : 161,'Sparks' : 162,'Spokane' : 163, 
                                                                                         'Springfield' : 164,'Sunnyvale' : 165,'Tallahassee' : 166,'Tampa' : 167,'Texas City' : 168,'Thomasville' : 169,'Thousand Oaks' : 170,'Tigard' : 171,'Tulsa' : 172,'Tuscaloosa' : 173,'Urbandale' : 174,'Vallejo' : 175,'Virginia Beach' : 176,'Waterbury' : 177,'Waterloo' : 178,'Westfield' : 179,'Wheeling' : 180,'Wilmington' : 181,'Yuma' : 182})
            
            self.log_writer.log(self.file_object,'End encoding categorical features...!!')
            return self.encoding_cat_feature



        except Exception as ex:
            print('error', ex)