Heart Disease prediction project uses Machine Learning with the Random Forest Classifier to predict the likelihood of heart disease based on user input. The project includes:

Frontend (HTML, CSS, JavaScript): A web form collects user data such as age, gender, blood pressure, cholesterol, and other medical parameters. On submission, the form sends the data to the backend for prediction.
Backend (Flask): Handles HTTP requests and routes. The /predict route processes user input and displays the prediction result.
Machine Learning Model: Utilizes the RandomForestClassifier from scikit-learn, trained on a heart disease dataset (heart.csv). The dataset is split into training and testing sets using train_test_split.
Prediction Function: Takes input parameters, runs the trained classifier, and returns a message indicating whether the user is likely to have heart disease or not.
Result Display: The prediction result is displayed on the same web page after form submission.
This project demonstrates integrating machine learning models into a web application for health-related predictions.
