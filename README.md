# Janani_cardheko
Car Dheko - Used Car Price Prediction

****About CarDekho**
**CarDekho.com has launched many innovative features to ensure that users get an immersive experience of the car model before visiting a dealer showroom. These include a Feel The Car tool that gives 360-degree interior/exterior views with sounds of the car and explanations of features with videos; search and comparison by make, model, price, features; and live offers and promotions in all cities. The platform also has used car classifieds wherein users can upload their cars for sale, and find used cars for buying from individuals and used car dealers.

Data Collected From: [CarDekho](https://www.cardekho.com/used-car-details/used-Maruti-Swift-Dzire-Vdi-cars-Chennai_afcd7bde-0a0d-4a47-b514-7b10cdff2767.htm)
Dataset Link: [Dataset](https://drive.google.com/drive/folders/16U7OH7URsCW0rf91cwyDqEgd9UoeZAJh)
Feature Description Link: [Features](https://docs.google.com/document/d/1hxW7IvCX5806H0IsG2Zg9WnVIpr2ZPueB4AElMTokGs/edit?usp=sharing)

Problem Statement:

The primary objective of is project is to create a data science solution for predicting used car prices accurately by analyzing a diverse dataset including car model, no. of owners, age, mileage, fuel type, kilometers driven, features and location. The aim is to build a machine learning model that offers users to find current valuations for used cars.

Data Understanding

The Dataset contains multiple excel files, each represents its city, columns in each excel gives you an overview of each car, its details, specification and available features.

Data Collected From: https://www.cardekho.com/usedCars

**** **1.Data Processing**
****Import and concatenate:
Import all city’s dataset which is in unstructured format.
Convert it into a  structured format.
Add a new column named ‘City’ and assign values for all rows with the name of the respective city.
Concatenate all datasets and make it as a single dataset.
Handling Missing Values: Identify and fill or remove missing values in the dataset.
For numerical columns, use techniques like mean, median, or mode imputation.
For categorical columns, use mode imputation or create a new category for missing values.
Standardising Data Formats:
Check for all data types and do the necessary steps to keep the data in the correct format.
Encoding Categorical Variables: Convert categorical features into numerical values using encoding techniques.
Use one-hot encoding for nominal categorical variables.
Use label encoding or ordinal encoding for ordinal categorical variables.
Normalizing Numerical Features: Scale numerical features to a standard range, usually between 0 and 1.( For necessary algorithms)

**** 2. **Exploratory Data Analysis (EDA)******
****Descriptive Statistics: Calculate summary statistics to understand the distribution of data.
Mean, median, mode, standard deviation, etc.
Data Visualization: Create visualizations to identify patterns and correlations.
Use scatter plots, histograms, box plots, and correlation heatmaps.



 3. **Model Development**
Train-Test Split: Split the dataset into training and testing sets to evaluate model performance.
Common split ratios are 70-30 or 80-20.
Model Selection: Choose appropriate machine learning algorithms for price prediction.
Linear Regression, Decision Trees, Random Forests, Gradient Boosting Machines, etc.
Model Training: Train the selected models on the training dataset.
Use cross-validation techniques to ensure robust performance.
.
 4. **Model Evaluation**
Mean Absolute Error (MAE), Mean Squared Error (MSE), R-squared.

5. **Optimization**
Feature Engineering: Create new features or modify existing ones to improve model performance.
Use domain knowledge and exploratory data analysis insights.
Regularization: Apply regularization techniques to prevent overfitting.
Lasso (L1) and Ridge (L2) regularization.

6.**Deployment**
Streamlit Application: Deploy the final model using Streamlit to create an interactive web application.
Allow users to input car features and get real-time price predictions.











