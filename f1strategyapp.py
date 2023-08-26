import streamlit as st
import requests
import plotly.express as px

class RaceCircuit:
    def __init__(self, name, tire_deg_rate, pit_loss_time):
        self.name = name
        self.tire_deg_rate = tire_deg_rate  # Tire degradation rate per lap
        self.pit_loss_time = pit_loss_time  # Time lost during a pit stop

def fetch_race_data(season, round_num):
    url = f"http://ergast.com/api/f1/{season}/{round_num}/results.json"
    response = requests.get(url)
    data = response.json()
    race_results = data.get("MRData", {}).get("RaceTable", {}).get("Races", [])[0].get("Results", [])
    return race_results

def main():
    st.title("Formula 1 Race Strategy Analysis")

    # User inputs
    season = st.text_input("Enter the season (e.g., 2023):")
    round_num = st.text_input("Enter the round number:")
    starting_tire_condition = st.slider("Starting Tire Condition (%)", min_value=0, max_value=100, value=100)

    # Fetch race data using Ergast API
    if st.button("Fetch Race Data"):
        race_data = fetch_race_data(season, round_num)
        # Extract relevant information (e.g., starting tire condition)
        # You can replace this with the actual data from the API

        # Rest of the code (linear regression, predicting lap times, etc.)
        # ...

        # Create a Plotly bar chart to visualize predicted lap times
        circuit_names = ["Monaco", "Silverstone"]
        predicted_lap_times = [predicted_lap_time_monaco[0], predicted_lap_time_silverstone[0]]

        fig = px.bar(x=circuit_names, y=predicted_lap_times, labels={"x": "Circuit", "y": "Predicted Lap Time (seconds)"})
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()
