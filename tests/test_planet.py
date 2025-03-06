import pytest
from entities.planet import Planet

@pytest.fixture
def planet():
    return Planet(name="Earth", type="planet", mass=5.972e24, position=[0, 0], velocity=[0, 0], color=(0, 0, 255), radius=6371000, atmosphere="Nitrogen-Oxygen", surface="Rocky")

def test_planet_initialization(planet):
    assert planet.name == "Earth"
    assert planet.type == "planet"
    assert planet.atmosphere == "Nitrogen-Oxygen"
    assert planet.surface == "Rocky"

def test_planet_to_dict(planet):
    planet_dict = planet.to_dict()
    assert planet_dict["name"] == "Earth"
    assert planet_dict["atmosphere"] == "Nitrogen-Oxygen"
    assert planet_dict["surface"] == "Rocky"