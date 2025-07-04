# End-to-End UFC Fight Predictor

This project demonstrates the entire lifecycle of a machine learning application, from local development to a live, public API deployed on Google Cloud Platform. The model predicts the winner of UFC fights based on historical data and fighter statistics.

**Live API Documentation:** [https://ufc-predictor-service-341137440410.us-central1.run.app/docs](https://ufc-predictor-service-341137440410.us-central1.run.app/docs)

---

## Project Overview

The project is broken down into four distinct phases, covering everything from initial setup to final deployment and maintenance considerations.

### Phase 1: Foundational Work

| Step | Status | Key Activities |
| :--- | :--- | :--- |
| **1. Project Setup** | ✅ **Completed** | Initialized Git, set up a structured directory, created a `venv` environment, and defined dependencies in `requirements.txt`. |
| **2. Data Acquisition** | ✅ **Completed** | Acquired data from Kaggle, organized it into `raw`/`processed`, and performed EDA in a Jupyter Notebook. |
| **3. Preprocessing**| ✅ **Completed** | Developed a cleaning pipeline, handled missing data, engineered differential features, and created a final, model-ready dataset. |

### Phase 2: Modeling & Local Deployment

| Step | Status | Key Activities |
| :--- | :--- | :--- |
| **4. Model Training** | ✅ **Completed** | Split data into training/testing sets and trained both a Logistic Regression and a Random Forest model. |
| **5. Model Evaluation**| ✅ **Completed** | Evaluated models using accuracy and ROC/AUC curves to select the best performer. Saved the final model with `joblib`. |
| **6. API Creation** | ✅ **Completed** | Built a robust API using FastAPI, defining data structures with Pydantic for automatic validation. |

### Phase 3: Cloud Deployment

| Step | Status | Key Activities |
| :--- | :--- | :--- |
| **7. Containerization** | ✅ **Completed** | Created a `Dockerfile` to package the application, dependencies, and model into a portable container. |
| **8. GCP Deployment** | ✅ **Completed** | Deployed the container to Google Cloud Run, using Cloud Build to create the image and Artifact Registry for storage. |

### Phase 4: Post-Deployment

| Step | Status | Key Activities |
| :--- | :--- | :--- |
| **9. Maintenance** | 💡 **Next Steps**| Set up monitoring in Cloud Run to track API errors and performance. Plan for future model retraining as new fight data becomes available. |
