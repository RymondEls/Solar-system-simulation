import pytest
from entities.asteroid import Asteroid

@pytest.fixture
def asteroid():
    return Asteroid(name="Ceres", type="asteroid", mass=9.393e20, position=[4.14e11, 0], velocity=[0, 18000], color=(128, 128, 128), radius=470000, composition="Rocky-Ice")

def test_asteroid_initialization(asteroid):
    assert asteroid.name == "Ceres"
    assert asteroid.type == "asteroid"
    assert asteroid.composition == "Rocky-Ice"

def test_asteroid_to_dict(asteroid):
    asteroid_dict = asteroid.to_dict()
    assert asteroid_dict["name"] == "Ceres"
    assert asteroid_dict["composition"] == "Rocky-Ice"