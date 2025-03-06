import pytest
from entities.planet import Planet
from operations.atmosphere_study import study_atmosphere

@pytest.fixture
def planet_with_atmosphere():
    return Planet(name="Earth", type="planet", mass=5.972e24, position=[0, 0], velocity=[0, 0], color=(0, 0, 255), radius=6371000, atmosphere="Nitrogen-Oxygen", surface="Rocky")

def test_study_atmosphere(capsys, planet_with_atmosphere):
    study_atmosphere(planet_with_atmosphere)
    captured = capsys.readouterr()
    assert "Изучение атмосферы Earth: Nitrogen-Oxygen" in captured.out