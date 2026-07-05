# 📈 House Price Prediction using Linear Regression

This project demonstrates the implementation of **Simple Linear Regression** using **Scikit-learn** to predict house prices based on the living area (`sqft_living`). It covers the complete machine learning workflow, including data loading, preprocessing, model training, evaluation, and visualization.

---

## 📌 Objective

The objective of this project is to understand and implement **Linear Regression** for predicting house prices using a real-world housing dataset.

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

---

## 📂 Dataset

**Dataset:** House Price Dataset

The dataset contains various features related to houses such as:

- Price
- Bedrooms
- Bathrooms
- Living Area (sqft_living)
- Lot Area (sqft_lot)
- Floors
- Waterfront
- View
- Condition
- Grade
- Year Built
- Year Renovated
- Location Details

**Target Variable:**

- `price`

**Feature Used (Simple Linear Regression):**

- `sqft_living`

---

## 📋 Project Workflow

1. Import the required libraries.
2. Load the dataset using Pandas.
3. Explore the dataset.
4. Select feature (`sqft_living`) and target (`price`).
5. Split the dataset into training and testing sets.
6. Train the Linear Regression model.
7. Predict house prices.
8. Evaluate model performance using:
   - Mean Absolute Error (MAE)
   - Mean Squared Error (MSE)
   - R² Score
9. Visualize the regression line.

---

## 📊 Model Evaluation Metrics

The following evaluation metrics are used:

- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **R² Score**

These metrics help evaluate the accuracy and performance of the regression model.

---

## 📉 Regression Plot

The project generates a regression plot showing:

- 🔵 Blue Points → Actual House Prices
- 🔴 Red Line → Predicted Regression Line

The generated plot is saved as:

```
Regression.png
```

---

## ▶️ How to Run

### 1. Install Dependencies

```bash
pip install pandas matplotlib scikit-learn
```

### 2. Run the Project

```bash
python task3.py
```

---

## 📁 Project Structure

```
Task3/
│── House-Price.csv
│── task3.py
│── README.md
│── screenshots/
│   ├── output.png
│   └── Regression.png
```

---

## 📌 Sample Output

```
========== MODEL EVALUATION ==========
Mean Absolute Error (MAE): XXXXX.XX
Mean Squared Error (MSE): XXXXX.XX
R² Score: 0.XX

========== MODEL PARAMETERS ==========
Coefficient (Slope): XXXXX.XX
Intercept: XXXXX.XX
```

---

## 📚 What I Learned

- Understanding Simple Linear Regression
- Preparing data for machine learning
- Splitting datasets into training and testing sets
- Training regression models using Scikit-learn
- Evaluating regression performance using MAE, MSE, and R² Score
- Visualizing regression results using Matplotlib
- Interpreting regression coefficients

---

## 🚀 Future Improvements

- Implement Multiple Linear Regression using additional features.
- Perform feature engineering for improved accuracy.
- Apply feature scaling where required.
- Compare Linear Regression with other regression algorithms.
- Build an interactive web application for house price prediction.

---

## 👨‍💻 Author

**Pragya Pathak**

B.Tech Computer Science Engineering (Machine Learning)

Lovely Professional University

---

## ⭐ Project Highlights

- ✔ Real-world House Price Dataset
- ✔ Simple Linear Regression
- ✔ Data Visualization
- ✔ Model Evaluation
- ✔ Easy to Understand
- ✔ Beginner-Friendly Machine Learning Project