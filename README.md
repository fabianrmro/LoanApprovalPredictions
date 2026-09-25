# 💳 Loan Approval Predictions

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/MLflow-Experiment%20Tracking-0194E2?style=for-the-badge&logo=mlflow&logoColor=white" alt="MLflow">
  <img src="https://img.shields.io/badge/Kaggle-Competition-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" alt="Kaggle">
</p>

<h3 align="center">
  Machine Learning Project for Loan Approval Prediction
</h3>

<p align="center">
  End-to-end Machine Learning workflow using Scikit-learn, MLflow and Kaggle.
</p>

---

# 👨‍💻 Author

## Fabian R.

Machine Learning & Data Science Project

🔗 **GitHub Repository:**  
https://github.com/fabianrmro/LoanApprovalPredictions

---

# 📌 About the Project

**Loan Approval Predictions** is an end-to-end Machine Learning project focused on predicting whether a loan application will be approved.

The project was developed using the **Loan Approval Prediction** Kaggle competition from the Playground Series.

The main goal was not only to train a classification model, but also to implement a complete Machine Learning workflow including:

- 📊 Exploratory Data Analysis
- 🧹 Data preprocessing
- ⚙️ Feature engineering
- 🤖 Machine Learning model training
- 📈 Model evaluation
- 🎚️ Classification threshold optimization
- 🧪 Experiment tracking with MLflow
- 📦 Model and artifact logging
- 📄 Submission file generation
- 🏆 Kaggle submission

The project therefore covers the complete process from raw data to a final competition submission.

---

# 🎯 Project Objective

The objective of this project is to develop a binary classification model capable of predicting the `loan_status` of unseen loan applications.

The target variable is:

| Value | Meaning |
|:---:|---|
| `0` | Loan not approved |
| `1` | Loan approved |

The final predictions are generated using the format required by Kaggle.

---

# 🏆 Kaggle Competition

This project was developed for the following Kaggle competition:

## Loan Approval Prediction — Playground Series S4E10

🔗 **Kaggle Competition:**  
https://www.kaggle.com/competitions/playground-series-s4e10

🔗 **GitHub Repository:**  
https://github.com/fabianrmro/LoanApprovalPredictions

The final prediction file was successfully submitted to Kaggle using the **Kaggle CLI**.

---

# 🧠 Machine Learning Workflow

The complete workflow implemented in this project can be summarized as:

