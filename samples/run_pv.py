import pvlib
import pandas as pd
import matplotlib.pyplot as plt

# Location (Enugu, Nigeria as example)
location = pvlib.location.Location(latitude=6.4584, longitude=7.5464, tz='Africa/Lagos')

# Example time range
times = pd.date_range('2025-01-01', '2025-01-02', freq='1h', tz=location.tz)

# Solar position
solpos = location.get_solarposition(times)

# Example clear sky irradiance
cs = location.get_clearsky(times)  # ghi, dni, dhi

pdc0_w = 50_000  # 50 kW
...
pv_power_w = pvlib.pvsystem.pvwatts_dc(poa["poa_global"], temp_cell=25, pdc0=pdc0_w, gamma_pdc=-0.004)
plt.plot(pv_power_w.index, pv_power_w.values, label="PV Power (W)")


# Simple PV system parameters
system = pvlib.pvsystem.PVSystem(surface_tilt=30, surface_azimuth=180, 
                                  module_parameters={'pdc0': 100, 'gamma_pdc': -0.004},
                                  inverter_parameters={'pdc0': 100})

# Calculate effective irradiance
aoi = system.get_aoi(solpos['apparent_zenith'], solpos['azimuth'])
poa = system.get_irradiance(solpos['apparent_zenith'], solpos['azimuth'],
                            cs['dni'], cs['ghi'], cs['dhi'])

# DC output
dc = system.pvwatts_dc(poa['poa_global'], temp_cell=25)

plt.plot(dc.index, dc.values, label="PV Power (W)")
plt.legend()
plt.title("PV Output (Sample Day - Enugu)")
plt.ylabel("Power (W)")
plt.show()

