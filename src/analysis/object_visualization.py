"""
Visualization utilities for object-level analysis.
"""

import matplotlib.pyplot as plt
from matplotlib_venn import venn2


class ObjectVisualization:

    def __init__(self, analysis_results):

        self.analysis_results = analysis_results

    def plot_class_distribution(self):

        class_distribution = self.analysis_results["class_distribution"]

        classes = list(class_distribution.keys())

        counts = list(class_distribution.values())

        plt.figure(figsize=(12, 6))

        plt.bar(classes, counts)

        plt.xticks(rotation=45)

        plt.xlabel("Object Classes")
        plt.ylabel("Object Count")

        plt.title("BDD100K Object Class Distribution")

        plt.tight_layout()

        plt.savefig("outputs/class_distribution.png")

        plt.close()

    def plot_bbox_area_distribution(self):

        bbox_stats = self.analysis_results["bounding_box_statistics"]

        areas = bbox_stats["areas"]

        plt.figure(figsize=(10, 6))

        plt.hist(
            areas,
            bins=50,
        )

        plt.xlabel("Bounding Box Area")

        plt.ylabel("Frequency")

        plt.title("Bounding Box Area Distribution")

        plt.tight_layout()

        plt.savefig("outputs/bbox_area_distribution.png")

        plt.close()

    def plot_occlusion_distribution(self):

        occlusion_stats = self.analysis_results["occlusion_statistics"][
            "occlusion_statistics"
        ]

        occluded = occlusion_stats["occluded_objects"]

        total = occlusion_stats["total_objects"]

        non_occluded = total - occluded

        labels = [
            "Occluded",
            "Non-Occluded",
        ]

        values = [
            occluded,
            non_occluded,
        ]

        plt.figure(figsize=(6, 6))

        plt.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
        )

        plt.title("Object Occlusion Distribution")

        plt.savefig("outputs/occlusion_distribution.png")

        plt.close()

    def plot_class_distribution_by_timeofday(self):

        distribution = self.analysis_results["timeofday_class_distribution"]

        time_conditions = list(distribution.keys())

        all_classes = set()

        for class_counts in distribution.values():

            all_classes.update(class_counts.keys())

        all_classes = sorted(all_classes)

        data = {}

        for class_name in all_classes:

            data[class_name] = []

            for time_condition in time_conditions:

                count = distribution[time_condition].get(class_name, 0)

                data[class_name].append(count)

        plt.figure(figsize=(14, 7))

        bottom = [0] * len(time_conditions)

        for class_name in all_classes:

            values = data[class_name]

            plt.bar(
                time_conditions,
                values,
                bottom=bottom,
                label=class_name,
            )

            bottom = [b + v for b, v in zip(bottom, values)]

        plt.xlabel("Time Of Day")

        plt.ylabel("Object Count")

        plt.title("Class Distribution Across Time Of Day")

        plt.legend()

        plt.tight_layout()

        plt.savefig("outputs/timeofday_class_distribution.png")

        plt.close()

    def plot_vru_perception_risk_analysis(self):

        stats = self.analysis_results["vru_analysis"]

        labels = [
            "Night Other\nObjects",
            "Night Occluded\nVRUs",
            "Day Other\nObjects",
            "Day Occluded\nVRUs",
        ]

        values = [
            stats["night_other_objects"],
            stats["night_occluded_vru_objects"],
            stats["day_other_objects"],
            stats["day_occluded_vru_objects"],
        ]

        plt.figure(figsize=(10, 6))

        plt.bar(labels, values)

        plt.ylabel("Object Count")

        plt.title("VRU Perception Risk Analysis")

        plt.tight_layout()

        plt.savefig("outputs/vru_perception_risk_analysis.png")

        plt.close()

    def run(self):

        self.plot_class_distribution()

        self.plot_bbox_area_distribution()

        self.plot_occlusion_distribution()

        self.plot_class_distribution_by_timeofday()

        self.plot_vru_perception_risk_analysis()
