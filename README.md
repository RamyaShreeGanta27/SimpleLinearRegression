# SimpleLinearRegression
# Height and Weight Prediction Using Simple Linear Regression

## 📌 Project Overview

The **Height and Weight Prediction** project is a Machine Learning application that predicts a person's weight based on their height using **Simple Linear Regression**.

The model is trained using a dataset containing height and weight values. After training, the model is saved as a Pickle file and integrated with a Flask web application.

Users can enter their height through a simple web interface and get the predicted weight instantly.

## 🎯 Objectives

- Understand and implement Simple Linear Regression.
- Analyze the relationship between height and weight.
- Train a machine learning model using Scikit-learn.
- Save and load the trained model using Pickle.
- Develop a user-friendly web application using Flask and HTML/CSS.
- Generate predictions based on user input.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| NumPy | Numerical operations |
| Pandas | Data manipulation |
| Matplotlib | Data visualization |
| Scikit-learn | Machine Learning model |
| Flask | Backend web framework |
| HTML | Webpage structure |
| CSS | Website styling |
| Pickle | Saving and loading the model |

## 📂 Project Structure

```text
Height-Weight-Prediction/
│
├── app.py
│
├── SLR_MODEL (1).pkl
│
├── data.csv
│
├── templates/
│   └── index.html
│
└── README.md
```

## 📊 Dataset

The dataset contains two main attributes:

- **Height:** Input feature used to predict weight.
- **Weight:** Target variable to be predicted.

The dataset is used to train the Simple Linear Regression model.

## 🤖 Machine Learning Algorithm

This project uses **Simple Linear Regression**, a supervised machine learning algorithm that establishes a linear relationship between one independent variable and one dependent variable.

The model learns the relationship between height and weight from the training dataset.

### Regression Equation

`Y = mX + C`

Where:

- Y = Predicted Weight
- X = Height
- m = Slope (coefficient)
- C = Intercept

## ⚙️ Project Workflow

1. Import the required Python libraries.
2. Load the height and weight dataset using Pandas.
3. Perform data analysis and visualization.
4. Separate independent and dependent variables.
5. Train the Simple Linear Regression model.
6. Save the trained model using Pickle.
7. Load the saved model into the Flask application.
8. Accept height as input from the user.
9. Pass the input to the trained model.
10. Display the predicted weight on the website.

## 🌐 Web Application

The project uses Flask to connect the machine learning model with the frontend.

**Frontend:**
- HTML for webpage structure.
- CSS for styling.
- Height input field.
- Predict Weight button.
- Reset button.
- Predicted weight display.

**Backend:**
- Flask handles user requests.
- Loads the trained Pickle model.
- Receives height from the HTML form.
- Generates weight predictions.
- Sends the result back to the webpage.

## 🚀 Installation and Execution

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Folder

```bash
cd Height-Weight-Prediction
```

### 3. Install Required Libraries

```bash
pip install numpy pandas matplotlib scikit-learn flask
```

### 4. Run the Flask Application

```bash
python app.py
```

### 5. Open the Website

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

Enter your height and click the **Predict Weight** button to view the predicted result.

## 📈 Expected Output

The application accepts height as input and displays the corresponding predicted weight based on the trained Simple Linear Regression model.

Example:

```text
Height: 1.70 meters

Predicted Weight: Model-generated result in kg
```

## 🔮 Future Enhancements

- Improve model accuracy using additional training data.
- Add model performance evaluation.
- Display regression graphs and prediction visualizations.
- Develop a more responsive user interface.
- Compare Simple Linear Regression with other regression algorithms.

## 👩‍💻 Author

**G. Ramya Shree**

Artificial Intelligence and Machine Learning Graduate

## 📌 Conclusion

This project demonstrates the practical implementation of Simple Linear Regression for predicting weight based on height. It combines machine learning with Flask web development to create a simple and interactive prediction application.
