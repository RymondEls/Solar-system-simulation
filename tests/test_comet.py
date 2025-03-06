import pytest
from entities.comet import Comet

@pytest.fixture
def comet():
    return Comet(name="Halley", type="comet", mass=2.2e14, position=[8.8e10, 0], velocity=[0, 54000], color=(255, 255, 255), radius=11000, tail_length=1000000)

def test_comet_initialization(comet):
    assert comet.name == "Halley"
    assert comet.type == "comet"
    assert comet.tail_length == 1000000

def test_comet_to_dict(comet):
    comet_dict = comet.to_dict()
    assert comet_dict["name"] == "Halley"
    assert comet_dict["tail_length"] == 1000000