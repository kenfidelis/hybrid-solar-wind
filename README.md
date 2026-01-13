⚡ Hybrid Solar–Wind Energy Model for Nigeria (Python + Streamlit)
===============================================================

A reproducible Python implementation inspired by my MSc research on **hybrid PV-wind integration** and **grid load flow** analysis.  
This project models PV and wind generation, integrates them with a simplified grid network, and visualizes results in an interactive Streamlit dashboard.

**Tech:** Python • pvlib • windpowerlib • pandapower • Streamlit  
**Domain:** renewable integration • load flow • grid constraints • reliability-minded modelling  
📄 Case study: [docs/case-study.md](docs/case-study.md)

---

## Why this exists
Grid-integrated renewables require more than energy yield estimates — engineers need:
- generation profiles (PV + wind),
- system-level impacts (voltages, line loading, losses),
- and clear visualization for scenario comparison.

This repo demonstrates an end-to-end workflow for those studies using open-source Python tools.

---

## Architecture (high level)
```
Data (weather / assumptions / samples)
        ↓
PV Model (pvlib) ─────────┐
                          ├── Hybrid integration + Load Flow (pandapower) ──→ Results
Wind Model (windpowerlib) ┘
        ↓
Streamlit Dashboard (app.py) → Interactive plots + comparison views

---

## Features
✅ PV system modeling (pvlib)  
✅ Wind turbine modeling (windpowerlib)  
✅ Load flow & grid analysis (pandapower)  
✅ Hybrid PV + wind simulation (generation vs load)  
✅ Interactive Streamlit dashboard  

---

## Repo structure
hybrid-solar-wind/
├── app.py
├── dashboard/
├── samples/
├── run_pv.py
├── run_wind.py
├── run_hybrid.py
├── requirements.txt
└── LICENSE

---
Requirements
> Python 3.10+ (recommended)
> Tested on Linux/macOS (Windows should work with venv)

## 🚀 Quickstart (Run Locally)
1) Clone
git clone https://github.com/kenfidelis/hybrid-solar-wind.git
cd hybrid-solar-wind

2) Create a virtual environment + install dependencies
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

3) Run the Streamlit dashboard
streamlit run app.py

## 🧪 Run the simulation scripts (CLI)
PV-only simulation
python run_pv.py

Wind-only simulation
python run_wind.py

Hybrid PV + Wind simulation (grid + load flow)
python run_hybrid.py

Tip: start with the sample inputs in samples/ if any script asks for data/config paths.

## 📊 Outputs
Depending on the script you run, you should see:
- PV and wind power profiles
- Hybrid generation vs load comparison
- Load flow outputs (bus voltages, line loading, system losses)
- Interactive charts in the Streamlit dashboard

## Skills demonstrated
- Power system modelling concepts translated into reproducible Python code
- Modular simulation workflow (PV, wind, hybrid integration)
- Grid-impact analysis using pandapower (voltages, loading, losses)
- Communicating results through an interactive Streamlit dashboard

## 🗺️ Background

This work is based on my MSc research in renewable integration and power system analysis, translated into a reproducible Python workflow inspired by DIgSILENT PowerFactory studies.

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE)



