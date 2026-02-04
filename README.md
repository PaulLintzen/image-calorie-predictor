![GitHub repo size](https://img.shields.io/github/repo-size/PaulLintzen/image-calorie-predictor) 
![GitHub contributors](https://img.shields.io/github/contributors/PaulLintzen/image-calorie-predictor) 
![GitHub stars](https://img.shields.io/github/stars/PaulLintzen/image-calorie-predictor?style=social) 
![GitHub forks](https://img.shields.io/github/forks/PaulLintzen/image-calorie-predictor?style=social) 
![GitHub license](https://img.shields.io/github/license/PaulLintzen/image-calorie-predictor)

**Description:** Our AI Food Image Calorie predictor lovingly named "GrubGuru".

---

## Table of Contents
- [About](#about)
- [Features](#features)
- [Demo](#demo)
- [Presentation Slides & Full Report](#report-and-slides)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About
This project was completed as our final project for CSCI 413: Advanced Data Science at the Colorado School of Mines. We trained a Convolutional Neural Network (CNN) on the Food-101 dataset to classify food images and estimate calorie content.

The system includes a front end Flask-based web application that allows users to upload images, after which a saved model is used to identify the food and return a calorie estimate. It provides a front end flask application that allows users to upload images at which point, we use our saved model to identify the food and return a calorie estimate. 

For a quick overview of the methodology and results, we recommend skimming our [presentation slides](PresentationSlides.pdf). For a more detailed discussion, see the full [project report](Report.pdf).


---

## Features
- Take a picture of a food item through the included Flask app  
- CNN model predicts the food type from 101 possible options  
- Returns an estimated calorie count based on the predicted food  
- Easy integration for personal use or as part of a larger nutrition-tracking application  
---


## Demo
The demo is run locally but we've included some screenshots here to demonstrate. We have five correctly classified images along with two incorrect ones. It is interesting to note that for those images where we are getting incorrect outputs, the confidence is generally lower and the correct classification is often listed as next most likely.


<table>
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/3c2bb447-6c79-4591-8402-3aa317864cab" width="300"/>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/3fac0fa5-e55b-44f2-ada3-9a1bfc5fa257" width="300"/>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/824e4435-0c53-4bda-ab45-ab1a0e04b88b" width="300"/>
    </td>
  </tr>

  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/95e90395-6fb9-45bd-8f6b-7fddbdc312b8" width="300"/>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/7118c711-04f5-4b89-80a5-8405a0bfd1f2" width="300"/>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/1b4ae1d2-aedd-4968-8638-5bcfba9129f8" width="300"/>
    </td>
  </tr>

  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/64a780d0-0dcd-483a-becf-37e8a82971dd" width="300"/>
    </td>
  </tr>
</table>

---

## Report and Slides

- **Full Project Report:** [Report.pdf](Report.pdf)  
  Detailed methodology, experiments, and evaluation.

- **Presentation Slides:** [PresentationSlides.pdf](PresentationSlides.pdf)  
  High-level overview of the pipeline and results.

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
- Deep Learning Framework: TensorFlow, PyTorch, Keras, Torchvision
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
