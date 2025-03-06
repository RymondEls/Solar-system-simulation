import pytest
from entities.planet import Planet
from operations.surface_study import study_surface

@pytest.fixture
def planet_with_surface():
    return Planet(name="Earth", type="planet", mass=5.972e24, position=[0, 0], velocity=[0, 0], color=(0, 0, 255), radius=6371000, atmosphere="Nitrogen-Oxygen", surface="Rocky")

def test_study_surface(capsys, planet_with_surface):
    study_surface(planet_with_surface)
    captured = capsys.readouterr()
    assert "Изучение поверхности Earth: Rocky" in captured.out