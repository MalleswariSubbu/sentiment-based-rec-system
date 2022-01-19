# import Flask class from the flask module
from flask import Flask, request, jsonify, render_template


# Create Flask object to run
app = Flask(__name__)

from model import filter_top_five_best as recommend

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Prediction page
@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    username = str(request.form.get('reviews_username'))
    print(username)
    prediction = recommend(username)
    print("Output :", prediction)
    return render_template('index.html', prediction_text='Your Top 5 Recommendations are:\n {}'.format(prediction))
    #return prediction[0]


if __name__ == "__main__":
    print("**Starting Server...")
    # Call function that loads Model
    print("**Model loaded...")
    # Run Server
    app.run(host="127.0.0.1", port=5000)
    #app.run(debug = True)