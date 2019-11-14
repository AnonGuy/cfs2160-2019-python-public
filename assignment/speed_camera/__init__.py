"""Utility methods for use in the main program."""

import re
from dataclasses import dataclass
from typing import Any


SPEED_LIMIT = 50

vehicle_pattern = re.compile(r'([HLC])(\d\d)')


@dataclass
class Reading:
    """A Reading taken by the speed camera."""

    vehicle: str
    speed: int

    descriptions = dict(
        H='Heavy Goods Vehicle',
        L='Light Goods Vehicle',
        C='Car'
    )

    def __post_init__(self):
        """Prepare dataclass attributes."""
        self.speed = int(self.speed)
        self.violation = self.speed > SPEED_LIMIT

    def from_string(string: str):
        """Create a Reading from a line of stdin."""
        match = vehicle_pattern.match(string)
        if match is not None:
            return Reading(*match.groups())
        else:
            return None

    def __str__(self):
        """Represent a Reading as a descriptive string."""
        vehicle = Reading.descriptions.get(
            self.vehicle,
            'Unknown vehicle'
        )
        kph = self.speed * 1.60934
        return f'{vehicle} at {self.speed:.2f}mph ({kph:.2f}kph)'

    def __add__(self, other):
        """Add the speed attribute of Readings."""
        return self.speed + other.speed

    def __radd__(self, other):
        """Add an integer (0) to a Reading value."""
        return self.speed + other

    def __gt__(self, other):
        """Use the speed attribute to sort between Readings."""
        return self.speed > other.speed
