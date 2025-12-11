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
This project was produced for as our Final Project from CSCI413 Advanced Data Science at Colorado School of Mines. It focuses on training a CNN model on the Food101 dataset and provides a front end flask application that allows users to upload images. Once an image has been uploaded, we use our saved model to identify the food and return a calorie estimate.

---

## Demo
The demo is run locally but we've included some screenshots here to demonstrate.

First some correct predictions:

<img width="524" height="511" alt="Screenshot 2025-12-08 221200" src="https://github.com/user-attachments/assets/3c2bb447-6c79-4591-8402-3aa317864cab" />
<img width="463" height="499" alt="Screenshot 2025-12-08 210723" src="https://github.com/user-attachments/assets/3fac0fa5-e55b-44f2-ada3-9a1bfc5fa257" />
<img width="473" height="575" alt="Screenshot 2025-12-08 210107" src="https://github.com/user-attachments/assets/824e4435-0c53-4bda-ab45-ab1a0e04b88b" />
<img width="532" height="557" alt="Screenshot 2025-12-08 205732" src="https://github.com/user-attachments/assets/95e90395-6fb9-45bd-8f6b-7fddbdc312b8" />
<img width="594" height="590" alt="Screenshot 2025-12-08 205601" src="https://github.com/user-attachments/assets/7118c711-04f5-4b89-80a5-8405a0bfd1f2" />


Some Incorrect Predictions:

<img width="475" height="575" alt="Screenshot 2025-12-08 205928" src="https://github.com/user-attachments/assets/1b4ae1d2-aedd-4968-8638-5bcfba9129f8" />
<img width="478" height="512" alt="Screenshot 2025-12-08 210807" src="https://github.com/user-attachments/assets/64a780d0-0dcd-483a-becf-37e8a82971dd" />






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
- Deep Learning Framework: TesnorFlow, PyTorch, Keras, Torchvision
- Web Framework: Flask
- Libraries: OpenCV, Pillow, NumPy, Pandas, scikit-learn, matplotlib, tqdm etc.

---

## Contributing
We welcome contributions! Follow these steps:
1. Fork the repository
2. Create a feature branch (```git checkout -b feature-name```)
3. Commit your changes (```git commit -m 'Add feature'```)
4. Push to branch (```git push origin feature-name```)
5. Open a Pull Request

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
LinkedIn: [John Rodocker](https://www.linkedin.com/in/johnrodocker/), [Paul Lintzen](https://www.linkedin.com/in/paul-lintzen/)

Email: [John Rodocker](mailto:john_rodocker@mines.edu), [Paul Lintzen](mailto:paul_lintzen@mines.edu)

---
