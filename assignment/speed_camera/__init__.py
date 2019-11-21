"""Utility methods for use in the main program."""

import re
from dataclasses import dataclass


SPEED_LIMIT = 50

# A valid reading will consist of three characters: 1 Letter (H, L or C) and 2 digits
# This regular expression will match one of [HLC] followed by two digits
vehicle_pattern = re.compile(r'([HLC])(\d\d)')


@dataclass
class Reading:
    """A Reading taken by the speed camera."""

    # 1-character string representing a vehicle type
    vehicle: str
    speed: int

    descriptions = dict(
        H='Heavy Goods Vehicle',
        L='Light Goods Vehicle',
        C='Car'
    )

    def __post_init__(self):
        """Prepare dataclass attributes."""
        # Cast speed to int if it isn't already
        self.speed = int(self.speed)
        # Reading.violation checks if reading is above the limit
        self.violation: bool = self.speed > SPEED_LIMIT

    def from_string(string: str):
        """Create a Reading from a line of stdin."""
        # If the string is a valid reading:
        if (match := vehicle_pattern.match(string)):
            # Create a new Reading object with the pattern matches
            return Reading(*match.groups())
        else:
            return None

    def __str__(self):
        """Represent a Reading as a descriptive string."""
        # Get the vehicle description, or "Unknown" if it doesn't exist
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
