"""
 In ADAS Context : Environmental analysis or data which recodrs environment plays very importatnt role
 Environmental analysis utilities for BDD100K dataset.

Focus areas:
- weather distribution
- scene distribution
- time-of-day distribution
"""

from collections import Counter


class EnvironmentalAnalyzer:

    def __init__(self, records):

        self.records = records

    def analyze_weather_distribution(self):

        weather_counter = Counter()

        for record in self.records:

            weather_counter[record.weather] += 1

        return dict(weather_counter)

    def analyze_scene_distribution(self):

        scene_counter = Counter()

        for record in self.records:

            scene_counter[record.scene] += 1

        return dict(scene_counter)

    def analyze_timeofday_distribution(self):

        timeofday_counter = Counter()

        for record in self.records:

            timeofday_counter[record.timeofday] += 1

        return dict(timeofday_counter)

    def run(self):

        return {
            "weather_distribution": self.analyze_weather_distribution(),
            "scene_distribution": self.analyze_scene_distribution(),
            "timeofday_distribution": self.analyze_timeofday_distribution(),
        }
