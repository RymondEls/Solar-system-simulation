import pytest
import numpy as np
from utils.physics import compute_acceleration, rk4_step
from entities.celestial_body import CelestialBody

@pytest.fixture
def bodies():
    sun = CelestialBody(name="Sun", type="star", mass=1.989e30, position=[0, 0], velocity=[0, 0], color=(255, 255, 0), radius=6.957e8)
    earth = CelestialBody(name="Earth", type="planet", mass=5.972e24, position=[1.496e11, 0], velocity=[0, 29780], color=(0, 0, 255), radius=6.371e6)
    return [sun, earth]

def test_compute_acceleration(bodies):
    acceleration = compute_acceleration(bodies, 1)  # Ускорение Земли
    assert isinstance(acceleration, np.ndarray)
    assert acceleration.shape == (2,)

def test_rk4_step(bodies):
    initial_position = bodies[1].position.copy()
    rk4_step(bodies, 3600)  # Шаг в 1 час
    assert not np.array_equal(bodies[1].position, initial_position)