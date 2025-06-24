# End to End Data Science Project

## Tech Stack

- Python 3.x
- Flask (Web Framework)
- scikit-learn (Machine Learning)
- pandas, numpy (Data Processing)
- joblib (Model Serialization)
- MLflow (Experiment Tracking)
- Dagshub (Remote MLflow Tracking)
- python-dotenv (Environment Variables)

### Workflows--ML Pipeline

1. Data Ingestion
2. Data Validation
3. Data Transformation-- Feature Engineering,Data Preprocessing
4. Model Trainer
5. Model Evaluation- MLFLOW,Dagshub

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py

## Environment Setup

1. Create a virtual environment (recommended):
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Deactivate the environment when done:
   ```powershell
   deactivate
   ```

## Environment Variables

This project uses a `.env` file in the project root to store sensitive environment variables such as MLflow tracking credentials. Example variables in `.env`:

```env
MLFLOW_TRACKING_URI=your_mlflow_tracking_uri
MLFLOW_TRACKING_USERNAME=your_username
MLFLOW_TRACKING_PASSWORD=your_password
```

- Do not share your actual credentials publicly.
- The `.env` file is used to configure MLflow tracking with Dagshub.
- To use these variables in your code, load them with `python-dotenv`:

```python
from dotenv import load_dotenv
load_dotenv()
```

## API Endpoint Reference

### 1. Homepage
- **URL:** `/`
- **Method:** `GET`
- **Description:** Renders the homepage with the input form.
- **Response:** HTML page (`index.html`)

---

### 2. Train Model
- **URL:** `/train`
- **Method:** `GET`
- **Description:** Triggers the training pipeline by running `main.py`.
- **Response:** Plain text message: `"Training Successful"`

---

### 3. Predict Wine Quality
- **URL:** `/predict`
- **Methods:** `GET`, `POST`
- **Description:**
  - `GET`: Renders the prediction form (`index.html`).
  - `POST`: Accepts form data for wine features, runs prediction, and renders the result.
- **Form Data (all required, as floats):**
  - `fixed_acidity`
  - `volatile_acidity`
  - `citric_acid`
  - `residual_sugar`
  - `chlorides`
  - `free_sulfur_dioxide`
  - `total_sulfur_dioxide`
  - `density`
  - `pH`
  - `sulphates`
  - `alcohol`
- **Response:**
  - On success: HTML page (`results.html`) with prediction result.
  - On error: Plain text message `"something is wrong"`