import pytest
import numpy as np
from entities.celestial_body import CelestialBody

@pytest.fixture
def celestial_body():
    return CelestialBody(name="TestBody", type="planet", mass=5.972e24, position=[0, 0], velocity=[0, 0], color=(255, 255, 255), radius=6371000)

def test_celestial_body_initialization(celestial_body):
    assert celestial_body.name == "TestBody"
    assert celestial_body.type == "planet"
    assert celestial_body.mass == 5.972e24
    assert np.array_equal(celestial_body.position, np.array([0, 0], dtype=float))
    assert np.array_equal(celestial_body.velocity, np.array([0, 0], dtype=float))
    assert celestial_body.color == (255, 255, 255)
    assert celestial_body.radius == 6371000

def test_update_position(celestial_body):
    new_position = np.array([1000, 1000], dtype=float)
    celestial_body.update_position(new_position)
    assert np.array_equal(celestial_body.position, new_position)
    assert len(celestial_body.trajectory) == 1