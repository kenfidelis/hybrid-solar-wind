# Case Study: Hybrid Solar–Wind Grid Integration Model (Nigeria)

## Context
This project is a reproducible Python implementation inspired by my MSc research on integrating hybrid PV–wind generation into a power network context. The goal is to model generation profiles, integrate them with a simplified grid, and evaluate grid-impact indicators such as bus voltages, line loading, and system losses.

## Problem
Renewable integration studies often become hard to reproduce: assumptions are spread across spreadsheets, models live in proprietary tools, and results are difficult to communicate. I wanted a workflow that is:
- reproducible (one repo, pinned dependencies),
- modular (PV, wind, hybrid modules),
- easy to explain (dashboard + clear outputs).

## Approach
- **PV modelling:** pvlib to generate PV power profiles based on [inputs/weather assumptions].
- **Wind modelling:** windpowerlib to model turbine output based on [assumptions].
- **Grid analysis:** pandapower to run load flow and compute grid-impact metrics.
- **Visualization:** Streamlit dashboard to compare scenarios and present results.

## Key outputs
- PV and wind generation profiles (time series)
- Hybrid generation vs load comparison
- Load flow results: bus voltages, line loading, losses
- Interactive dashboard views to explore scenarios

## Engineering decisions (what I optimized for)
- **Clarity over complexity:** kept the grid model simplified and focused on demonstrating the workflow end-to-end.
- **Modularity:** separate scripts for PV, wind, and hybrid integration to support testing and future extensions.
- **Reproducibility:** requirements pinned for consistent environments.

## How this maps to roles (what this project demonstrates)
- **Energy / Power Systems:** renewable integration, load flow concepts, communicating grid impacts.
- **OT/ICS Security:** understanding of SCADA-monitored systems and reliability constraints in critical infrastructure.
- **Platform/DevSecOps:** building reproducible workflows, dependency management, and a deployable dashboard-style application.

## Next improvements
- Add CI checks (lint/test) via GitHub Actions
- Add containerized run (Docker) for one-command startup
- Add scenario configuration via a YAML/JSON input layer
- Add basic validation tests for inputs and model outputs

## Links
- Repo: https://github.com/kenfidelis/hybrid-solar-wind
- MSc thesis (Zenodo): https://doi.org/10.5281/zenodo.16934221
