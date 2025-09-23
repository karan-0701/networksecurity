# ML Pipeline for Network Security 🔐

An **end-to-end machine learning pipeline** designed for network security classification.  
The project automates the entire workflow from **data ingestion → validation → transformation → model training → evaluation → deployment readiness**,  
while ensuring reproducibility, scalability, and maintainability using modern MLOps practices.

---

## 🚀 Features
- **Data Ingestion**: Collect and organize raw network traffic data.
- **Data Validation**: Schema checks, missing value detection, and anomaly handling.
- **Data Transformation**: Feature scaling, encoding, and dataset preparation.
- **Model Training & Evaluation**: Multiple classification models with hyperparameter tuning.
- **Experiment Tracking**: MLflow integration for logging metrics, artifacts, and model versions.
- **CI/CD**: Automated workflows via GitHub Actions.
- **Cloud Integration**: Deployment-ready setup with AWS services.
- **API Serving**: FastAPI app for real-time inference.
- **Robust Design**: Modular components with error handling and logging.

---

## 🛠️ Tech Stack
- **Programming Language**: Python  
- **ML & Data**: scikit-learn, pandas, numpy  
- **Experiment Tracking**: MLflow  
- **Automation & CI/CD**: GitHub Actions  
- **Cloud**: AWS (S3, EC2)  
- **API Framework**: FastAPI + Uvicorn  

---

## ⚡ Getting Started

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/network-security-ml-pipeline.git
cd network-security-ml-pipeline
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the ML pipeline
```bash
python src/main.py
```

### 4️⃣ Track experiments
Launch MLflow UI to view experiments:
```bash
mlflow ui
```

### 5️⃣ Run the FastAPI app
Serve the trained model via API:
```bash
uvicorn app:app --reload
```

The API will be available at:  
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)
---

## 📊 Results
- Achieved improved classification performance with optimized models.  
- Automated tracking of experiments with MLflow for reproducibility.  
- CI/CD enabled seamless integration and deployment workflows.  
- FastAPI enabled real-time inference with low-latency responses.  

---

## 🔮 Future Improvements
- Add deep learning models for enhanced detection.
- Integrate monitoring for deployed models.
- Expand cloud automation with AWS SageMaker.

---

## 📜 License
This project is licensed under the MIT License.