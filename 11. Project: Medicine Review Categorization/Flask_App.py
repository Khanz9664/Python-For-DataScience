from flask import Flask, request, jsonify
import joblib
import scipy.sparse as sp

# Load the saved components
model = joblib.load('medicine_review_model.pkl')
tfidf_uses = joblib.load('tfidf_uses_vectorizer.pkl')
tfidf_side_effects = joblib.load('tfidf_side_effects_vectorizer.pkl')
label_encoder = joblib.load('manufacturer_label_encoder.pkl')

# Check if the components are loaded correctly
print(f"Model: {type(model)}")
print(f"TF-IDF Uses: {type(tfidf_uses)}")
print(f"TF-IDF Side Effects: {type(tfidf_side_effects)}")
print(f"Label Encoder: {type(label_encoder)}")

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    print("Predict endpoint hit!")  # Check if the endpoint is reached
    
    try:
        # Step 1: Get data from the request
        data = request.json
        print(f"Data received: {data}")  # Check the data received from the user
        
        if not data:
            print("No data provided")  # If no data is sent, return an error
            return jsonify({"error": "No data provided"}), 400

        # Step 2: Extract values from the input
        uses = data.get("Uses", "")
        side_effects = data.get("Side_effects", "")
        manufacturer = data.get("Manufacturer", "")
        print(f"Inputs - Uses: {uses}, Side Effects: {side_effects}, Manufacturer: {manufacturer}")
        
        # Step 3: Transform inputs using the saved transformers
        X_uses = tfidf_uses.transform([uses])
        print("Uses transformed")
        X_side_effects = tfidf_side_effects.transform([side_effects])
        print("Side Effects transformed")
        manufacturer_encoded = label_encoder.transform([manufacturer])
        print(f"Manufacturer encoded: {manufacturer_encoded}")

        # Step 4: Combine the features into a single matrix
        X_combined = sp.hstack([X_uses, X_side_effects, sp.csr_matrix(manufacturer_encoded).T])
        
        # Step 5: Make the prediction using the loaded model
        prediction = model.predict(X_combined)
        print(f"Prediction: {prediction}")  # Print prediction result

        # Step 6: Return the prediction as a response
        return jsonify({"Review_Category": prediction[0]})
    
    except Exception as e:
        print(f"Error occurred: {e}")  # Log the error if something goes wrong
        return jsonify({"error": "An error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)

