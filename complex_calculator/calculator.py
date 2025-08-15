import math
import matplotlib.pyplot as plt

class Calculator:
    def __init__(self):
        self.history = []
    
    def create(self, real, imag):
        """Create a complex number"""
        return complex(real, imag)
    
    def show(self, z, label=""):
        """Show complex number in simple format"""
        if label:
            print(f"\n{label}:")
        print(f"  Form: {z}")
        print(f"  Real: {z.real}")
        print(f"  Imaginary: {z.imag}")
    
    def add(self, z1, z2):
        """Add two complex numbers"""
        result = z1 + z2
        self.history.append(f"({z1}) + ({z2}) = {result}")
        return result
    
    def subtract(self, z1, z2):
        """Subtract two complex numbers"""
        result = z1 - z2
        self.history.append(f"({z1}) - ({z2}) = {result}")
        return result
    
    def multiply(self, z1, z2):
        """Multiply two complex numbers"""
        result = z1 * z2
        self.history.append(f"({z1}) × ({z2}) = {result}")
        return result
    
    def divide(self, z1, z2):
        """Divide two complex numbers"""
        if z2 == 0:
            print("Error: Cannot divide by zero!")
            return None
        result = z1 / z2
        self.history.append(f"({z1}) ÷ ({z2}) = {result}")
        return result
    
    def plot_vectors(self, z1, z2, result, operation):
        """Simple plot of vectors on cartesian plane"""
        try:
            # Create figure
            plt.figure(figsize=(10, 8))
            
            # Plot origin
            plt.plot(0, 0, 'ko', markersize=8, label='Origin')
            
            # Plot vectors from origin
            plt.quiver(0, 0, z1.real, z1.imag, angles='xy', scale_units='xy', scale=1, 
                      color='blue', alpha=0.7, linewidth=2, label=f'z₁ = {z1}')
            plt.quiver(0, 0, z2.real, z2.imag, angles='xy', scale_units='xy', scale=1, 
                      color='red', alpha=0.7, linewidth=2, label=f'z₂ = {z2}')
            plt.quiver(0, 0, result.real, result.imag, angles='xy', scale_units='xy', scale=1, 
                      color='green', alpha=0.9, linewidth=3, label=f'Result = {result}')
            
            # Plot points
            plt.plot(z1.real, z1.imag, 'bo', markersize=10)
            plt.plot(z2.real, z2.imag, 'ro', markersize=10)
            plt.plot(result.real, result.imag, 'go', markersize=12)
            
            # Grid and axes
            plt.grid(True, alpha=0.3)
            plt.axhline(y=0, color='k', linewidth=0.5)
            plt.axvline(x=0, color='k', linewidth=0.5)
            
            # Labels
            plt.xlabel('Real Part')
            plt.ylabel('Imaginary Part')
            plt.title(f'Operation: {operation}')
            plt.legend()
            plt.axis('equal')
            
            # Show plot
            plt.tight_layout()
            plt.show()
            
            print("✅ Plot displayed successfully!")
            
        except Exception as e:
            print(f"❌ Could not display plot: {e}")
