import streamlit as st
import requests
import plotly.express as px

class RaceCircuit:
    def __init__(self, name, tire_deg_rates, pit_loss_time):
        self.name = name
        self.tire_deg_rates = tire_deg_rates  # Dictionary of tire degradation rates per lap for different compounds
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

        # Simulate tire strategies and find the quickest one
        strategies = {}
        for circuit in [circuit_monaco, circuit_silverstone]:
            strategy_times = []
            for compound, deg_rate in circuit.tire_deg_rates.items():
                strategy_time = analyze_strategy(circuit, laps, starting_tire_condition, num_pit_stops, deg_rate)
                strategy_times.append((compound, strategy_time))
            strategies[circuit.name] = min(strategy_times, key=lambda x: x[1])

        # Create a Plotly bar chart to visualize quickest tire strategies
        circuit_names = list(strategies.keys())
        compound_names = [compound for compound, _ in strategies.values()]
        times = [time for _, time in strategies.values()]

        fig = px.bar(x=circuit_names, y=times, color=compound_names,
                     labels={"x": "Circuit", "y": "Total Time (seconds)"})
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()

