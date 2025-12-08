import keras
import numpy as np
import os
import pandas as pd
import tensorflow as tf
from dotenv import load_dotenv
from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from keras.applications.mobilenet_v2 import preprocess_input
from keras.models import Model
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
calorie_df = pd.read_csv(CALORIE_FILE_PATH).dropna()
calorie_dict = dict(zip(calorie_df['food'], calorie_df['kcal/100g']))

IMG_HEIGHT = 128
IMG_WIDTH = 128

# Class names are ordered just as they were in testing
CLASS_NAMES = [
    'apple_pie', 'baby_back_ribs', 'baklava', 'beef_carpaccio', 'beef_tartare', 
    'beet_salad', 'beignets', 'bibimbap', 'bread_pudding', 'breakfast_burrito', 
    'bruschetta', 'caesar_salad', 'cannoli', 'caprese_salad', 'carrot_cake', 
    'ceviche', 'cheese_plate', 'cheesecake', 'chicken_curry', 'chicken_quesadilla', 
    'chicken_wings', 'chocolate_cake', 'chocolate_mousse', 'churros', 'clam_chowder', 
    'club_sandwich', 'crab_cakes', 'creme_brulee', 'croque_madame', 'cup_cakes', 
    'deviled_eggs', 'donuts', 'dumplings', 'edamame', 'eggs_benedict', 
    'escargots', 'falafel', 'filet_mignon', 'fish_and_chips', 'foie_gras', 
    'french_fries', 'french_onion_soup', 'french_toast', 'fried_calamari', 'fried_rice', 
    'frozen_yogurt', 'garlic_bread', 'gnocchi', 'greek_salad', 'grilled_cheese_sandwich', 
    'grilled_salmon', 'guacamole', 'gyoza', 'hamburger', 'hot_and_sour_soup', 
    'hot_dog', 'huevos_rancheros', 'hummus', 'ice_cream', 'lasagna', 
    'lobster_bisque', 'lobster_roll_sandwich', 'macaroni_and_cheese', 'macarons', 'miso_soup', 
    'mussels', 'nachos', 'omelette', 'onion_rings', 'oysters', 
    'pad_thai', 'paella', 'pancakes', 'panna_cotta', 'peking_duck', 
    'pho', 'pizza', 'pork_chop', 'poutine', 'prime_rib', 
    'pulled_pork_sandwich', 'ramen', 'ravioli', 'red_velvet_cake', 'risotto', 
    'samosa', 'sashimi', 'scallops', 'seaweed_salad', 'shrimp_and_grits', 
    'spaghetti_bolognese', 'spaghetti_carbonara', 'spring_rolls', 'steak', 'strawberry_shortcake', 
    'sushi', 'tacos', 'takoyaki', 'tiramisu', 'tuna_tartare', 'waffles'
]


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
#   This page is currently set to be the same as the upload page, but
#   this can be changed later if desired.
@app.route('/')
def home():
    return redirect(url_for('upload'))


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
    #   The type conflict is ignored here since keras.models.load_model()
    #   does not explicitly return the keras.models.Model type
    predictions = cnn_model.predict(img_array) # type: ignore

    # Output all predictions to terminal for debugging
    print("\n=== PREDICTIONS ===")
    for idx, prob in enumerate(predictions[0]):
        print(f"{idx}: {CLASS_NAMES[idx]} = {prob:.4f}")
    print("===================\n")

    predicted_class_idx = np.argmax(predictions[0])
    confidence = float(predictions[0][predicted_class_idx] * 100)
    predicted_class_name = CLASS_NAMES[predicted_class_idx]
    predicted_calories = calorie_dict.get(predicted_class_name.replace('_', ' '), None)

    # Get top 5 predictions
    top_5_indices = np.argsort(predictions[0])[-5:][::-1]
    top_5_predictions = [
        {
            'class': CLASS_NAMES[idx],
            'confidence': float(predictions[0][idx] * 100),
            'calories': calorie_dict.get(CLASS_NAMES[idx].replace('_', ' '), None)
        }
        for idx in top_5_indices
    ]

    return render_template('result.html',
                           filename=filename,
                           prediction=predicted_class_name,
                           confidence=confidence,
                           calories=predicted_calories,
                           top_predictions=top_5_predictions)


# ------------------------------
# Image Upload
# ------------------------------
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Clear all previous uploads
        for filename in os.listdir(app.config['UPLOAD_FOLDER']):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            try:
                if os.path.isfile(filepath):
                    os.remove(filepath)
            except Exception as e:
                print(f"Error deleting {filename}: {e}")
        
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


# ------------------------------
# Upload Retrieval
# ------------------------------
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



if __name__ == '__main__':
    app.run(debug=True)