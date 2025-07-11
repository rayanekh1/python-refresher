import numpy as np
import math
import unittest


# prob 1
def calc_buoyancy(vol, fluid_density):
    """returns buoyant force on obj w/ vol & fluid dens.
    water"""
    if vol <= 0 or fluid_density <= 0:
        raise ValueError("Must be +")
    return 9.81 * vol * fluid_density


# prob 2
"""check if float in h2o
(density < 1000 means float)"""


def will_float(vol, mass):
    if vol <= 0 or mass <= 0:
        raise ValueError("Must be +")
    return (mass / vol) < 1000


# prob 3
def water_pressure(depth):
    """depth in meters + return water pressure
    (no atm)"""
    if depth < 0:
        raise ValueError("can't do negative")
    return 9.81 * 1000 * depth


# prob 4
def lin_accel(force, mass):
    """newton's 2nd law it returns linear accel
    mass != 0"""
    if mass <= 0:
        raise ValueError("mass needs to be > 0")
    return force / mass


# prob 5
def ang_accel(tau, inertia):
    """returns angular acceleration
    inertia != 0"""
    if inertia == 0:
        raise ValueError("inertia != 0")
    return tau / inertia


# prob 6
def torque_calc(F, angle_deg, dist):
    """finds torque from force, distance from axis,
    and angle of application"""
    rad = math.radians(angle_deg)
    torque = F * dist * math.sin(rad)
    return torque


# prob 7
def moment_inertia(m, r):
    """returns the moment of inertia
    for a point mass at a radius"""
    I = m * (r**2)
    return I


# prob 8
def auv_accel_2D(force, angle_rad, mass=100, volume=0.1, thruster_distance=0.5):
    """split force into x and y parts to find acceleration in 2D for AUV
    45 degree angle force (gives accel)
    """
    if angle_rad > math.pi / 6 or angle_rad < -math.pi / 6:
        raise ValueError("angle not in range")
    fx = force * math.cos(angle_rad)
    fy = -1 * force * math.sin(angle_rad)
    ax = fx / mass
    ay = fy / mass
    return ax, ay


def auv_ang_accel(force, angle_rad, inertia=1, dist=0.5):
    """calculate angular accel from torque (force × cos × dist)"""
    return (force * math.cos(angle_rad) * dist) / inertia


# prob 9
def accel_auv4(T, alpha, theta, mass=100):
    """calc accel (x,y) of 4 thrusters
    use rotation matrix and direction matrix to do in body and world frame
    """
    if len(T) != 4:
        raise ValueError("need 4 thrusters")

    R = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])

    dir_matrix = np.array(
        [
            [np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],
            [np.sin(alpha), -np.sin(alpha), -np.sin(alpha), np.sin(alpha)],
        ]
    )
    combo = np.matmul(R, np.matmul(dir_matrix, T))
    return combo / mass


def ang_accel_auv4(T, alpha, L, l, inertia=100):
    """returns angular acceleration of an AUV from
    thrusts and geometry"""
    signs = np.array([1, -1, 1, -1])
    torque = np.sum(signs * T * (L * np.sin(alpha) + l * np.cos(alpha)))
    return torque / inertia


# prob 10
def simulate_auv(
    T, alpha, L, l, mass=100, inertia=100, dt=0.1, t_final=10, x0=0, y0=0, theta0=0
):
    """simulate movement in 2D + rotation, output positions and states"""
    T = np.array(T)
    steps = int(t_final / dt)
    t = np.linspace(0, t_final, steps)
    x = np.zeros_like(t)
    y = np.zeros_like(t)
    theta = np.zeros_like(t)
    v = np.zeros_like(t)
    omega = np.zeros_like(t)
    a = np.zeros_like(t)

    x[0] = x0
    y[0] = y0
    theta[0] = theta0
    angular_a = ang_accel_auv4(T, alpha, L, l, inertia)

    for i in range(1, len(t)):
        theta[i] = theta[i - 1] + omega[i - 1] * dt
        omega[i] = omega[i - 1] + angular_a * dt
        ax, ay = accel_auv4(T, alpha, theta[i], mass)
        a[i] = np.sqrt(ax**2 + ay**2)
        v[i] = v[i - 1] + a[i] * dt
        x[i] = x[i - 1] + v[i] * dt * np.cos(theta[i])
        y[i] = y[i - 1] + v[i] * dt * np.sin(theta[i])

    return t, x, y, theta, v, omega, a


# testing
class TestPhysics(unittest.TestCase):

    def test_buoyancy(self):
        self.assertAlmostEqual(calc_buoyancy(0.2, 1000), 1962)

    def test_will_float(self):
        self.assertTrue(will_float(1.0, 500))
        self.assertFalse(will_float(0.5, 600))

    def test_pressure(self):
        self.assertEqual(water_pressure(10), 98100)

    def test_accel(self):
        self.assertAlmostEqual(lin_accel(20, 2), 10)

    def test_ang_accel(self):
        self.assertAlmostEqual(ang_accel(10, 5), 2)

    def test_torque(self):
        self.assertAlmostEqual(torque_calc(10, 90, 2), 20, places=1)

    def test_moi(self):
        self.assertEqual(moment_inertia(2, 3), 18)

    def test_auv_accel(self):
        ax, ay = auv_accel_2D(100, 0)
        self.assertAlmostEqual(ax, 1.0)
        self.assertAlmostEqual(ay, 0.0, places=3)

    def test_auv_ang(self):
        self.assertAlmostEqual(auv_ang_accel(100, 0), 50)

    def test_simulate_output_shape(self):
        T = np.array([10, 10, 10, 10])
        result = simulate_auv(T, 0, 2, 1)
        self.assertEqual(len(result), 7)
        self.assertEqual(len(result[0]), 100)


if __name__ == "__main__":
    unittest.main()
