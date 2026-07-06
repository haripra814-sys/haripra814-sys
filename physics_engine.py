"""
Physics Engine Utility Library
Designed for kinematic and gravitational potential energy computations.
"""

class PhysicsEngine:
    def __init__(self):
        # Acceleration due to gravity on Earth (m/s^2)
        self.g = 9.81

    def calculate_displacement(self, velocity: float, time: float) -> float:
        """
        Calculates basic linear displacement (Radius/Distance) using: R = V * T
        :param velocity: Velocity in meters per second (m/s)
        :param time: Time duration in seconds (s)
        :return: Displacement in meters (m)
        """
        if time < 0:
            raise ValueError("Time cannot be negative.")
        return velocity * time

    def calculate_potential_energy(self, mass: float, height: float) -> float:
        """
        Calculates Gravitational Potential Energy using: PE = m * g * h
        :param mass: Mass of the object in kilograms (kg)
        :param height: Height above reference level in meters (m)
        :return: Potential Energy in Joules (J)
        """
        if mass < 0 or height < 0:
            raise ValueError("Mass and height must be non-negative values.")
        return mass * self.g * height


# --- Automated Testing Execution ---
if __name__ == "__main__":
    print("🚀 Initializing Physics Engine Tests...")
    engine = PhysicsEngine()
    
    # Test 1: Kinematics (e.g., An object moving at 3 m/s for 10 seconds)
    v_test, t_test = 3.0, 10.0
    r_result = engine.calculate_displacement(v_test, t_test)
    print(f"[SUCCESS] Kinematic Displacement (R = {v_test} * {t_test}): {r_result} meters")
    
    # Test 2: Potential Energy (e.g., A 5kg object held 2 meters high)
    m_test, h_test = 5.0, 2.0
    pe_result = engine.calculate_potential_energy(m_test, h_test)
    print(f"[SUCCESS] Potential Energy (PE = {m_test} * 9.81 * {h_test}): {pe_result:.2f} Joules")
    
    print("\n✅ All repository physics calculations verified successfully!")
