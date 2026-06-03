import random

class QuantumSimulator:
    """Simulates basic quantum gate operations and state collapses using statistical matrices."""
    
    def __init__(self):
        # Base state: |0> represents 100% probability of collapsing to 0
        self.state_alpha = 1.0  # Amplitude for state 0
        self.state_beta = 0.0   # Amplitude for state 1

    def apply_hadamard_gate(self):
        """Places the qubit into a theoretical superposition state.
        The mathematical probability for either state becomes exactly 0.50 (50%).
        """
        # In a real quantum system, amplitudes become 1/sqrt(2).
        # We simulate the resulting equal probability state here.
        self.state_alpha = 0.7071
        self.state_beta = 0.7071

    def measure_qubit(self) -> int:
        """Collapses the wave function. The superposition state is destroyed,
        forcing the qubit into a deterministic 0 or 1.
        """
        # Calculate probabilities based on the square of the amplitudes
        prob_zero = round(self.state_alpha ** 2, 2)
        
        # Generate a random float between 0.0 and 1.0 to simulate measurement
        if random.random() < prob_zero:
            return 0
        return 1

    def run_simulation_batch(self, total_trials: int) -> dict:
        """Executes a sequential batch of quantum flips to audit statistical distribution."""
        results = {0: 0, 1: 0}
        
        for _ in range(total_trials):
            # Reset state to |0>
            self.__init__()
            # Pass through the gate to induce superposition
            self.apply_hadamard_gate()
            # Collapse the state and record the metric
            measurement = self.measure_qubit()
            results[measurement] += 1
            
        return results

# --- Execution & Telemetry Logging ---
if __name__ == "__main__":
    trials = 10000
    sim = QuantumSimulator()
    
    print(f"--- Initializing Quantum Gate Simulation: {trials,:,} Trials ---")
    raw_data = sim.run_simulation_batch(trials)
    
    # Calculate empirical percentages
    pct_zero = (raw_data[0] / trials) * 100
    pct_one = (raw_data[1] / trials) * 100
    
    print(f"Resulting State Space Distribution:")
    print(f" -> State |0>: {raw_data[0]} counts ({pct_zero:.2f}%)")
    print(f" -> State |1>: {raw_data[1]} counts ({pct_one:.2f}%)")
    print(f"System Divergence from Theoretical Ideal: {abs(50.0 - pct_zero):.2f}%")