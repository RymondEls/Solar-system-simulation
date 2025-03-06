import pytest
import json
import os
from utils.json_load import load_bodies_from_json, save_bodies_to_json
from entities.planet import Planet

@pytest.fixture
def temp_json_file(tmpdir):
    data = [
        {
            "name": "Earth",
            "type": "planet",
            "mass": 5.972e24,
            "position": [0, 0],
            "velocity": [0, 0],
            "color": [0, 0, 255],
            "radius": 6371000,
            "atmosphere": "Nitrogen-Oxygen",
            "surface": "Rocky"
        }
    ]
    file_path = tmpdir.join("test.json")
    with open(file_path, "w") as f:
        json.dump(data, f)
    return file_path

def test_load_bodies_from_json(temp_json_file):
    bodies = load_bodies_from_json(temp_json_file)
    assert len(bodies) == 1
    assert isinstance(bodies[0], Planet)
    assert bodies[0].name == "Earth"

def test_save_bodies_to_json(temp_json_file):
    bodies = [Planet(name="Earth", type="planet", mass=5.972e24, position=[0, 0], velocity=[0, 0], color=(0, 0, 255), radius=6371000, atmosphere="Nitrogen-Oxygen", surface="Rocky")]
    save_bodies_to_json(temp_json_file, bodies)
    with open(temp_json_file, "r") as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["name"] == "Earth"