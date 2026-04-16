# 🚁 UAV Flight Envelope Calculator

![UAV Dashboard](UAV_Graphs.png)

## 📌 Project Overview
When UAVs scale to more complex missions (think high-flying surveillance or heavy payload deliveries), environmental issues can quickly become points of failure. It relies on the international standard atmoshere (ISA) mathematical model to instantly output, on a graphical user interface, flight envelopes ready for immediate use and carry out drone operations as tool written in Python.

It allows them to provide a target elevation, and immediately check the air density at that elevation for propeller lift, and if the ambient air is safe for LiPo operation.

## ⚙️ The Physics Engine
The core mathematical engine (`isa_engine.py`) programmatically implements atmospheric physics and thermodynamic laws (Ideal Gas Law, Tropospheric Temperature Lapse Rates) together to derive:
1. **Air Density:** So that the motor/rotor generates enough thrust.
2. **Temperature:** For battery drain risk mapping and freezing points.
3. **Barometric Pressure:** Used to calibrate altimeter and estimate aerodynamic drag.

## 🛠️ Technology Stack
* **Language:** Python
* **Data Processing:** `numpy` (for high-efficiency array generation of altitude envelopes)
* **Visualization:** `matplotlib` (to build professional-looking engineering dashboards, with multiple axis)

## 🚀 How to Run the Tool
1. Clone this repository to your local machine.
2. Ensure you have the required libraries installed (`pip install numpy matplotlib`).
3. Run the dashboard file from your terminal:
   ```bash
   python dashboard.py
4. Enter your planned UAV flight altitude when prompted to generate your custom mission map.

### 👨‍🔧About the Developer
Sajjad Mehdi *B.Sc. Aeronautics (Avionics) | Jamia Millia Islamia*

I am building a "Dual-Threat" engineering profile. My academic background gives me a deep, practical understanding of aircraft maintenance and systems (CAR 147/66). I build tools like this to bridge that hands-on maintenance knowledge with Core Aerospace Systems Design and autonomous software logic.

[Connect with me on LinkedIn)

(https://www.linkedin.com/in/sajjad-mehdi-naqvi/)
