import numpy as np
import matplotlib.pyplot as plt

# Wind turbine parameters
air_density = 1.225  # kg/m³
rotor_area = 100  # m²
cp = 0.4  # Power coefficient
rated_power = 1500  # kW

# Example wind speed profile (10 hours)
wind_speeds = np.array([3, 5, 7, 9, 11, 12, 14, 16, 18, 20])  # m/s

# Power output calculation (Betz law)
power_output = 0.5 * air_density * rotor_area * (wind_speeds**3) * cp / 1000  # in kW

# Apply rated limit
power_output = np.clip(power_output, 0, rated_power)

plt.plot(wind_speeds, power_output, 'o-', label="Wind Power (kW)")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Power Output (kW)")
plt.title("Wind Turbine Power Curve")
plt.legend()
plt.show()
