from datetime import datetime

class App_Logger:
    def __init__(self):
        pass

    def log(self, file_object, log_message, class_name = "", method_name = ""):
        try:
            self.now = datetime.now()
            self.date = self.now.date()
            self.current_time = self.now.strftime("%H:%M:%S")
            file_object.write(str(self.date) + "/" + str(self.current_time) + "\t\t" + log_message +  "\t\t" + class_name + "\t\t" + method_name +"\n")
        except Exception as ex:
            print('App_Logger-log error', ex)

