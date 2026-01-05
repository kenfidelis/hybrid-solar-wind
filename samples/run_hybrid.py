import pandas as pd
import pvlib
import matplotlib.pyplot as plt
import pandapower as pp

# --- Step 1: Define grid ---
net = pp.create_empty_network()

bus_hv = pp.create_bus(net, vn_kv=33.0, name="33kV Grid")
bus_lv = pp.create_bus(net, vn_kv=0.4, name="0.4kV Bus")

# Slack/grid connection (required)
pp.create_ext_grid(net, bus=bus_hv, vm_pu=1.0, name="Utility Grid")

# Transformer (keep 0.4 MVA and use a realistic LV load)
pp.create_transformer_from_parameters(
    net, hv_bus=bus_hv, lv_bus=bus_lv,
    sn_mva=0.4,
    vn_hv_kv=33.0, vn_lv_kv=0.4,
    vk_percent=6.0, vkr_percent=0.5,
    pfe_kw=1.0, i0_percent=0.1,
    name="33/0.4kV Transformer"
)

# --- Step 2: PV model (pvlib) ---
location = pvlib.location.Location(latitude=13.0, longitude=5.2, tz="Africa/Lagos")  # Sokoto
times = pd.date_range("2025-01-01", "2025-01-02", freq="1h", tz=location.tz)

cs = location.get_clearsky(times, model="ineichen")  # ghi/dni/dhi
solpos = location.get_solarposition(times)

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

# 50 kW PV example (W)
pdc0_w = 50_000
pv_power_w = pvlib.pvsystem.pvwatts_dc(
    g_poa_effective=poa["poa_global"],
    temp_cell=25,
    pdc0=pdc0_w,
    gamma_pdc=-0.004
)

t_idx = 12  # sample hour
pv_power_mw = float(pv_power_w.iloc[t_idx]) / 1e6  # MW
pp.create_sgen(net, bus=bus_lv, p_mw=pv_power_mw, q_mvar=0.0, name="PV Plant")

# --- Step 3: Wind model (simple) ---
wind_speed = 8.0  # m/s
air_density = 1.225
rotor_area = 2000.0  # m²
cp = 0.4
wind_power_mw = 0.5 * air_density * rotor_area * (wind_speed**3) * cp / 1e6  # MW
pp.create_sgen(net, bus=bus_lv, p_mw=wind_power_mw, q_mvar=0.0, name="Wind Farm")

# --- Step 4: Add Load (match transformer rating) ---
# 0.30 MW + 0.05 MVAr fits a 0.4 MVA transformer demo better than 20 MW
load_p_mw = 0.30
load_q_mvar = 0.05
pp.create_load(net, bus=bus_lv, p_mw=load_p_mw, q_mvar=load_q_mvar, name="Load")

# --- Step 5: Run Load Flow ---
pp.runpp(net)

print("=== Bus Results ===")
print(net.res_bus[["vm_pu", "va_degree"]])

print("\n=== Transformer Results ===")
print(net.res_trafo[["loading_percent", "p_hv_mw", "q_hv_mvar", "p_lv_mw", "q_lv_mvar"]])

# --- Visualization ---
plt.bar(["PV", "Wind", "Load"], [pv_power_mw, wind_power_mw, load_p_mw])
plt.ylabel("Power (MW)")
plt.title("Hybrid Solar-Wind System at Sokoto (Sample Hour)")
plt.show()
