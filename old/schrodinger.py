import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Constants
h_bar = 1  # Planck's constant (for simplicity, set to 1)
A0 = 1     # Amplitude of the wave function
E = 1      # Energy of the particle
p = 1      # Momentum of the particle

# Define the wave function
def wave_function(x, t):
    exponent = -1j / h_bar * (E * t - p * x)
    return A0 * np.exp(exponent)

# Create a grid for x, t, and y (real and imaginary parts)
x = np.linspace(-5, 5, 100)   # Range for x-axis (-5 to 5), 100 points
t = np.linspace(0, 10, 100)   # Range for t-axis (0 to 10), 100 points

X, T = np.meshgrid(x, t)  # Create meshgrid for x and t

# Initialize figure and axis for 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Function to update the 3D plot for each frame of the animation
def update(frame):
    ax.clear()
    wave_at_position = wave_function(X, T[frame])
    real_part = np.real(wave_at_position)
    imag_part = np.imag(wave_at_position)
    ax.plot_surface(X, T, real_part, cmap='viridis', alpha=0.7)
    ax.plot_surface(X, T, imag_part, cmap='plasma', alpha=0.7)
    ax.set_title(f'Evolution of Wave Function in 3D (t={t[frame]:.2f})')
    ax.set_xlabel('Position (x)')
    ax.set_ylabel('Time (t)')
    ax.set_zlabel('Amplitude')
    ax.legend(['Real part', 'Imaginary part'])
    ax.view_init(elev=20, azim=30)  # Adjust viewing angle

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(t), interval=100, blit=False)

plt.show()
