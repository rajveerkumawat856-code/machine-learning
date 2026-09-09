import streamlit as st
import pickle
import pandas as pd
import os

# -----------------------------
# Load the trained model
# -----------------------------

model_path = os.path.join(
    os.path.dirname(__file__),
    "LinearRegressionModel.pkl"
)

model = pickle.load(open(model_path, "rb"))


# -----------------------------
# Streamlit App
# -----------------------------

st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗"
)

st.title("🚗 Car Price Prediction")
st.write("Enter the details of the car to predict its price.")


# -----------------------------
# User Inputs
# -----------------------------

name = st.text_input("Car Name")

company = st.text_input("Company")

year = st.number_input(
    "Year",
    min_value=1990,
    max_value=2026,
    value=2018,
    step=1
)

kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=50000,
    step=1000
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG"]
)


# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Price"):

    # Check whether car name and company are entered
    if name == "" or company == "":
        st.warning("Please enter the car name and company.")

    else:

        # Create DataFrame
        input_data = pd.DataFrame(
            [[
                name,
                company,
                year,
                kms_driven,
                fuel_type
            ]],
            columns=[
                "name",
                "company",
                "year",
                "kms_driven",
                "fuel_type"
            ]
        )

        # Make prediction
        prediction = model.predict(input_data)

        # Display result
        st.success(
            f"Estimated Car Price: ₹ {prediction[0]:,.2f}"
        )

        # streamlit run "D:\genai\Machine learning\practice ml algo\car_prediction_model.py"