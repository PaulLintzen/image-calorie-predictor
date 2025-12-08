import keras
import os
import tensorflow as tf
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

os.makedirs('uploads', exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
    return render_template('predict.html', filename=filename)


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