```text
                         ┌─────────────────────┐
                         │       DATASET       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ EXPLORATORY DATA    │
                         │      ANALYSIS       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ DATA PREPROCESSING  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ FEATURE ENGINEERING │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   MODEL TRAINING    │
                         │  Random Forest      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ MODEL EVALUATION    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ THRESHOLD           │
                         │ OPTIMIZATION        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │       MLFLOW        │
                         │ EXPERIMENT TRACKING │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   SUBMISSION.CSV    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │       KAGGLE        │
                         │     SUBMISSION      │
                         └─────────────────────┘
````

---

# 📊 Dataset

The project uses the dataset provided by the Kaggle competition.

The training dataset contains:

* **58,645 observations**

The test dataset contains:

* **39,098 observations**

The final submission contains:

* **39,098 predictions**
* **2 columns**
* `id`
* `loan_status`

### Submission format

```csv
id,loan_status
58645,1
58646,0
58647,1
58648,0
58649,0
```

The generated submission file was checked before uploading it to Kaggle.

---

# 🔍 Exploratory Data Analysis

The project includes an exploratory analysis of the dataset to understand:

* Dataset structure
* Feature types
* Missing values
* Numerical variables
* Categorical variables
* Target distribution
* Relationships between variables
* Relevant patterns within the data

The analysis was performed using Python and common Data Science libraries such as:

* Pandas
* NumPy
* Matplotlib
* Seaborn

---

# 🧹 Data Preprocessing

Before training the Machine Learning model, the dataset goes through a preprocessing pipeline.

The preprocessing workflow handles the different types of features and prepares the data for model training.

The objective is to ensure that the same transformations are applied consistently to both training and test data.

---

# 🤖 Machine Learning Model

The project uses a classification pipeline based on:

## 🌲 Random Forest Classifier

The Random Forest model is used to predict the probability of loan approval.

The project then uses:

```text
TunedThresholdClassifierCV
```

to optimize the classification threshold.

Instead of automatically using:

```text
threshold = 0.5
```

the project evaluates different thresholds in order to identify an operating point based on the evaluation process used in the notebook.

---

# 🎚️ Threshold Optimization

One of the important aspects of this project is the analysis of the classification threshold.

A binary classifier normally converts predicted probabilities into classes using a threshold.

For example:

```text
Probability >= 0.5 → Class 1
Probability < 0.5  → Class 0
```

However, the default threshold of `0.5` is not necessarily the only threshold worth evaluating.

This project therefore evaluates different thresholds and compares metrics such as:

* AUC
* False Positive Rate
* True Positive Rate

The threshold selected during the experiment was:

```text
Optimal Threshold = 0.19192
```

---

# 📈 Model Results

The selected MLflow run produced the following metrics:

| Metric                      |       Value |
| --------------------------- | ----------: |
| **AUC**                     | **0.86998** |
| **Optimal Threshold**       | **0.19192** |
| **FPR — Optimal Threshold** | **0.06394** |
| **TPR — Optimal Threshold** | **0.80390** |
| **Average Threshold**       | **0.50000** |
| **FPR — Average Threshold** | **0.01081** |
| **TPR — Average Threshold** | **0.72107** |

### 📊 AUC

The model achieved an AUC of approximately:

```text
0.86998
```

in the evaluation performed during the project.

---

# 🧪 MLflow Experiment Tracking

**MLflow** was used to track the Machine Learning experiment.

The experiment stores:

* Model information
* Evaluation metrics
* Model artifacts
* Submission artifacts
* Experiment runs

### MLflow Experiment

```text
loan_prediction
```

### MLflow Run ID

```text
98f55631a65a4debbe89554df326f102
```

### MLflow Run Name

```text
ambitious-deer-694
```

---

# 📊 Logged Metrics

The following metrics were logged to MLflow:

```text
auc
optimal_threshold
fpr_optimal
tpr_optimal
average_threshold
fpr_average
tpr_average
```

This makes it possible to keep track of the experiment and reproduce the evaluation results.

---

# 📦 MLflow Artifacts

The MLflow run contains the generated submission artifact:

```text
submission.csv
```

The file was downloaded from the MLflow run and checked before being submitted to Kaggle.

The downloaded file contains:

```text
Shape: (39098, 2)

Columns:
- id
- loan_status
```

---

# 🔐 MLflow Model Logging

During model logging, MLflow detected several Scikit-learn objects that were not automatically considered trusted by the model serialization layer.

The model was therefore logged by explicitly specifying the trusted types used by the trained model.

The following configuration was used:

```python
mlflow.sklearn.log_model(
    model,
    name="model",
    skops_trusted_types=[
        "sklearn.metrics._ranking.roc_auc_score",
        "sklearn.metrics._scorer._CurveScorer",
        "sklearn.metrics._scorer._Scorer",
        "sklearn.tree._tree.Tree",
        "sklearn.utils._metadata_requests.MetadataRequest",
        "sklearn.utils._metadata_requests.MethodMetadataRequest",
    ],
)
```

After applying this configuration, the model was successfully logged to MLflow.

---

# 🏆 Kaggle Submission

Once the submission file had been generated and validated, it was uploaded directly to Kaggle using the Kaggle CLI.

The command used was:

```bash
kaggle competitions submit \
    -c playground-series-s4e10 \
    -f "submission.csv" \
    -m "Submission from MLflow run 98f55631"
```

# 🛠️ Technologies Used

| Technology              | Purpose                 |
| ----------------------- | ----------------------- |
| 🐍 **Python 3.12**      | Programming language    |
| 🐼 **Pandas**           | Data manipulation       |
| 🔢 **NumPy**            | Numerical computation   |
| 🤖 **Scikit-learn**     | Machine Learning        |
| 🌲 **Random Forest**    | Classification model    |
| 📈 **Matplotlib**       | Data visualization      |
| 🎨 **Seaborn**          | Data visualization      |
| 🧪 **MLflow**           | Experiment tracking     |
| 🏆 **Kaggle CLI**       | Competition submission  |
| 📓 **Jupyter Notebook** | Development environment |
| 🌿 **Git**              | Version control         |
| 🐙 **GitHub**           | Project repository      |

---

# 📂 Project Structure

LoanApprovalPredictions/
│
├── 📁 data/
│   ├── 📄 sample_submission.csv
│   ├── 📄 submission.csv
│   ├── 📄 test.csv
│   └── 📄 train.csv
│
├── 📁 notebook/
│   └── 📓 MLFlow IV - Kaggle II (1).ipynb
│
├── 📁 screenshots/
│   ├── 📸 Kaggle.png
│   ├── 📸 loanApprovePrediction.png
│   └── 📸 submission.png
│
├── 📄 requirements.txt
├── 📄 submission.csv
└── 📄 README.md

> The exact structure may vary depending on the current version of the repository.

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/fabianrmro/LoanApprovalPredictions.git
```

