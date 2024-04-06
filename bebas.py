import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Konstanta-konstanta Tata Surya
AU = 149.6e6  # Satuan Astronomi (dalam kilometer)
G = 6.674e-11  # Konstanta gravitasi (m^3/kg/s^2)

# Data planet (nama, massa (kg), jarak rata-rata dari Matahari (AU), kecepatan orbit (km/s))
planets = {
    'Mercury': (3.285e23, 0.39, 47.87),
    'Venus': (4.867e24, 0.72, 35.02),
    'Earth': (5.972e24, 1.0, 29.78),
    'Mars': (6.39e23, 1.52, 24.07),
    'Jupiter': (1.898e27, 5.2, 13.07),
    'Saturn': (5.683e26, 9.58, 9.69),
    'Uranus': (8.681e25, 19.18, 6.81),
    'Neptune': (1.024e26, 30.06, 5.43)
}


# Fungsi untuk menghitung percepatan gravitasi
def gravity_acceleration(mass, position):
    r = np.linalg.norm(position)
    return -G * mass / r**3 * position

# Fungsi untuk menghitung perubahan posisi dan kecepatan menggunakan metode Euler
def update_state(state, dt):
    position, velocity = state
    acceleration = sum(gravity_acceleration(m, position - np.array([distance * AU, 0, 0])) for (_, (m, distance, _)) in planets.items())
    new_position = position + velocity * dt
    new_velocity = velocity + acceleration * dt
    return new_position, new_velocity



# Waktu simulasi (dalam hari)
total_days = 365
dt = 0.1  # Interval waktu (dalam hari)

# Array untuk menyimpan posisi planet
positions = {planet: np.zeros((total_days, 3)) for planet in planets}

# Kondisi awal (posisi relatif terhadap Matahari)
initial_state = {planet: (np.array([distance * AU, 0, 0]), np.array([0, velocity * 1000, 0])) for planet, (_, distance, velocity) in planets.items()}

# Simulasi pergerakan planet
for i in range(total_days):
    for planet in planets:
        positions[planet][i] = initial_state[planet][0]
        initial_state[planet] = update_state(initial_state[planet], dt)

# Plot hasil simulasi
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Solar System Simulation')

for planet, (_, distance, _) in planets.items():
    ax.plot(positions[planet][:, 0], positions[planet][:, 1], positions[planet][:, 2], label=planet)

ax.set_xlabel('X (km)')
ax.set_ylabel('Y (km)')
ax.set_zlabel('Z (km)')
ax.legend()
plt.show()


