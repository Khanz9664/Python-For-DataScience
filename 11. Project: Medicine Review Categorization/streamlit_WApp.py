import streamlit as st
import scipy.sparse as sp
import joblib

# Load the saved components
model = joblib.load('medicine_review_model.pkl')
tfidf_uses = joblib.load('tfidf_uses_vectorizer.pkl')
tfidf_side_effects = joblib.load('tfidf_side_effects_vectorizer.pkl')
label_encoder = joblib.load('manufacturer_label_encoder.pkl')

st.title("Medicine Review Predictor")

# Input fields
uses = st.text_input("Enter Uses of the Medicine:")
side_effects = st.text_input("Enter Side Effects:")
manufacturer = st.text_input("Enter Manufacturer:")

if st.button("Predict"):
    try:
        # Transform inputs
        X_uses = tfidf_uses.transform([uses])
        X_side_effects = tfidf_side_effects.transform([side_effects])
        manufacturer_encoded = label_encoder.transform([manufacturer])
        X_combined = sp.hstack([X_uses, X_side_effects, sp.csr_matrix(manufacturer_encoded).T])

        # Predict
        prediction = model.predict(X_combined)
        st.success(f"Review Category: {prediction[0]}")

    except Exception as e:
        st.error(f"An error occurred: {e}")

