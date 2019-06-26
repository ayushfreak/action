# pyre-strict
from dataclasses import dataclass
from math import asin, cos, radians, sin, sqrt


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self):
        print(self.name, self.lon, self.lat)


Position("ayush", 21, 12).distance_to()