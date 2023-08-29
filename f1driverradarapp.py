import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ergast API base URL
ERGAST_BASE_URL = "https://ergast.com/api/f1"

# Function to fetch driver data from the API
def get_driver_data(driver_id, circuit_id):
    url = f"{ERGAST_BASE_URL}/drivers/{driver_id}/circuits/{circuit_id}/results.json"
    response = requests.get(url)
    data = response.json()
    return data

driver_data = get_driver_data(1, 1)

# Function to create a radar chart
def create_radar_chart(data, labels, title):
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
    data = np.concatenate((data, [data[0]]))  # Close the plot
    angles = np.concatenate((angles, [angles[0]]))  # Close the plot

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, data, color='blue', linewidth=2)
    ax.fill(angles, data, color='blue', alpha=0.25)
    ax.set_thetagrids(angles * 180 / np.pi, labels)
    ax.set_title(title)
    ax.grid(True)

    return fig

# Streamlit app
def main():
    st.title("F1 Driver Comparison at a Race Track")
    
    # Sidebar input
    driver_id = st.sidebar.text_input("Enter Driver ID (e.g., hamilton):")
    circuit_id = st.sidebar.text_input("Enter Circuit ID (e.g., monza):")
    
    if st.sidebar.button("Compare"):
        # Fetch data
        driver_data = get_driver_data(driver_id, circuit_id)
        
        # Extract relevant data
        results = driver_data["MRData"]["RaceTable"]["Races"][0]["Results"]
        driver_names = [result["Driver"]["familyName"] for result in results]
        points = [int(result["points"]) for result in results]
        
        # Create radar chart
        st.write("Radar Chart of Points")
        radar_chart = create_radar_chart(points, driver_names, f"F1 Driver Comparison at {circuit_id.capitalize()} Circuit")
        st.pyplot(radar_chart)

if __name__ == "__main__":
    main()


