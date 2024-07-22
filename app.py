from flask import Flask, render_template,request
import pickle
import numpy as np

model1 = pickle.load(open(r'C:\Users\Ranjith007\Documents\MY DOCUMENTS\heartml\model\heart.pkl','rb'))  

app = Flask(__name__)  # initializing Flask app


@app.route("/",methods=['GET'])
def hello():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST': 

        d1 = request.form['age']
        d2 = request.form['sex']
        d3 = request.form['chestPain']
        d4 = request.form['cloodPressure']
        d5 = request.form['cholesterol']
        d6 = request.form['bloodSugar']
        d7 = request.form['electrocardio']
        d8 = request.form['heartRate']
      
        
       
        arr = np.array([[d1,d2,d3,d4,d5,d6,d7,d8]])
        print([d1,d2,d3,d4,d5,d6,d7,d8])
        pred1 = model1.predict(arr)

        if pred1[0] == 0:
            pred1 = "Hey! Your Heart is Healthy 😊" 
        else:
            pred1 ="Your Heart is not Healthy 😒"


      
      
    return render_template('result.html',prediction_text1=pred1)
    
if __name__ == '__main__':
    app.run(debug=True)
    

