import pandas as pd
import pvlib
import numpy as np
import matplotlib.pyplot as plt
import pandapower as pp

# --- Step 1: Define grid ---
net = pp.create_empty_network()
bus1 = pp.create_bus(net, vn_kv=33)   # Medium voltage
bus2 = pp.create_bus(net, vn_kv=0.4)  # Low voltage

pp.create_transformer_from_parameters(net, hv_bus=bus1, lv_bus=bus2, sn_mva=0.4,
                                      vn_hv_kv=33, vn_lv_kv=0.4,
                                      vk_percent=6, vkr_percent=0.5,
                                      pfe_kw=1.0, i0_percent=0.1)

# --- Step 2: PV model (using pvlib) ---
location = pvlib.location.Location(latitude=13.0, longitude=5.2, tz='Africa/Lagos')  # Sokoto
times = pd.date_range('2025-01-01', '2025-01-02', freq='1h', tz=location.tz)
cs = location.get_clearsky(times)

system = pvlib.pvsystem.PVSystem(surface_tilt=30, surface_azimuth=180,
                                  module_parameters={'pdc0': 50000, 'gamma_pdc': -0.004},
                                  inverter_parameters={'pdc0': 50000})

poa = system.get_irradiance(solpos=location.get_solarposition(times)['apparent_zenith'],
                            azimuth=location.get_solarposition(times)['azimuth'],
                            dni=cs['dni'], ghi=cs['ghi'], dhi=cs['dhi'])

pv_power = system.pvwatts_dc(poa['poa_global'], temp_cell=25) / 1000  # MW

# Take one value for load flow
pp.create_sgen(net, bus=bus2, p_mw=pv_power.iloc[12], name="PV Plant")

# --- Step 3: Wind model (simple) ---
wind_speed = 8  # m/s (Sokoto avg)
air_density = 1.225
rotor_area = 2000  # m²
cp = 0.4
wind_power = 0.5 * air_density * rotor_area * (wind_speed**3) * cp / 1e6  # MW

pp.create_sgen(net, bus=bus2, p_mw=wind_power, name="Wind Farm")

# --- Step 4: Add Load ---
pp.create_load(net, bus=bus2, p_mw=20, q_mvar=5)

# --- Step 5: Run Load Flow ---
pp.runpp(net)

print(net.res_bus)
print(net.res_line)

# --- Visualization ---
plt.bar(["PV", "Wind", "Load"], [pv_power.iloc[12], wind_power, 20])
plt.ylabel("Power (MW)")
plt.title("Hybrid Solar-Wind System at Sokoto (Sample Hour)")
plt.show()
