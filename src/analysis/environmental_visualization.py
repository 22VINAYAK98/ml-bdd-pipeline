"""
Visualization utilities for
environmental analysis.
"""

import matplotlib.pyplot as plt


class EnvironmentalVisualization:

    def __init__(self, analysis_results):

        self.analysis_results = analysis_results

    def plot_weather_distribution(self):

        distribution = (
            self.analysis_results[
                "weather_distribution"
            ]
        )

        labels = list(
            distribution.keys()
        )

        values = list(
            distribution.values()
        )

        plt.figure(figsize=(10, 6))

        plt.bar(labels, values)

        plt.xlabel("Weather")

        plt.ylabel("Image Count")

        plt.title(
            "Weather Distribution"
        )

        plt.tight_layout()

        plt.savefig(
            "outputs/weather_distribution.png"
        )

        plt.close()

    def plot_scene_distribution(self):

        distribution = (
            self.analysis_results[
                "scene_distribution"
            ]
        )

        labels = list(
            distribution.keys()
        )

        values = list(
            distribution.values()
        )

        plt.figure(figsize=(10, 6))

        plt.bar(labels, values)

        plt.xlabel("Scene Type")

        plt.ylabel("Image Count")

        plt.title(
            "Scene Distribution"
        )

        plt.xticks(rotation=20)

        plt.tight_layout()

        plt.savefig(
            "outputs/scene_distribution.png"
        )

        plt.close()

    def plot_timeofday_distribution(self):

        distribution = (
            self.analysis_results[
                "timeofday_distribution"
            ]
        )

        labels = list(
            distribution.keys()
        )

        values = list(
            distribution.values()
        )

        plt.figure(figsize=(6, 6))

        plt.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
        )

        plt.title(
            "Time Of Day Distribution"
        )

        plt.savefig(
            "outputs/timeofday_distribution.png"
        )

        plt.close()

    def run(self):

        self.plot_weather_distribution()

        self.plot_scene_distribution()

        self.plot_timeofday_distribution()