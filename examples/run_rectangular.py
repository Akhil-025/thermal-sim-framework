import sys
import os
import yaml

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from src.geometry.rectangular_channel import generate_rectangular_channel

with open("configs/base_rectangular.yaml", "r") as f:
    config = yaml.safe_load(f)

geom = config["geometry"]

geometry_data = generate_rectangular_channel(
    length=geom["length"],
    width=geom["width"],
    height=geom["height"]
)

print(geometry_data)
