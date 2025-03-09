# Smart Adaptive Streetlight System for Energy-Efficient Smart Cities 🚦💡

## Overview
This project simulates an intelligent street lighting system that dynamically adjusts brightness based on real-time vehicle movement. The system optimizes energy consumption, enhances road safety, and supports sustainable urban development.

## Features
- Real-Time Vehicle Detection – Tracks vehicle movement to adjust streetlight brightness.
- Adaptive Brightness Control – Lights brighten when vehicles are near and dim when roads are empty.
- Energy Optimization – Reduces unnecessary power usage, making cities more sustainable.
- Dashboard Monitoring – Displays live streetlight statuses and real-time energy consumption.

## Technology Stack
- on – Core programming language
- Pygame – Vehicle movement simulation
- Streamlit – Interactive dashboard for real-time monitoring
- Multithreading – Runs simulation and dashboard simultaneously

## Installation & Setup
1️. Clone the Repository
```bash
git clone https://github.com/YKD-1273/Smart-Adaptive-Streetlight-System-for-Energy-Efficient-Smart-Cities.git
cd Smart-Adaptive-Streetlight-System-for-Energy-Efficient-Smart-Cities
```
2. Install Dependencies
```bash
pip install pygame streamlit
```
3. Run the Project
- Start the Streamlit Dashboard (which launches the simulation):
  ```bash
  python -m streamlit run dashboard.py
  ```

## How It Works

1. Click "Start Simulation" on the dashboard.
2. The Pygame simulation starts, showing vehicles moving on the road.
3. Streetlights adjust brightness dynamically based on vehicle proximity.
4. The dashboard updates in real-time, showing:
5. Each streetlight’s ON/OFF status
6. Energy consumption values

## Future Improvements
- Integrate real-world traffic data using AI models.
- Add machine learning for smarter energy predictions.
- Simulate pedestrian detection for enhanced streetlight control.
