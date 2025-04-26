# Transit Delay Prediction 🚍🌦️

Public transit reliability is a major concern for urban commuters. Understanding and predicting delays can significantly improve commuter experiences and help the Chicago Transit Authority (CTA) optimize its operations.

This project aims to build a machine learning model that predicts whether a bus will be delayed, using real-world data collected over multiple sources.

## 📊 Data Overview:

Location Data: Route, Destination, nearest_stop_name, distance_to_stop

Time Data: Timestamp, time, year_month, is_day()

Weather Data: temperature_2m (°C), rain (mm), snowfall (cm), snow_depth (m), wind_speed_10m (km/h), cloud_cover (%), etc.

Target Variable: Delay (boolean)

## 🏆 Results:

The model achieved a recall of 93% for predicting delays, demonstrating strong effectiveness in correctly identifying delayed instances.

Better predictions → Better decisions → Happier riders + More efficient city.

## 📱 Future Work

We plan to develop a mobile application that allows users to input key information such as Route, Temperature, and Time to predict whether their bus is likely to be delayed.

## 🔧 Tech Stack:

Python (Pandas, Scikit-learn, XGBoost)

Jupyter Notebooks

Machine Learning classification models

Visualization (Matplotlib, Seaborn)
