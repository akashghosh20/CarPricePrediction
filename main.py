# from flask import Flask,render_template
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('Template/index.html')
#
#
# if __name__ =="__main__":
#     app.run(debug=True)

import streamlit as st
import pandas as pd
import pickle

# Load the machine learning model
model = pickle.load(open("CarPricingModel.pkl",'rb'))  # Replace with the path to your model file
# Create a function to predict car prices
def predict_car_price(name, company, year, kms_driven, fuel_type):
    features = pd.DataFrame({
        'name': [name],
        'company': [company],
        'year': [year],
        'kms_driven': [kms_driven],
        'fuel_type': [fuel_type]
    })

    predicted_price = model.predict(features)
    return predicted_price[0]

# Streamlit UI
st.title('Car Price Prediction')

# Input form for user to provide feature values
name = st.text_input('Car Name')
company = st.text_input('Car Company')
year = st.number_input('Year of Manufacture', min_value=1950, max_value=2023)
kms_driven = st.number_input('Kilometers Driven')
fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG', 'LPG'])

# Make a prediction when the user clicks the 'Predict' button
if st.button('Predict'):
    if not name or not company:
        st.warning('Please fill in the car name and company.')
    else:
        try:
            predicted_price = predict_car_price(name, company, year, kms_driven, fuel_type)
            st.success(f'Predicted Price: ₹ {predicted_price:.2f}')
        except Exception as e:
            st.error(f'An error occurred: {e}')

# Add a sidebar with some information or options
st.sidebar.markdown('## About')
st.sidebar.info('This is a simple web app for predicting car prices based on features.')

# You can add more content or options to the sidebar if needed

# Sample data
st.sidebar.markdown('## Sample Data')
sample_data = {
    'name': 'Honda City',
    'company': 'Honda',
    'year': 2019,
    'kms_driven': 45000,
    'fuel_type': 'Petrol'
}

if st.sidebar.checkbox('Use Sample Data'):
    name = sample_data['name']
    company = sample_data['company']
    year = sample_data['year']
    kms_driven = sample_data['kms_driven']
    fuel_type = sample_data['fuel_type']
    st.text('Sample data is filled in for demonstration.')

# You can add more customization to the UI, such as styling or additional features.
