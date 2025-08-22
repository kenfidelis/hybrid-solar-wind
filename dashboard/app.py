import streamlit as st
import pandas as pd
import pvlib
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Hybrid Solar-Wind Dashboard", layout="wide")

# --- Title ---
st.title("⚡ Hybrid Solar-Wind Power Simulation for Nigeria")

# --- Sidebar Inputs ---
st.sidebar.header("Simulation Settings")

location_choice = st.sidebar.selectbox(
    "Select Location",
    ["Sokoto", "Enugu", "Port Harcourt"]
)

tilt = st.sidebar.slider("PV Tilt Angle (degrees)", 10, 50, 30)
wind_speed = st.sidebar.slider("Average Wind Speed (m/s)", 2, 15, 8)
load = st.sidebar.slider("Grid Load Demand (MW)", 10, 100, 50)

# --- Location Data ---
locations = {
    "Sokoto": {"lat": 13.0059, "lon": 5.2476},
    "Enugu": {"lat": 6.4584, "lon": 7.5464},
    "Port Harcourt": {"lat": 4.8581, "lon": 6.9209},
}

lat, lon = locations[location_choice]["lat"], locations[location_choice]["lon"]
location = pvlib.location.Location(latitude=lat, longitude=lon, tz="Africa/Lagos")

# --- Time Range ---
times = pd.date_range("2025-01-01", "2025-01-02", freq="1h", tz=location.tz)
solpos = location.get_solarposition(times)
cs = location.get_clearsky(times)

# --- PV System ---
system = pvlib.pvsystem.PVSystem(
    surface_tilt=tilt,
    surface_azimuth=180,
    module_parameters={"pdc0": 50000, "gamma_pdc": -0.004},
    inverter_parameters={"pdc0": 50000}
)

poa = system.get_irradiance(
    solpos["apparent_zenith"],
    solpos["azimuth"],
    cs["dni"], cs["ghi"], cs["dhi"]
)

pv_power = system.pvwatts_dc(poa["poa_global"], temp_cell=25) / 1000  # MW

# --- Wind System (simplified) ---
air_density = 1.225  # kg/m³
rotor_area = 2000    # m²
cp = 0.4
wind_power = 0.5 * air_density * rotor_area * (wind_speed**3) * cp / 1e6  # MW constant

# --- Hybrid Output ---
hybrid_power = pv_power + wind_power

# --- Plot Results ---
st.subheader(f"Simulation Results for {location_choice}")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(times, pv_power, label="PV Power (MW)", color="orange")
ax.axhline(y=wind_power, color="blue", linestyle="--", label="Wind Power (MW)")
ax.plot(times, hybrid_power, label="Hybrid Output (MW)", color="green")
ax.axhline(y=load, color="red", linestyle=":", label="Load Demand (MW)")
ax.set_ylabel("Power (MW)")
ax.set_title(f"Hybrid Solar-Wind Simulation at {location_choice}")
ax.legend()
st.pyplot(fig)

# --- Summary ---
st.markdown("### ⚡ Key Results")
st.write(f"- Average PV output: **{pv_power.mean():.2f} MW**")
st.write(f"- Wind farm output: **{wind_power:.2f} MW** (constant)")
st.write(f"- Average Hybrid output: **{hybrid_power.mean():.2f} MW**")
st.write(f"- Grid Load Demand: **{load} MW**")
