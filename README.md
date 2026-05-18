# 🍷 Wine Quality Predictor — End-to-End MLOps Pipeline

An end-to-end machine learning project that predicts **red wine quality** using an **ElasticNet regression model**, with a full MLOps pipeline including data ingestion, validation, transformation, model training, evaluation with **MLflow** tracking, and a **Flask** web application for real-time predictions — containerized with **Docker**.

---

## 📌 Project Overview

| Component              | Details                                      |
|------------------------|----------------------------------------------|
| Dataset                | Wine Quality (Red) — `winequality-red.csv`   |
| Model                  | ElasticNet Regression (sklearn)              |
| Experiment Tracking    | MLflow (DagsHub remote URI)                  |
| Web Framework          | Flask                                        |
| Containerization       | Docker                                       |
| Config Management      | YAML-based (`config.yaml`, `params.yaml`)    |
| Pipeline Orchestration | Modular Python pipeline stages               |

---

## 🗂️ Project Structure

```
DataScience_Project/
├── src/datascience/
│   ├── components/         # Core pipeline components
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   ├── pipeline/           # Training & prediction pipelines
│   ├── config/             # Configuration manager
│   ├── entity/             # Config dataclasses
│   ├── constants/          # Path constants
│   └── utils/              # Utility functions
├── config/config.yaml      # Data & model paths
├── params.yaml             # ElasticNet hyperparameters
├── schema.yaml             # Data schema for validation
├── app.py                  # Flask web application
├── main.py                 # Pipeline entry point
├── Dockerfile              # Docker container config
├── requirements.txt        # Python dependencies
└── research/               # Exploratory notebooks
```

---

## ⚙️ Pipeline Stages

1. **Data Ingestion** — Downloads and extracts `winequality-red.csv` from a remote zip URL
2. **Data Validation** — Validates dataset schema against `schema.yaml`
3. **Data Transformation** — Splits data into train/test sets
4. **Model Training** — Trains an ElasticNet model with configurable `alpha` and `l1_ratio`
5. **Model Evaluation** — Evaluates using RMSE, MAE, R² and logs metrics/params to MLflow

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Somesh-Salunkhe/DataScience_Project.git
cd DataScience_Project
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory:
```env
MLFLOW_TRACKING_URI=<your_dagshub_mlflow_uri>
MLFLOW_TRACKING_USERNAME=<your_dagshub_username>
MLFLOW_TRACKING_PASSWORD=<your_dagshub_token>
```

### 4. Run the Training Pipeline
```bash
python main.py
```

### 5. Launch the Flask App
```bash
python app.py
```
Open your browser at `http://localhost:8080`

---

## 🐳 Docker

### Build the Image
```bash
docker build -t wine-quality-predictor .
```

### Run the Container
```bash
docker run -p 8080:8080 \
  -e MLFLOW_TRACKING_URI="your-uri" \
  -e MLFLOW_TRACKING_USERNAME="your-username" \
  -e MLFLOW_TRACKING_PASSWORD="your-password" \
  wine-quality-predictor
```

Open:
`http://localhost:8080`

---

## 🧪 Model Configuration

Edit `params.yaml` to tune ElasticNet hyperparameters:

```yaml
ElasticNet:
  alpha: 0.2
  l1_ratio: 0.1
```

---

## 📊 MLflow Experiment Tracking

Model metrics (RMSE, MAE, R²) and parameters are automatically logged to MLflow after each training run. Configure the remote tracking URI in your `.env` file to use DagsHub or any MLflow server.

---

## 🌐 Web Application

The Flask app provides two main routes:

| Route      | Method | Description                      |
|------------|--------|----------------------------------|
| `/`        | GET    | Home page with input form        |
| `/train`   | GET    | Triggers model training pipeline |
| `/predict` | POST   | Returns wine quality prediction  |

**Input features:** `fixed_acidity`, `volatile_acidity`, `citric_acid`, `residual_sugar`, `chlorides`, `free_sulfur_dioxide`, `total_sulfur_dioxide`, `density`, `pH`, `sulphates`, `alcohol`

**Output:** Wine quality score (integer, range: 1–7)

---

## 🛠️ Tech Stack

- **Python** — Core language
- **scikit-learn** — ElasticNet model
- **MLflow** — Experiment tracking & model registry
- **Flask** — Web serving
- **Docker** — Containerization
- **DagsHub** — Remote MLflow backend
- **YAML** — Config & schema management

---

## 📄 License

This project is licensed under the [GPL-3.0 License](LICENSE).
