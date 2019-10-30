"""Utilities for formatting and performing arithmetic with readings."""

from dataclasses import dataclass


@dataclass
class Reading:
    """Represents a temperature reading."""

    scale: str = 'C'
    value: float = 0.0
    default_scale: str = None

    @staticmethod
    def convert(reading, scale: str):
        """Convert a Reading to a particular scale."""
        if reading.scale == scale:
            return reading
        elif reading.scale == 'C':
            return Reading(
                scale='F',
                value=(reading.value * 9/5) + 32
            )
        elif reading.scale == 'F':
            return Reading(
                scale='C',
                value=(reading.value - 32) * 5/9
            )

    def __post_init__(self):
        self.scale = self.scale.upper()
        if Reading.default_scale is None:
            Reading.default_scale = self.scale

    def __add__(self, other):
        if self.scale == other.scale:
            return Reading(
                self.scale,
                self.value + other.value
            )
        else:
            return self + Reading.convert(other, self.scale)

    def __radd__(self, other):
        if type(other) is int:
            return Reading(self.scale, self.value + other)

    def __truediv__(self, other):
        if type(other) is int:
            return Reading(self.scale, self.value / other)

    def __gt__(self, other):
        if self.scale != other.scale:
            return self > Reading.convert(other, self.scale)
        return self.value > other.value

    def __str__(self):
        default = Reading.default_scale or 'C'
        if self.scale != default:
            return str(
                Reading.convert(self, default)
            )
        return f'{self.value:.2f}°{self.scale}'
