# Super Good and Special Image Calorie Predictor

![GitHub repo size](https://img.shields.io/github/repo-size/PaulLintzen/image-calorie-predictor) 
![GitHub contributors](https://img.shields.io/github/contributors/PaulLintzen/image-calorie-predictor) 
![GitHub stars](https://img.shields.io/github/stars/PaulLintzen/image-calorie-predictor?style=social) 
![GitHub forks](https://img.shields.io/github/forks/PaulLintzen/image-calorie-predictor?style=social) 
![GitHub license](https://img.shields.io/github/license/PaulLintzen/image-calorie-predictor)

**Description:** Collects calorie info for 101 foods and uses a CNN to predict the food type and estimate its calorie content.

---

## Table of Contents
- [About](#about)
- [Demo](#demo)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About
*(Add long description here)*

---

## Demo
*(Add screenshots or live demo links here)*

---

## Features
- Take a picture of a food item through the included Flask app  
- CNN model predicts the food type from 101 possible options  
- Returns an estimated calorie count based on the predicted food  
- Easy integration for personal use or as part of a larger nutrition-tracking application  

---

## Installation
Step-by-step instructions to get your project running locally:

```bash
# Clone repository
git clone https://github.com/your-username/image-calorie-predictor.git

# Navigate into project folder
cd image-calorie-predictor

# Create a virtual environment (Python example)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Usage
To run the app and predict calories from an image:
```bash
# Activate your virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run the Flask app
python app.py
```
Once the app is running, open your browser and navigate to http://localhost:5000 to take a picture and get predictions.

---

## Technologies
- Language: Python
- Deep Learning Framework: PyTorch
- Web Framework: Flask
- Libraries: OpenCV, Pillow, NumPy, Pandas, torchvision, etc.

---

## Configuration
Before running the app, create your own API keys and add them to the provided .env file:
```
# Example .env
API_KEY=your_api_key_here
```

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## Contact
John Rodocker - https://www.linkedin.com/in/johnrodocker/

Paul Lintzen - https://www.linkedin.com/in/paul-lintzen/
