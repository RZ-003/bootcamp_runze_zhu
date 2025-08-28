Project Overview and Objectives:
This project demonstrates the process of moving a basic machine learning workflow from the prototype to productization. A basic linear regression model is trained, saved using Pickle, and served through a Flask API. 

The Way to Run:
Use pip install -r requirements.txt to install all the required packages.
Open and run stage13_productization.ipynb from start to end

Assumptions, risks, and lifecycle mapping:
Assumptions: We assume a gingle-feature numeric input
Risks: API routes must be updated if the feature count changes.

Instructions for using APIs or dashboards:
Single input prediction (1-feature models): http://127.0.0.1:5000/predict/2.0
Plot predictions: http://127.0.0.1:5000/plot