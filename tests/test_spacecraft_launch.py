import pytest
from operations.spacecraft_launch import launch_spacecraft
from entities.spacecraft import Spacecraft

def test_launch_spacecraft():
    bodies = []
    launch_spacecraft(bodies, "Apollo", 5000, [0, 0], [0, 0], "Moon Landing")
    assert len(bodies) == 1
    assert bodies[0].name == "Apollo"
    assert bodies[0].mission == "Moon Landing"