# ⚡ Hybrid Solar-Wind Energy Model for Nigeria

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-green.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This repository provides a **Python-based equivalent** of my MSc thesis originally modeled in DIgSILENT PowerFactory:

> *Modelling and Simulation of Hybrid Wind and Photovoltaic Connected System to Nigeria Power Network*

It demonstrates how **PV and Wind systems** can be modeled in Python, integrated into the Nigerian grid, and visualized interactively.

---

## ✨ Features
- ✅ **PV system modeling** using [pvlib](https://pvlib-python.readthedocs.io/)
- ✅ **Wind turbine modeling** using [windpowerlib](https://windpowerlib.readthedocs.io/)
- ✅ **Load flow & grid analysis** with [pandapower](https://www.pandapower.org/)
- ✅ **Hybrid system simulation** (PV + Wind + Load)
- ✅ **Interactive dashboard** with [Streamlit](https://streamlit.io)

---

**Tech:** Python • pvlib • windpowerlib • pandapower • Streamlit

## 📂 Repository Structure
```text
hybrid-solar-wind/
├── app.py                # Streamlit dashboard entrypoint
├── dashboard/            # Dashboard components/assets (plots, UI helpers, etc.)
├── samples/              # Sample input data / config files
├── run_pv.py             # PV modelling workflow (pvlib)
├── run_wind.py           # Wind modelling workflow (windpowerlib)
├── run_hybrid.py         # Hybrid integration + pandapower load flow
├── requirements.txt
├── README.md
└── LICENSE

🚀 Quickstart (Run Locally)
1) Clone
git clone https://github.com/kenfidelis/hybrid-solar-wind.git
cd hybrid-solar-wind

2) Create a virtual environment + install dependencies
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

3) Run the Streamlit dashboard
streamlit run app.py

🧪 Run the simulation scripts (CLI)
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

## 🗺️ Background

This work is based on my MSc research in renewable integration and power system analysis, translated into a reproducible Python workflow inspired by DIgSILENT PowerFactory studies.

📜 License

This project is licensed under the MIT License — see the [LICENSE](https://github.com/kenfidelis/hybrid-solar-wind/blob/main/LICENSE)





