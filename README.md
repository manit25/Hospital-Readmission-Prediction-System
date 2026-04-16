# Hospital Readmission Prediction System

<div align="center">

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive machine learning pipeline for predicting hospital patient readmission risk using advanced data processing, model training, and real-time APIs.

[Features](#features) • [Quick Start](#quick-start) • [Documentation](#documentation) • [Architecture](#architecture)

</div>

---

## 📋 Overview

Hospital readmission is a critical metric in healthcare quality and cost management. This project implements an **end-to-end machine learning system** that predicts the likelihood of patient readmission within 30 days of discharge, enabling proactive interventions and resource optimization.

### Key Capabilities

- **Data Pipeline**: Automated ingestion, processing, and transformation of patient data
- **ML Model**: Random Forest classifier trained on historical readmission patterns
- **REST API**: FastAPI backend for real-time predictions
- **Interactive Dashboard**: Streamlit-based visualization and monitoring
- **Batch Processing**: Apache Spark for large-scale data processing
- **Orchestration**: Apache Airflow for workflow automation
- **Containerization**: Docker & Docker Compose for seamless deployment

---

## ✨ Features

### 1. **Data Processing Pipeline**

- Spark-based distributed data processing
- Automatic feature engineering and encoding
- Handling of categorical and numeric data types
- Data quality validation and cleaning

### 2. **Machine Learning Model**

- **Algorithm**: Random Forest Classifier (Ensemble Learning)
- **Target**: Binary classification (Readmitted: Yes/No)
- **Features**: Patient demographics, medical history, admission details
- **Model Persistence**: Serialized models for production inference

### 3. **Production APIs**

- **FastAPI** backend with async support
- Real-time prediction endpoints
- Request validation and error handling
- Interactive API documentation (Swagger UI)

### 4. **Interactive Dashboards**

- **Streamlit** web interface
- Real-time model predictions
- Data visualizations and analytics
- Performance monitoring

### 5. **Workflow Orchestration**

- Apache Airflow DAGs for automated pipelines
- Scheduled data ingestion and model training
- Dependency management and error handling

### 6. **Database Integration**

- PostgreSQL backend for data persistence
- Connection pooling and optimization
- Secure credential management

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Data Sources                              │
│              (Raw Patient Data - CSV)                        │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│            Data Ingestion & Loading                          │
│         (load_data.py with PostgreSQL)                       │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│          Data Processing & Feature Engineering               │
│      (Spark Processing + Label Encoding)                     │
└──────────────────────┬──────────────────────────────────────┘
                       │
       ┌───────────────┴────────────────┐
       │                                │
       ▼                                ▼
  ┌─────────────┐             ┌──────────────────┐
  │   EDA       │             │  Model Training  │
  │ (Notebook)  │             │  (sklearn)       │
  └─────────────┘             └──────────────────┘
                                      │
                                      ▼
                             ┌──────────────────┐
                             │  Trained Model   │
                             │  (model.pkl)     │
                             └────────┬─────────┘
                                      │
          ┌───────────────────────────┼────────────────────────┐
          │                           │                        │
          ▼                           ▼                        ▼
    ┌─────────────┐          ┌──────────────────┐      ┌─────────────┐
    │  FastAPI    │          │   Streamlit      │      │   Airflow   │
    │  REST API   │          │   Dashboard      │      │   DAGs      │
    └─────────────┘          └──────────────────┘      └─────────────┘
```

---

## � Exploratory Data Analysis

The following visualizations represent key insights from the exploratory data analysis:

![EDA Visualizations](data/processed/eda_visualizations.png)

### Key Insights:

- **Hospital Stay Distribution**: Most patients stay 3-8 days, with outliers up to 14+ days
- **Readmission Status**: Class distribution shows readmission rates across the patient population
- **Feature Distributions**: Demographic and clinical features show typical patient profiles
- **Feature Correlations**: Heatmap reveals relationships between key predictive features

For detailed analysis code and interactive exploration, see [analysis/eda.ipynb](analysis/eda.ipynb)

---

## �🚀 Quick Start

### Prerequisites

- **Python 3.8+**
- **Docker & Docker Compose** (optional, for containerized deployment)
- **PostgreSQL** (for database)

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd hospital_readmission_advanced
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv venv

   # Windows
   .\venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables** (create `.env` file)
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/hospital_db
   MODEL_PATH=./model/model.pkl
   SPARK_HOME=/path/to/spark
   ```

### Running the Application

#### Option 1: Individual Components

```bash
# 1. Data Processing
python processing/spark_processing.py

# 2. Model Training
python model/train_model.py

# 3. Start API Server (on port 8000)
uvicorn api.main:app --reload

# 4. Start Dashboard (on port 8501)
streamlit run dashboard/app.py
```

#### Option 2: Docker Compose (Recommended)

```bash
docker-compose up --build
```

This will start:

- **API**: http://localhost:8000
- **Dashboard**: http://localhost:8501
- **PostgreSQL**: localhost:5432

---

## 📚 Documentation

### API Endpoints

#### Health Check

```http
GET /
```

**Response:**

```json
{
  "message": "Hospital Readmission API Running"
}
```

#### Make Prediction

```http
POST /predict
Content-Type: application/json

{
  "age": 65,
  "admission_type": 1,
  "time_in_hospital": 5,
  "num_medications": 15,
  "...other_features": "..."
}
```

**Response:**

```json
{
  "prediction": 1,
  "risk": "High"
}
```

### Interactive API Documentation

Once the API is running, visit:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Dashboard Features

- Patient risk prediction interface
- Historical readmission trends
- Feature importance visualization
- Model performance metrics
- Real-time prediction monitoring

---

## 📁 Project Structure

```
hospital_readmission_advanced/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── Dockerfile                         # Container image
├── docker-compose.yml                 # Multi-container orchestration
│
├── api/
│   └── main.py                       # FastAPI application
│
├── dashboard/
│   └── app.py                        # Streamlit dashboard
│
├── model/
│   ├── train_model.py                # Model training script
│   └── model.pkl                     # Trained model (serialized)
│
├── airflow/
│   └── dag_pipeline.py               # Airflow DAG definitions
│
├── processing/
│   └── spark_processing.py           # Spark data processing
│
├── ingestion/
│   └── load_data.py                  # Data loading & ingestion
│
├── database/
│   └── db_connection.py              # Database connection setup
│
├── analysis/
│   └── eda.ipynb                     # Exploratory Data Analysis
│
└── data/
    ├── raw/
    │   └── diabetic_data/
    │       └── diabetic_data.csv     # Raw patient data
    └── processed/
        ├── processed_data.csv         # Processed dataset
        └── eda_visualizations.png     # EDA outputs
```

---

## 🔧 Configuration

### Environment Variables

| Variable       | Description                  | Default             |
| -------------- | ---------------------------- | ------------------- |
| `DATABASE_URL` | PostgreSQL connection string | Required            |
| `MODEL_PATH`   | Path to trained model        | `./model/model.pkl` |
| `API_HOST`     | API server host              | `0.0.0.0`           |
| `API_PORT`     | API server port              | `8000`              |
| `SPARK_HOME`   | Spark installation path      | `/usr/local/spark`  |

### Database Setup

```sql
CREATE DATABASE hospital_db;
CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    age INT,
    admission_type INT,
    time_in_hospital INT,
    readmitted BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 📊 Model Details

### Training Data

- **Source**: Diabetic patient dataset
- **Records**: Patient admissions and readmission outcomes
- **Features**: Demographics, medical history, treatment details
- **Target Variable**: Readmission flag (binary: 0/1)

### Model Performance

- **Algorithm**: Random Forest Classifier (ensemble learning)
- **Train/Test Split**: 80/20
- **Metrics**: Accuracy, Precision, Recall, F1-Score

### Feature Engineering

- Age ranges extracted and converted to numeric
- Categorical features label-encoded
- Normalization applied where needed

---

## 🐳 Docker Deployment

### Build and Run

```bash
# Build images
docker-compose build

# Start services
docker-compose up -d

# View logs
docker-compose logs -f api

# Stop services
docker-compose down
```

### Container Services

- **api**: FastAPI service (port 8000)
- **dashboard**: Streamlit service (port 8501)
- **postgres**: PostgreSQL database (port 5432)
- **spark**: Apache Spark cluster (optional)

---

## 🔍 Monitoring & Debugging

### Check API Health

```bash
curl http://localhost:8000/
```

### View Model Performance

```bash
python model/train_model.py
```

### Run EDA Notebook

```bash
jupyter notebook analysis/eda.ipynb
```

### Monitor Airflow DAGs

```bash
airflow webserver -p 8080
airflow scheduler
```

---

## 🛠️ Development

### Prerequisites for Development

```bash
pip install pytest pytest-cov black flake8 mypy
```

### Code Formatting

```bash
black .
flake8 .
mypy --strict .
```

### Running Tests

```bash
pytest tests/ -v --cov
```

---

## 🚨 Known Issues & Troubleshooting

### scikit-learn Version Warning

**Issue**: `InconsistentVersionWarning` when loading models

```
Trying to unpickle estimator DecisionTreeClassifier from version 1.7.2 when using version 1.8.0
```

**Solution**: Pin scikit-learn version in requirements.txt

```bash
pip install scikit-learn==1.7.2
```

### Database Connection Errors

**Issue**: `psycopg2.OperationalError: could not connect to server`
**Solution**: Ensure PostgreSQL is running and credentials are correct

```bash
# Check PostgreSQL status
psql -U postgres -c "SELECT 1"
```

### Spark Processing Failures

**Issue**: Memory or classpath errors
**Solution**: Adjust Spark configuration in `processing/spark_processing.py`

```python
spark = SparkSession.builder \
    .appName("HospitalProcessing") \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "4g") \
    .getOrCreate()
```

---

## 📈 Performance & Scalability

- **Data Processing**: Spark handles datasets up to terabyte scale
- **API Performance**: Async FastAPI for concurrent requests
- **Model Inference**: Sub-100ms prediction latency
- **Database**: Connection pooling with psycopg2 for high throughput

---

## 🔐 Security Best Practices

- Store credentials in environment variables (`.env` file)
- Use HTTPS in production
- Implement API authentication (JWT tokens recommended)
- Validate and sanitize all inputs
- Keep dependencies updated: `pip install --upgrade -r requirements.txt`

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📞 Support & Contact

For issues, questions, or suggestions:

- Open an [Issue](../../issues) on GitHub
- Submit a [Discussion](../../discussions) for questions
- Check [Troubleshooting](#-known-issues--troubleshooting) section

---

## 🙏 Acknowledgments

- Scikit-learn for ML algorithms
- FastAPI for modern API development
- Streamlit for rapid dashboard development
- Apache Spark for distributed processing
- PostgreSQL for reliable data storage

---

## Author

Manit Srivastava

<div align="center">

**Built with ❤️ for Healthcare Analytics**

[⬆ back to top](#hospital-readmission-prediction-system)

</div>
