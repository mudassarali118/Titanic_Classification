# Titanic Survival Prediction

A Machine Learning web application that predicts whether a passenger would survive the Titanic disaster using a **Logistic Regression** model built with **Scikit-learn**.

## Features

* Predicts passenger survival.
* Trained using Logistic Regression.
* Handles missing values before training.
* Uses one-hot encoding for categorical features.
* Interactive web interface built with Streamlit.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle

## Input Features

* Passenger Class (Pclass)
* Sex
* Age
* Fare
* Embarked
* Number of Siblings/Spouses (SibSp)
* Number of Parents/Children (Parch)

## Project Structure

```text
├── app.py
├── train_model.py
├── Titanic-Dataset.csv
├── titanic_model.pkl
├── requirements.txt
└── README.md
```

## How to Run

1. Clone the repository.
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## Live Demo

**Streamlit App:** *https://titanicclassification-jvodbjwrrnzomkto6wg4bg.streamlit.app*

## Author

**Mudassar Ali**
