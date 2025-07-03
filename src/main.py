from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# 1. Initialize the FastAPI app
app = FastAPI(title="UFC Fight Predictor API")

# 2. Define the input data structure using Pydantic
# The field names MUST match the feature names our model was trained on.
class FightFeatures(BaseModel):
    height_diff: float
    reach_diff: float
    age_diff: float
    sig_str_landed_diff: float
    sig_str_accuracy_diff: float
    takedown_accuracy_diff: float
    sub_avg_diff: float

# 3. Load the trained model ONCE at startup
# Make sure the path to your model file is correct.
# This path is relative to where you run the uvicorn command (the project root).
model_path = "models/ufc_predictor_log_reg.joblib"
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    raise RuntimeError(f"Model file not found at {model_path}. Please ensure the model is trained and saved.")

# 4. Define the prediction endpoint
@app.post("/predict/")
def predict(features: FightFeatures):
    """
    Takes fighter feature differences and predicts the winner.
    - **features**: A JSON object with the required feature differences.
    - **returns**: A JSON object with the predicted winner and the prediction probability.
    """
    # Convert the input Pydantic object to a dictionary
    data = features.dict()
    
    # Create a pandas DataFrame from the dictionary
    # The order of columns must match the order the model was trained on.
    feature_df = pd.DataFrame([data], columns=features.__fields__.keys())

    # Get the prediction probability from the model
    # predict_proba returns probabilities for both classes [P(Red wins), P(Blue wins)]
    prediction_proba = model.predict_proba(feature_df)

    # Get the probability for the "Blue Wins" class (which is the second value)
    confidence = prediction_proba[0][1]
    
    # Determine the predicted winner based on the confidence
    predicted_winner = "Blue" if confidence > 0.5 else "Red"

    return {
        "predicted_winner": predicted_winner,
        "confidence_score": float(f"{confidence:.4f}") # Format to 4 decimal places
    }

# Optional: Add a root endpoint for a simple health check
@app.get("/")
def read_root():
    return {"status": "UFC Predictor API is running."}