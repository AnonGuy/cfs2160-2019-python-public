"""Take unlimited readings, convert them accordingly, and display statistics."""

import re

from typing import List

from utils import Reading


readings: List[Reading] = []

# Pattern to match temperatures, e.g. "120.2f" or "1C"
pattern = re.compile(
    '(?P<reading>\d+(.\d+)?)'
    '(?P<scale>[FfCc])?'
)

count = 1
# Continuously take input until input is invalid
while match := pattern.match(input(f'Enter reading {count}: ')):
    scale = match.group('scale') or Reading.default_scale or 'C'
    # New Reading instances will set default_scale if None
    reading = Reading(scale, match.group('reading'))
    readings.append(reading)
    count += 1

print('\nReadings:', *readings, sep='\n')

lowest, highest, average = (
    min(readings),
    max(readings),
    sum(readings) / len(readings)
)

print(
    '',
    f'Lowest:  {lowest}',
    f'Highest: {highest}',
    f'Average: {average}',
    sep='\n'
)
