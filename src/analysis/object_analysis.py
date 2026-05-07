"""
Object-level analysis utilities for BDD100K dataset.

Focus areas:
- class distribution
- object density
- occlusion statistics
- truncation statistics
- bounding box statistics
"""

from collections import Counter
import statistics
from src.data.categories import VRU_CLASSES


class ClassDistributionAnalyzer:
    """
    Analyze object class distribution.
    """

    def __init__(self, records):

        self.records = records

    def run(self):

        class_counter = Counter()

        for record in self.records:

            for annotation in record.annotations:

                class_counter[annotation.category] += 1

        return dict(class_counter)


class DensityAnalyzer:
    """
    Analyze object density per image.
    """

    def __init__(self, records):

        self.records = records

    def run(self):

        object_counts = []

        for record in self.records:

            object_counts.append(
                len(record.annotations)
            )

        return {
            "min_objects": min(object_counts),
            "max_objects": max(object_counts),
            "avg_objects":
                sum(object_counts) / len(object_counts),
        }


class OcclusionAnalyzer:
    """
    Analyze occlusion and truncation statistics.
    """

    def __init__(self, records):

        self.records = records

    def analyze_occlusion(self):

        total_objects = 0
        occluded_objects = 0

        for record in self.records:

            for annotation in record.annotations:

                total_objects += 1

                if annotation.occluded:
                    occluded_objects += 1

        return {
            "total_objects": total_objects,
            "occluded_objects": occluded_objects,
            "occlusion_ratio":
                occluded_objects / total_objects,
        }

    def analyze_truncation(self):

        total_objects = 0
        truncated_objects = 0

        for record in self.records:

            for annotation in record.annotations:

                total_objects += 1

                if annotation.truncated:
                    truncated_objects += 1

        return {
            "total_objects": total_objects,
            "truncated_objects": truncated_objects,
            "truncation_ratio":
                truncated_objects / total_objects,
        }

    def run(self):

        return {
            "occlusion_statistics":
                self.analyze_occlusion(),

            "truncation_statistics":
                self.analyze_truncation(),
        }


class BoundingBoxAnalyzer:
    """
    Analyze bounding box statistics.
    """

    def __init__(self, records):

        self.records = records

    def run(self):

        widths = []
        heights = []
        areas = []

        for record in self.records:

            for annotation in record.annotations:

                bbox = annotation.bbox

                width = bbox.x2 - bbox.x1
                height = bbox.y2 - bbox.y1

                area = width * height

                widths.append(width)
                heights.append(height)
                areas.append(area)

        return {

            "min_width": min(widths),
            "max_width": max(widths),
            "avg_width": sum(widths) / len(widths),

            "min_height": min(heights),
            "max_height": max(heights),
            "avg_height": sum(heights) / len(heights),

            "min_area": min(areas),
            "max_area": max(areas),
            "avg_area": sum(areas) / len(areas),

            "median_area": statistics.median(areas),

            "areas": areas,
        }


class ClassDistributionByTimeOfDay:
    """
    Analyze class distribution across
    different illumination conditions.
    """

    def __init__(self, records):

        self.records = records

    def run(self):

        distribution = {}

        for record in self.records:

            timeofday = record.timeofday

            if timeofday not in distribution:

                distribution[timeofday] = Counter()

            for annotation in record.annotations:

                distribution[timeofday][
                    annotation.category
                ] += 1

        final_distribution = {}

        for timeofday, counter in distribution.items():

            final_distribution[
                timeofday
            ] = dict(counter)

        return final_distribution


class VulnerableRoadUserAnalyzer:
    """
    Analyze vulnerable road users under
    different illumination and occlusion
    conditions.
    """

    def __init__(self, records):

        self.records = records

    def run(self):

        stats = {

            "night_other_objects": 0,

            "night_occluded_vru_objects": 0,

            "day_other_objects": 0,

            "day_occluded_vru_objects": 0,
        }

        for record in self.records:

            is_night = (
                record.timeofday == "night"
            )

            for annotation in record.annotations:

                is_vru = (
                    annotation.category
                    in VRU_CLASSES
                )

                is_occluded = (
                    annotation.occluded
                )

                if is_night:

                    if (
                        is_vru
                        and is_occluded
                    ):

                        stats[
                            "night_occluded_vru_objects"
                        ] += 1

                    elif not is_vru:

                        stats[
                            "night_other_objects"
                        ] += 1

                else:

                    if (
                        is_vru
                        and is_occluded
                    ):

                        stats[
                            "day_occluded_vru_objects"
                        ] += 1

                    elif not is_vru:

                        stats[
                            "day_other_objects"
                        ] += 1

        return stats


class ObjectAnalysisPipeline:
    """
    Aggregates all object-level analysis modules.
    """

    def __init__(self, records):

        self.records = records

    def run(self):

        return {

            "class_distribution":
                ClassDistributionAnalyzer(
                    self.records
                ).run(),

            "density_statistics":
                DensityAnalyzer(
                    self.records
                ).run(),

            "occlusion_statistics":
                OcclusionAnalyzer(
                    self.records
                ).run(),

            "bounding_box_statistics":
                BoundingBoxAnalyzer(
                    self.records
                ).run(),

            "timeofday_class_distribution":
                ClassDistributionByTimeOfDay(
                    self.records
                ).run(),

            "vru_analysis":
                VulnerableRoadUserAnalyzer(
                    self.records
                ).run(),
        }
