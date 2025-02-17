Real-Time Fraud Detection System

Overview
This project implements a real-time fraud detection system for mobile payment transactions using machine learning models.

The system leverages a Random Forest model trained on credit card transaction data and deploys a real-time prediction pipeline using Kafka.

📂 Project Structure:
- `requirements.txt` - Python dependencies
- `data_preprocessing.py` - Data preprocessing script
- `model_training.py` - Model training script
- `real_time_pipeline.py` - Real-time prediction pipeline
- `utils.py` - Utility functions
- `charts/` - Visual charts from the dataset
- `.gitignore` - Ignore unnecessary files


🚀 Instructions to Run the Project
1. Install dependencies:**  
   pip install -r requirements.txt

2. Run data preprocessing:
   python data_preprocessing.py
 

3. Train the model:
   python model_training.py
   
4.Start the real-time prediction pipeline:
   python real_time_pipeline.py



 📊 Visualizations
Class Distribution (Legit vs Fraud)
Pair Plot of V1, V2, V3 Features


⚙️ Dependencies
- Python 3.8+
- Pandas
- Numpy
- Scikit-learn
- Matplotlib
- Joblib
- Kafka-python


📜 License
This project is licensed under the MIT License.

