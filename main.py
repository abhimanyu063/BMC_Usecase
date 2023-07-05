from model_training import model_training
from flask import Flask, render_template
import os


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

port = int(os.getenv("PORT",3000))
if __name__ == "__main__":
    objmodel_training = model_training.ModelTraining()
    objmodel_training.model_train()
    #app.run(port=port,debug=True)