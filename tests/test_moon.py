import pytest
from entities.moon import Moon

@pytest.fixture
def moon():
    return Moon(name="Moon", type="moon", mass=7.342e22, position=[384400000, 0], velocity=[0, 1022], color=(128, 128, 128), radius=1737000, parent_planet="Earth")

def test_moon_initialization(moon):
    assert moon.name == "Moon"
    assert moon.type == "moon"
    assert moon.parent_planet == "Earth"

def test_moon_to_dict(moon):
    moon_dict = moon.to_dict()
    assert moon_dict["name"] == "Moon"
    assert moon_dict["parent_planet"] == "Earth"