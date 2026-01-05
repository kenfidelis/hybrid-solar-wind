import pvlib
import pandas as pd
import matplotlib.pyplot as plt

# Location (Enugu, Nigeria)
location = pvlib.location.Location(latitude=6.4584, longitude=7.5464, tz="Africa/Lagos")

# Time range (hourly, 1 day)
times = pd.date_range("2025-01-01", "2025-01-02", freq="1h", tz=location.tz)

# Solar position + clear-sky irradiance
solpos = location.get_solarposition(times)
cs = location.get_clearsky(times, model="ineichen")  # ghi, dni, dhi

# Plane-of-array irradiance (tilt/azimuth)
surface_tilt = 30
surface_azimuth = 180

poa = pvlib.irradiance.get_total_irradiance(
    surface_tilt=surface_tilt,
    surface_azimuth=surface_azimuth,
    solar_zenith=solpos["apparent_zenith"],
    solar_azimuth=solpos["azimuth"],
    dni=cs["dni"],
    ghi=cs["ghi"],
    dhi=cs["dhi"],
)

# PVWatts DC model (W)
pdc0_w = 50_000  # 50 kW
pv_power_w = pvlib.pvsystem.pvwatts_dc(
    g_poa_effective=poa["poa_global"],
    temp_cell=25,
    pdc0=pdc0_w,
    gamma_pdc=-0.004
)

# Plot
plt.figure(figsize=(10, 4))
plt.plot(pv_power_w.index, pv_power_w.values, label="PV Power (W)")
plt.title("PV Output (Clear-sky, Sample Day - Enugu)")
plt.ylabel("Power (W)")
plt.xlabel("Time")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
