import random
import math

class QuantumDNANanobot:
    def __init__(self, drug_payload):
        self.payload = drug_payload
        self.healthy_marker = "CD34"       # Healthy stem cell marker
        self.cancer_marker = "CD19_MUTANT"  # Target leukemia marker
        self.has_quantum_instructions = False
        self.teleportation_successful = False

    def receive_quantum_teleportation(self, donor_atom_state):
        """Simulates instantaneous quantum state transfer to program the DNA logic."""
        print("\n--- Initiating Quantum Teleportation Protocol ---")
        if donor_atom_state == "ENCRYPTED_CANCER_DATA":
            self.has_quantum_instructions = True
            self.teleportation_successful = True
            print(">> SUCCESS: Quantum state transferred to nanobot atom instantly.")
            print(">> DNA logic updated: Bone marrow targeting instructions loaded.")
        else:
            self.teleportation_successful = False
            print(">> ERROR: Quantum entanglement decoherence. Teleportation failed.")

    def scan_cell_surface(self, cell_proteins):
        """Executes a multi-antigen AND-NOT logic gate to protect healthy tissue."""
        if not self.has_quantum_instructions:
            return "Bot Inactive: Waiting for quantum teleportation of DNA target instructions."

        print(f"\n[Scanning Cell] Detected Surface Proteins: {cell_proteins}")
        
        has_cancer_sig = self.cancer_marker in cell_proteins
        has_healthy_sig = self.healthy_marker in cell_proteins
        
        # Multi-antigen gate verification
        if has_cancer_sig and not has_healthy_sig:
            return self.trigger_attack()
        elif has_healthy_sig:
            return "-> RESULT: Protective CD34+ marker verified. System override: Standing down."
        else:
            return "-> RESULT: Baseline cell detected. No actionable signatures. Continuing sweep."

    def trigger_attack(self):
        return f"-> ALERT: TARGET MATCHED! Deploying {self.payload} directly inside tumor."


def calculate_stokes_drag(radius_nm, velocity_m_s=0.001):
    """Calculates fluid friction in bone marrow plasma using Stokes' Law."""
    eta = 0.002  # Fluid viscosity
    radius_meters = radius_nm * 1e-9 
    return 6 * math.pi * eta * radius_meters * velocity_m_s


def calculate_quantum_simulation_fitness(nanobot_instance, size_nm, charge):
    """Evaluates systemic efficiency based on physics and environmental drag constraints."""
    if not nanobot_instance.teleportation_successful:
        return -100 
        
    print(">> Quantum Advantage: Zero travel delay. Instant target profile activation.")
    
    radius_nm = size_nm / 2
    drag = calculate_stokes_drag(radius_nm)
    
    if 40 <= size_nm <= 60:
        base_efficiency = 95
    else:
        base_efficiency = 50
        
    drag_penalty = drag * 1e11  
    cancer_cells_killed = max(10, int(base_efficiency - drag_penalty))
    healthy_cells_damaged = 1 if charge == "Negative" else 20

    fitness_score = cancer_cells_killed - (healthy_cells_damaged * 2)
    return fitness_score, drag


# =====================================================================
# RUNNING THE UNIFIED BIO-PHYSICS SIMULATION
# =====================================================================
if __name__ == "__main__":
    # 1. Initialize System
    quantum_bot = QuantumDNANanobot(drug_payload="Quantum-Targeted-Anti-Leukemia-RNA")

    # 2. Verify lockdown state before teleportation
    print(quantum_bot.scan_cell_surface(["CD19_MUTANT"]))

    # 3. Beam target data via quantum entanglement
    quantum_bot.receive_quantum_teleportation("ENCRYPTED_CANCER_DATA")

    # 4. Execute cellular scanning logic gates
    healthy_test = ["CD34", "HLA-DR", "CD38"]
    cancer_test = ["CD19_MUTANT", "CD22", "CD38"]
    
    print(quantum_bot.scan_cell_surface(healthy_test))
    print(quantum_bot.scan_cell_surface(cancer_test))

    # 5. Run kinetic efficiency analysis
    virtual_size = random.randint(30, 120)
    virtual_charge = random.choice(["Positive", "Negative"])
    score, fluid_drag = calculate_quantum_simulation_fitness(quantum_bot, virtual_size, virtual_charge)

    print("\n--- Physical Telemetry & Fluid Analysis ---")
    print(f"Nanobot Size = {virtual_size}nm | Charge = {virtual_charge}")
    print(f"Calculated Stokes' Drag Force: {fluid_drag:.2e} Newtons")
    print(f"Final System Fitness Score: {score} points")