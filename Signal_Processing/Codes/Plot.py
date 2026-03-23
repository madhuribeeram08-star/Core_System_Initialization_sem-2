import matplotlib
matplotlib.use('Agg')  # Required for Termux/Debian
import matplotlib.pyplot as plt
import control as ctrl
import numpy as np

# Define T(s) = (s - 5) / (s^2 + 5s + 6)
num = [1, -5]
den = [1, 5, 6]
sys = ctrl.TransferFunction(num, den)

# Extract poles and zeros for manual labeling
poles = ctrl.poles(sys)
zeros = ctrl.zeros(sys)

plt.figure(figsize=(10, 7))

# Generate the PZ map using the control library
# This handles the 'x' and 'o' markers automatically
ctrl.pole_zero_plot(sys, plot=True, title='Pole-Zero Map with Labels')

# Manually add labels and colors to make it clear
# Plot Poles (Red X)
for p in poles:
    plt.plot(p.real, p.imag, 'rx', markersize=10, mew=2)
    plt.text(p.real, p.imag + 0.1, f' Pole: {p.real:.1f}', 
             color='red', fontweight='bold', ha='center')

# Plot Zeros (Blue o)
for z in zeros:
    plt.plot(z.real, z.imag, 'bo', markersize=10, fillstyle='none', mew=2)
    plt.text(z.real, z.imag + 0.1, f' Zero: {z.real:.1f}', 
             color='blue', fontweight='bold', ha='center')

# Highlight the Right Half Plane (The "Non-Minimum Phase" zone)
plt.axvspan(0, max(zeros.real) + 2, color='yellow', alpha=0.1)
if any(z.real > 0 for z in zeros):
    plt.text(2.5, -0.5, "NON-MINIMUM PHASE\n(Zero in RHP)", 
             bbox=dict(facecolor='white', alpha=0.8), ha='center', color='darkred')

# Final Touches
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.axvline(0, color='black', linewidth=1.5)
plt.axhline(0, color='black', linewidth=1.5)
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')

# Save and Notify
plt.savefig('labeled_system_plot.png')
print("Successfully generated 'labeled_system_plot.png'")