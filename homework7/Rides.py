import numpy as np

# Constants

def calculate_speed(height_initial, height_final):
    # Calculate the speed based on change in height using conservation of energy.
    # change in potential energy and resulting kinetic energy
    delta_h = height_initial - height_final
    speed = np.sqrt(2 * 9.8 * delta_h)  # KE = PE change
    return max(speed, 0)  # Speed is positive

def check_status(speed):
    """
    Determine the status of the ride based on speed.
    Parameters:
        speed (float): current speed of the ride (m/s)
    Returns:
        str: 'Wooooo!', 'okay', or 'oops' based on its speeds
    """
    if speed > 10:
        return "Wooooo!"
    elif speed > 0:
        return "okay"
    else:
        return "oops"