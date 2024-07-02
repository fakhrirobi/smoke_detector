import streamlit as st
import requests
import joblib
from PIL import Image
from IPython.display import display
import json

# Load and set images in the first place

# st.image(header_images)

# Add some information about the service
st.title("Smoke Prediction")
st.subheader("Just enter variabel below then click Predict button :sunglasses:")

# Create form of input
with st.form(key = "air_data_form"):
    # Create box for number input
    temperature = st.number_input(
        label = "1.\tEnter Temperature[C] Value:",
        min_value = -40,
        max_value = 125,
        help = "Value range from -40 to 125"
    )

    humidity = st.number_input(
        label = "2.\tEnter Humidity[%] Value:",
        min_value = 0,
        max_value = 100,
        help = "Value range from 0 to 100"
    )
    
    pressure = st.number_input(
        label = "3.\tEnter Pressure[hPa] Value:",
        min_value = 300,
        max_value = 1250,
        help = "Value range from 300 to 1250"
    )

    pm1 = st.number_input(
        label = "4.\tEnter PM1.0 Value",
        min_value = 0,
        max_value = 65535,
        help = "Value range from 0 to 65535"
    )

    tvoc = st.number_input(
        label = "5.\tEnter TVOC[ppb] Value:",
        min_value = 0,
        max_value = 60000,
        help = "Value range from 0 to 60000"
    )

    eco2 = st.number_input(
        label = "6.\tEnter eCO2[ppm] Value:",
        min_value = 400,
        max_value = 60000,
        help = "Value range from 400 to 60000"
    )

    h2 = st.number_input(
        label = "7.\tEnter Raw H2 Value:",
        min_value = 0,
        max_value = 60000,
        help = "Value range from 0 to 60000"
    )

    ethanol = st.number_input(
        label = "8.\tEnter Raw Ethanol Value:",
        min_value = 0,
        max_value = 60000,
        help = "Value range from 0 to 60000"
    )
    
    # Create button to submit the form
    submitted = st.form_submit_button("Predict")

    # Condition when form submitted
    if submitted:
        # Create dict of all data in the form

        raw_data = {

            "Humidity": humidity,
            "Pressure": pressure,
            "PM1": pm1,
            "TVOC": tvoc,
            "H2": h2,
            "Ethanol": ethanol
        }
        print(raw_data)
        # raw_data = json.dumps(raw_data)
        # Create loading animation while predicting
        with st.spinner("Sending data to prediction server ..."):
            res = requests.post("http://108.136.169.48:8000/predict", json = raw_data).json()
            print(res)
        # Parse the prediction result
        if res["error_msg"] != "":
            st.error("Error Occurs While Predicting: {}".format(res["error_msg"]))
        else:
            if res["res"] != "Tidak ada api.":
                st.warning("Ada api.")
            else:
                st.success("Tidak ada api.")