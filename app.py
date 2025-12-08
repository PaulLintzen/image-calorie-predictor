import keras
import numpy as np
import os
import pandas as pd
import tensorflow as tf
from dotenv import load_dotenv
from flask import Flask, render_template, request, flash, redirect, url_for
from keras.applications.mobilenet_v2 import preprocess_input
from werkzeug.utils import secure_filename


# Load environment variables
load_dotenv()

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Check if SECRET_KEY is set
if not app.config['SECRET_KEY']:
    raise ValueError("No SECRET_KEY set. Set it in .env file.")

os.makedirs('uploads', exist_ok=True)

# Model configuration
CALORIE_FILE_PATH = 'data/calories.csv'
calorie_df = pd.read_csv(CALORIE_FILE_PATH)

IMG_HEIGHT = 128
IMG_WIDTH = 128
CLASS_NAMES = sorted(calorie_df['food'].tolist())


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image_mobilenet(img_path):
    """
    Preprocess image just as done in training for MobileNetV2 based architectures
    """
    # Load image
    img = keras.preprocessing.image.load_img(
        img_path,
        target_size=(IMG_HEIGHT, IMG_WIDTH)
    )

    # Convert to image array, add batch dimensions, and preprocess
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    img_array = preprocess_input(img_array)
    
    return img_array



# ------------------------------
# Model Loading
# ------------------------------
cnn_model = keras.models.load_model('models/architecture7.keras')


# ------------------------------
# Home Page
# ------------------------------
@app.route('/')
def home():
    return render_template('index.html')


# ------------------------------
# Prediction with CNN
# ------------------------------
@app.route('/predict/<filename>', methods=['GET'])
def predict(filename):
    # Load the uploaded image
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if not os.path.exists(filepath):
        flash('File not found')
        return redirect(url_for('upload'))
    
    # Preprocess image
    img_array = preprocess_image_mobilenet(filepath)

    # Make prediction
    predictions = cnn_model.predict(img_array)

    predicted_class_idx = np.argmax(predictions[0])
    confidence = float(predictions[0][predicted_class_idx] * 100)
    predicted_class_name = CLASS_NAMES[predicted_class_idx]

    # Get top 3 predictions
    top_3_indices = np.argsort(predictions[0])[-3:][::-1]
    top_3_predictions = [
        {
            'class': CLASS_NAMES[idx],
            'confidence': float(predictions[0][idx] * 100)
        }
        for idx in top_3_indices
    ]

    return render_template('result.html',
                           filename=filename,
                           prediction=predicted_class_name,
                           confidence=confidence,
                           top_predictions=top_3_predictions)


# ------------------------------
# Image Upload
# ------------------------------
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Check if the post has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        # Check if file is supplied
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        
        # Download the file if it is allowed, then redirect to predict
        if file and allowed_file(file.filename):
            filename = secure_filename(str(file.filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('predict', filename=filename))
        else:
            flash('Invalid file type. Please upload a PNG, JPG, or JPEG image.')
            return redirect(request.url)

    return render_template('upload.html')



if __name__ == '__main__':
    app.run(debug=True)