Move into the project directory:

```bash
cd LoanApprovalPredictions
```

---

## 2. Create the Conda environment

Create a dedicated environment using Python 3.12:

```bash
conda create -n loan-approval python=3.12 -y
```

Activate it:

```bash
conda activate loan-approval
```

---

## 3. Install the dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

# 🧪 Running MLflow

Start the local MLflow tracking server:

```bash
mlflow server
```

The MLflow interface will be available at:

```text
http://127.0.0.1:5000
```

In the Jupyter Notebook, configure MLflow using:

```python
import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000")

mlflow.set_experiment("loan_prediction")
```

---

# 📓 Running the Notebook

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Then open:

```text
MLFlow IV - Kaggle II (1).ipynb
```

Run the notebook cells sequentially to reproduce the workflow.

---

# 📊 Reproducibility

To reproduce the project:

### Step 1

Clone the repository:

```bash
git clone https://github.com/fabianrmro/LoanApprovalPredictions.git
```

### Step 2

Create the environment:

```bash
conda create -n loan-approval python=3.12 -y
```

### Step 3

Activate the environment:

```bash
conda activate loan-approval
```

### Step 4

Install dependencies:

```bash
pip install -r requirements.txt
```

### Step 5

Start MLflow:

```bash
mlflow server
```

### Step 6

Open the notebook:

```bash
jupyter notebook
```

### Step 7

Run the Machine Learning workflow.

### Step 8

Generate the submission file.

### Step 9

Log the experiment and artifacts to MLflow.

### Step 10

Submit the predictions to Kaggle.

---

# 🔗 Project Links

## 💻 GitHub

**LoanApprovalPredictions**

[https://github.com/fabianrmro/LoanApprovalPredictions](https://github.com/fabianrmro/LoanApprovalPredictions)

---

## 🏆 Kaggle

**Loan Approval Prediction — Playground Series S4E10**

[https://www.kaggle.com/competitions/playground-series-s4e10](https://www.kaggle.com/competitions/playground-series-s4e10)

---

# 📌 Key Takeaways

This project demonstrates a complete Machine Learning workflow:

```text
📊 Data
   ↓
🔍 Analysis
   ↓
🧹 Preprocessing
   ↓
⚙️ Feature Engineering
   ↓
🤖 Random Forest
   ↓
📈 Evaluation
   ↓
🎚️ Threshold Optimization
   ↓
🧪 MLflow
   ↓
📄 Submission CSV
   ↓
🏆 Kaggle
```

The project combines model development with experiment tracking and deployment of predictions to a real Kaggle competition environment.

---

# 🚀 Final Result

The project successfully completed the complete workflow:

### ✅ Dataset processed

### ✅ Machine Learning model trained

### ✅ Model evaluated

### ✅ Classification threshold optimized

### ✅ Metrics tracked with MLflow

### ✅ Model logged to MLflow

### ✅ `submission.csv` generated

### ✅ Submission file validated

### ✅ Kaggle submission completed successfully

---

# 👨‍💻 About the Author

## Fabian R. M.

Machine Learning & Data Science

This project was developed as part of a practical Machine Learning workflow focused on classification, experiment tracking and Kaggle competition submission.

### 🔗 GitHub

[https://github.com/fabianrmro/LoanApprovalPredictions](https://github.com/fabianrmro/LoanApprovalPredictions)

---

<p align="center">

## 💳 Loan Approval Predictions

### Machine Learning · Scikit-learn · MLflow · Kaggle

**Made by Fabian R. M.**

⭐ Thanks for visiting the project! ⭐

</p>
```
