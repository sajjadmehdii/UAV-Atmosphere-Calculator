# dashboard.py
# Interactive Data Visualization for UAV Operations

import numpy as np
import matplotlib.pyplot as plt
from isa_engine import calculate_isa

def generate_uav_dashboard():
    print("\n==========================================")
    print("  Interactive UAV Mission Dashboard  ")
    print("==========================================")

    # 1. ASK THE USER FOR INPUT
    user_input = input("Enter your planned UAV flight altitude in meters (e.g., 2500): ")
    
    try:
        drone_alt = float(user_input)
    except ValueError:
        print("Invalid number. Defaulting to 1000 meters.")
        drone_alt = 1000.0

    # Get the exact numbers for the user's specific drone altitude
    drone_temp, drone_press, drone_dens = calculate_isa(drone_alt)

    print(f"\nCalculating flight map for {drone_alt} meters. Please wait...")

    # 2. GENERATE THE MAP BACKGROUND
    altitudes = np.linspace(0, 5000, 500)
    temperatures = []
    densities = []
    pressures = [] # NEW: We added an empty list for Pressure!

    for alt in altitudes:
        temp, press, dens = calculate_isa(alt)
        temperatures.append(temp)
        densities.append(dens)
        pressures.append(press) # NEW: We are now saving the pressure data!

    # 3. DRAW THE DASHBOARD (Now with 3 columns instead of 2!)
    # Notice the (1, 3) below. It means 1 Row, 3 Columns.
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

    # --- GRAPH 1: Air Density ---
    ax1.plot(altitudes, densities, color='blue', linewidth=2)
    ax1.plot(drone_alt, drone_dens, marker='o', markersize=10, color='red', label=f'Drone ({drone_alt}m)')
    ax1.set_title('Lift: Air Density')
    ax1.set_xlabel('Altitude (meters)')
    ax1.set_ylabel('Air Density (kg/m^3)')
    ax1.grid(True, linestyle='--', alpha=0.7)
    ax1.legend()

    # --- GRAPH 2: Temperature ---
    celsius_temps = [t - 273.15 for t in temperatures]
    drone_temp_c = drone_temp - 273.15
    ax2.plot(altitudes, celsius_temps, color='red', linewidth=2)
    ax2.plot(drone_alt, drone_temp_c, marker='o', markersize=10, color='blue', label=f'Drone ({drone_alt}m)')
    ax2.set_title('Thermal: Temperature')
    ax2.set_xlabel('Altitude (meters)')
    ax2.set_ylabel('Temperature (°C)')
    ax2.grid(True, linestyle='--', alpha=0.7)
    ax2.axhline(0, color='black', linestyle=':', label='Freezing Point')
    ax2.legend()

    # --- GRAPH 3: Air Pressure (THE NEW GRAPH) ---
    # We divide by 1000 to turn Pascals (Pa) into kiloPascals (kPa) so the numbers look cleaner on the graph.
    kpa_pressures = [p / 1000 for p in pressures]
    drone_press_kpa = drone_press / 1000
    
    ax3.plot(altitudes, kpa_pressures, color='green', linewidth=2)
    ax3.plot(drone_alt, drone_press_kpa, marker='o', markersize=10, color='black', label=f'Drone ({drone_alt}m)')
    ax3.set_title('Barometric: Air Pressure')
    ax3.set_xlabel('Altitude (meters)')
    ax3.set_ylabel('Pressure (kPa)')
    ax3.grid(True, linestyle='--', alpha=0.7)
    ax3.legend()

    # Show the final product
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    generate_uav_dashboard()