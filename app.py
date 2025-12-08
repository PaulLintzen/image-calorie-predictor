from flask import Flask, render_template, request
import keras
import tensorflow as tf

app = Flask(__name__)

# ------------------------------
# Model Loading
# ------------------------------
cnn_model = keras.models.load_model('models/architecture7.keras')

# ------------------------------
# Home Page
# ------------------------------
@app.route('/')
def home():
    return 'TEMP: Homepage'

# ------------------------------
# Prediction with CNN
# ------------------------------
@app.route('/predict', methods=['GET'])
def predict():
    return 'TEMP: Predict'

# ------------------------------
# Image Upload
# ------------------------------
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    return 'TEMP: Upload'



if __name__ == '__main__':
    app.run(debug=True)