import random
import math

class QuantumDNANanobot:
    def __init__(self, drug_payload):
        self.payload = drug_payload
        self.is_locked = True
        self.has_quantum_instructions = False
        self.teleportation_successful = False

    def receive_quantum_teleportation(self, donor_atom_state):
        """Simulates quantum teleportation. The state of a single atom outside the body 
        is instantly transferred to a receiver atom inside the nanobot's DNA structure.
        """
        print("\n--- Initiating Quantum Teleportation Protocol ---")
        if donor_atom_state == "ENCRYPTED_CANCER_DATA":
            self.has_quantum_instructions = True
            self.teleportation_successful = True
            print(">> SUCCESS: Quantum state transferred to nanobot atom instantly.")
            print(">> DNA logic updated: Bone marrow targeting instructions loaded.")
        else:
            self.teleportation_successful = False
            print(">> ERROR: Quantum entanglement decoherence. Teleportation failed.")

    def check_bone_marrow_cell(self, has_receptor_A, has_receptor_B):
        if not self.has_quantum_instructions:
            return "Bot Inactive: Waiting for quantum teleportation of DNA target instructions."

        if has_receptor_A and has_receptor_B:
            self.is_locked = False
            return self.release_payload()
        else:
            self.is_locked = True
            return "Scan Result: Normal bone marrow cell detected. Standing by."

    def release_payload(self):
        return f"TARGET MATCHED! Deploying {self.payload} directly inside the bone marrow tumor."


def calculate_stokes_drag(radius_nm, velocity_m_s=0.001):
    """Calculates fluid friction using Stokes' Law: F = 6 * pi * eta * r * v
    eta (fluid viscosity of bone marrow plasma) is roughly 0.002 Pa*s
    """
    eta = 0.002  
    radius_meters = radius_nm * 1e-9  # Convert nanometers to meters
    
    # Stokes' Law equation
    drag_force = 6 * math.pi * eta * radius_meters * velocity_m_s
    return drag_force


def calculate_quantum_simulation_fitness(nanobot_instance, size_nm, charge):
    """Evaluates nanobot efficiency by combining quantum data transfer 
    with classical fluid dynamics (Stokes' Law drag constraints).
    """
    if not nanobot_instance.teleportation_successful:
        return -100 # Maximum failure penalty
        
    print(">> Quantum Advantage: Zero travel delay. Instant target profile activation.")
    
    # Calculate physical drag force acting on the nanobot
    radius_nm = size_nm / 2
    drag = calculate_stokes_drag(radius_nm)
    
    # Mathematical Triage: Higher drag reduces the cells killed due to mobility loss
    # Ideal nanobot size window is 40nm - 60nm
    if 40 <= size_nm <= 60:
        base_efficiency = 95
    else:
        base_efficiency = 50
        
    # Scale efficiency down based on physical drag force metrics
    drag_penalty = drag * 1e11  # Scale scientific notation to whole numbers
    cancer_cells_killed = max(10, int(base_efficiency - drag_penalty))
    
    # Electrostatic safety check
    healthy_cells_damaged = 1 if charge == "Negative" else 20

    # Final fitness evaluation
    fitness_score = cancer_cells_killed - (healthy_cells_damaged * 2)
    return fitness_score, drag


# =====================================================================
# RUNNING THE UPGRADED QUANTUM NANOBOT SIMULATION
# =====================================================================

# 1. Initialize our Nanobot deep in the bone marrow environment
quantum_bot = QuantumDNANanobot(drug_payload="Quantum-Targeted-Anti-Leukemia-RNA")

# 2. Simulate beaming the target data via an entangled atom
outside_quantum_state = "ENCRYPTED_CANCER_DATA"
quantum_bot.receive_quantum_teleportation(outside_quantum_state)

# 3. Generate physical environment metrics
virtual_size = random.randint(30, 120) # Extends size range to test fluid limits
virtual_charge = random.choice(["Positive", "Negative"])

# 4. Run the physics-backed fitness evaluation
score, fluid_drag = calculate_quantum_simulation_fitness(quantum_bot, virtual_size, virtual_charge)

print("\n--- Telemetry Metrics & Fluid Analysis ---")
print(f"Nanobot Physical Attributes: Size = {virtual_size}nm, Charge = {virtual_charge}")
print(f"Calculated Stokes' Drag Force: {fluid_drag:.2e} Newtons")
print(f"Final Quantum Simulation Fitness Score: {score} points")