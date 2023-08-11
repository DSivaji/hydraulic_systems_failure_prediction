# Hydraulic System Condition Monitoring Dataset

## Introduction

This repository contains the **Hydraulic System Condition Monitoring Dataset**, which was experimentally obtained using a hydraulic test rig. The test rig comprises a primary working circuit and a secondary cooling-filtration circuit connected through an oil tank [1], [2]. The data captures cyclically repeated constant load cycles with a duration of 60 seconds. Various process values, such as pressures, volume flows, and temperatures, are measured. Additionally, the condition of four hydraulic components—cooler, valve, pump, and accumulator—is quantitatively varied.

## Dataset Information

### Overview

The dataset consists of raw process sensor data, structured as matrices with rows representing cycles and columns representing data points within a cycle. The sensors involved in the data collection process are:

- PS1: Pressure (bar) - Sampled at 100 Hz
- PS2: Pressure (bar) - Sampled at 100 Hz
- PS3: Pressure (bar) - Sampled at 100 Hz
- PS4: Pressure (bar) - Sampled at 100 Hz
- PS5: Pressure (bar) - Sampled at 100 Hz
- PS6: Pressure (bar) - Sampled at 100 Hz
- EPS1: Motor power (W) - Sampled at 100 Hz
- FS1: Volume flow (l/min) - Sampled at 10 Hz
- FS2: Volume flow (l/min) - Sampled at 10 Hz
- TS1: Temperature (°C) - Sampled at 1 Hz
- TS2: Temperature (°C) - Sampled at 1 Hz
- TS3: Temperature (°C) - Sampled at 1 Hz
- TS4: Temperature (°C) - Sampled at 1 Hz
- VS1: Vibration (mm/s) - Sampled at 1 Hz
- CE: Cooling efficiency (virtual) (%) - Sampled at 1 Hz
- CP: Cooling power (virtual) (kW) - Sampled at 1 Hz
- SE: Efficiency factor (%) - Sampled at 1 Hz

### Target Conditions

The target condition values for each cycle are annotated in the 'profile.txt' file, where each row represents a cycle number. The columns represent:

1. Cooler Condition (%):
   - 3: Close to total failure
   - 20: Reduced efficiency
   - 100: Full efficiency

2. Valve Condition (%):
   - 100: Optimal switching behavior
   - 90: Small lag
   - 80: Severe lag
   - 73: Close to total failure

3. Internal Pump Leakage:
   - 0: No leakage
   - 1: Weak leakage
   - 2: Severe leakage

4. Hydraulic Accumulator (bar):
   - 130: Optimal pressure
   - 115: Slightly reduced pressure
   - 100: Severely reduced pressure
   - 90: Close to total failure

5. Stable Flag:
   - 0: Conditions were stable
   - 1: Static conditions might not have been reached yet

## Usage

You can use this dataset for various machine learning tasks, such as classification, regression, anomaly detection, and more. The raw sensor data and annotated target conditions provide a valuable resource for developing predictive maintenance and condition monitoring models for hydraulic systems.

## Citation

If you use this dataset in your work, please consider citing the original source:
https://archive.ics.uci.edu/dataset/447/condition+monitoring+of+hydraulic+systems#


## Acknowledgments

We acknowledge the creators and contributors of the **Hydraulic System Condition Monitoring Dataset** for their efforts in collecting and providing this valuable data.
