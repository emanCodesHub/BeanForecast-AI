# ==========================================
# BeanForecast AI - Model Training Script
# ==========================================

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import numpy as np

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv(
    "data/BeanForecast_AI_Advanced_Dataset_5000_Rows.csv"
)

print("Dataset Loaded Successfully!")
print(df.head())

# ==========================================
# Remove Date
# ==========================================

df = df.drop(columns=["Date"])

# ==========================================
# Features & Target
# ==========================================

X = df.drop("DailyRevenue", axis=1)
y = df["DailyRevenue"]

# ==========================================
# Categorical & Numerical Columns
# ==========================================

categorical_features = [
    "DayOfWeek",
    "Season",
    "TopSellingProduct"
]

numerical_features = [
    col for col in X.columns
    if col not in categorical_features
]

# ==========================================
# Preprocessing
# ==========================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)

# ==========================================
# Pipeline
# ==========================================

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LinearRegression())
])

# ==========================================
# Train Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ==========================================
# Train Model
# ==========================================

pipeline.fit(X_train, y_train)

print("\nModel Trained Successfully!")

# ==========================================
# Prediction
# ==========================================

y_pred = pipeline.predict(X_test)

# ==========================================
# Evaluation
# ==========================================

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\n========== Model Performance ==========")
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

# ==========================================
# Save Pipeline
# ==========================================

joblib.dump(
    pipeline,
    "models/beanforecast_pipeline.pkl"
)

print("\nPipeline Saved Successfully!")