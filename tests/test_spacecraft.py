import pytest
from entities.spacecraft import Spacecraft

@pytest.fixture
def spacecraft():
    return Spacecraft(name="Apollo", type="spacecraft", mass=5000, position=[0, 0], velocity=[0, 0], color=(255, 255, 255), radius=5, mission="Moon Landing")

def test_spacecraft_initialization(spacecraft):
    assert spacecraft.name == "Apollo"
    assert spacecraft.type == "spacecraft"
    assert spacecraft.mission == "Moon Landing"

def test_spacecraft_to_dict(spacecraft):
    spacecraft_dict = spacecraft.to_dict()
    assert spacecraft_dict["name"] == "Apollo"
    assert spacecraft_dict["mission"] == "Moon Landing"