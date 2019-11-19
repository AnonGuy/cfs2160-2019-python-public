"""Process a stream of vehicle data, then output statistics."""

import sys

from collections import defaultdict
from typing import List

from speed_camera import Reading, SPEED_LIMIT


vehicles = defaultdict(int)
readings: List[Reading] = []

count = 1
while (entry := input(f'Enter reading {count}: ')) != 'END':
    if reading := Reading.from_string(entry):
        readings.append(reading)
    count += 1

if readings:
    highest, lowest, average = (
        max(readings),
        min(readings),
        sum(readings) / len(readings)
    )
else:
    print('Not enough readings supplied.')
    sys.exit(1)

print(
    '',
    f'Vehicles seen: {count}',
    f'Highest speed: {highest}',
    f'Lowest speed: {lowest}',
    (
        f'Average speed: {average:.2f}mph '
        f'({average * 1.60934:.2f}kph)\n'
    ),
    sep='\n'
)

violations = 0
for reading in readings:
    if reading.violation:
        violations += 1
    vehicles[reading.vehicle] += 1

print(
    f'Number of {SPEED_LIMIT}mph violations: {violations} '
    f'({violations / len(readings):.2%})'
)
for vehicle, count in vehicles.items():
    print(
        f'Number of {Reading.descriptions.get(vehicle)}s: '
        f'{count} ({count / len(readings):.2%})'
    )
