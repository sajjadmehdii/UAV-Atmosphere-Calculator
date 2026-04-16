# isa_engine.py
# Core Mathematical Engine for the International Standard Atmosphere

import math

def calculate_isa(altitude):
    """
    Takes an altitude in meters and returns Temperature (K), Pressure (Pa), and Density (kg/m^3).
    """
    
    # 1. THE BASELINE CONSTANTS (Sea Level)
    T0 = 288.15        # Base Temperature in Kelvin (15 C)
    P0 = 101325.0      # Base Pressure in Pascals (The full stack of blankets)
    g = 9.80665        # Gravity (m/s^2)
    R = 287.05         # Gas Constant for Air 
    lapse_rate = -0.0065 # How fast it gets cold per meter (The campfire rule)

    # Variables we will calculate
    temperature = 0.0
    pressure = 0.0

    # 2. THE LOGIC BRANCH (Asking where the drone is)
    if altitude <= 11000:
        # ZONE 1: The Troposphere (0 to 11,000 meters) - Where UAVs fly!
        
        # Calculate new Temperature (Campfire gets further away)
        temperature = T0 + (lapse_rate * altitude)
        
        # Calculate new Pressure (Fewer blankets pushing down)
        # Formula: P = P0 * (T / T0)^(-g / (lapse_rate * R))
        power_factor = -g / (lapse_rate * R)
        pressure = P0 * math.pow((temperature / T0), power_factor)

    elif altitude <= 20000:
        # ZONE 2: The Tropopause (11,000 to 20,000 meters) - Too high for drones
        
        # The temperature stops dropping here, it stays perfectly frozen
        temperature = 216.65 
        
        # The pressure at exactly 11,000 meters (our new starting point for this zone)
        P11 = 22632.1 
        
        # Calculate new Pressure using exponential decay
        # Formula: P = P11 * e^(-g * (h - 11000) / (R * T))
        pressure = P11 * math.exp(-g * (altitude - 11000) / (R * temperature))
        
    else:
        print("Warning: Altitude too high for this basic drone calculator!")
        return None, None, None

    # 3. THE UNIVERSAL RULE (Calculating Air Density)
    # Density = Pressure / (Gas Constant * Temperature)
    # This is the "Packing Rule" - how thick the air is for the propellers!
    density = pressure / (R * temperature)

    # 4. HAND THE NUMBERS BACK
    return temperature, pressure, density


# --- INTERACTIVE TERMINAL TOOL ---
if __name__ == "__main__":
    print("==========================================")
    print("  UAV Standard Atmosphere Calculator  ")
    print("==========================================")
    print("Type 'q' at any time to quit the program.")

    # The 'while True' loop keeps the program running until you type 'q'
    while True:
        # Ask the user for input
        user_input = input("\nEnter altitude in meters: ")

        # Check if the user wants to quit
        if user_input.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break

        # The 'try' block acts as a safety net in case the user types letters instead of numbers
        try:
            # Convert the text the user typed into a decimal number (float)
            test_altitude = float(user_input)
            
            # Send the altitude to our engine
            temp, press, dens = calculate_isa(test_altitude)
            
            # If the engine successfully calculated the numbers, print them
            if temp is not None:
                print(f"--- Atmospheric Conditions at {test_altitude} m ---")
                print(f"  Temperature: {temp:.2f} Kelvin")
                print(f"  Pressure:    {press:.2f} Pascals")
                print(f"  Air Density: {dens:.4f} kg/m^3")
                
        except ValueError:
            # If they typed words instead of numbers, catch the error and warn them nicely
            print("Error: Invalid input. Please enter a number (e.g., 2500) or 'q' to quit.")