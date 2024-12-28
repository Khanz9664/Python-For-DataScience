# Medicine Review Classification

This project is a web-based application designed to classify medicine reviews into predefined categories based on their uses, side effects, and manufacturer. Built using Streamlit, the application leverages machine learning to provide quick and accurate predictions, enabling healthcare professionals, pharmaceutical companies, and patients to gain insights into medicine reviews.

---

## Features

- **Input Fields**:
  - `Uses`: The intended use or purpose of the medicine.
  - `Side Effects`: Known or experienced side effects of the medicine.
  - `Manufacturer`: The company that produced the medicine.
- **Machine Learning**:
  - Trained classification model to predict the review category.
  - TF-IDF Vectorization for textual features.
  - Label Encoding for categorical data.
- **Streamlit Interface**:
  - User-friendly web application for submitting and viewing predictions.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/medicine-review-classification.git
   cd medicine-review-classification
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure the following `.pkl` files are present in the project directory:
   - `medicine_review_model.pkl`
   - `tfidf_uses_vectorizer.pkl`
   - `tfidf_side_effects_vectorizer.pkl`
   - `manufacturer_label_encoder.pkl`

4. Run the Streamlit application:
   ```bash
   streamlit run Streamlit_WApp.py
   ```

---

## Usage

1. Open the application in your browser (typically at `http://localhost:8501`).
2. Enter the following details:
   - `Uses`: Specify the purpose of the medicine.
   - `Side Effects`: Mention any known side effects.
   - `Manufacturer`: Enter the manufacturer's name.
3. Click on the "Predict" button.
4. View the predicted review category displayed on the screen.

---

## Project Structure

```
medicine-review-classification/
|-- Streamlit_WApp.py                  # Streamlit app
|-- requirements.txt        # Python dependencies
|-- medicine_review_model.pkl           # Trained model
|-- tfidf_uses_vectorizer.pkl           # TF-IDF vectorizer for uses
|-- tfidf_side_effects_vectorizer.pkl   # TF-IDF vectorizer for side effects
|-- manufacturer_label_encoder.pkl      # Label encoder for manufacturer
|-- README.md               # Project readme
```

medicine_review_model.pkl, tfidf_uses_vectorizer.pkl, tfidf_side_effects_vectorizer.pkl,  manufacturer_label_encoder.pkl 

These files will be created when you have run the notebook on your local machine.

---

## Dependencies

- Python 3.8+
- Streamlit
- scikit-learn
- joblib
- scipy

Install dependencies using `pip install -r requirements.txt`.

---

## Future Enhancements

- Add confidence scores to predictions.
- Incorporate Explainable AI (e.g., SHAP values) for interpretability.
- Include additional input fields like dosage and age group.
- Extend support for multi-language reviews.
- Deploy on cloud platforms like Heroku or Streamlit Cloud.

---

## Author

Developed by [Shahid Ul Islam](https://github.com/Khanz9664).

Feel free to contribute or provide suggestions to enhance the project!

