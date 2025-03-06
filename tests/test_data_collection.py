import pytest
from entities.planet import Planet
from operations.data_collection import collect_data

@pytest.fixture
def planet():
    return Planet(name="Earth", type="planet", mass=5.972e24, position=[0, 0], velocity=[0, 0], color=(0, 0, 255), radius=6371000, atmosphere="Nitrogen-Oxygen", surface="Rocky")

def test_collect_data(capsys, planet):
    collect_data(planet)
    captured = capsys.readouterr()
    assert "Сбор данных о Earth:" in captured.out
    assert "Масса: 5.972e+24 кг" in captured.out
    assert "Атмосфера: Nitrogen-Oxygen" in captured.out
    assert "Поверхность: Rocky" in captured.out