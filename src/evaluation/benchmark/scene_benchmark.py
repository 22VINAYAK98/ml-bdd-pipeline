"""
Scenario-aware benchmarking utilities
for ADAS perception evaluation.
"""

from src.data.categories import VRU_CLASSES


class SceneBenchmark:
    """
    Generate scenario-specific
    benchmark subsets.
    """

    def __init__(
        self,
        records,
    ):

        self.records = records

    # ----------------------------------
    # Helper Functions
    # ----------------------------------

    def _contains_vru(
        self,
        record,
    ):

        for annotation in record.annotations:

            if annotation.category in VRU_CLASSES:

                return True

        return False

    def _contains_occluded_vru(
        self,
        record,
    ):

        for annotation in record.annotations:

            if annotation.category in VRU_CLASSES and annotation.occluded:

                return True

        return False

    def _has_occlusion(
        self,
        record,
    ):

        for annotation in record.annotations:

            if annotation.occluded:

                return True

        return False

    def _is_dense_scene(
        self,
        record,
        threshold=15,
    ):

        return len(record.annotations) >= threshold

    # ----------------------------------
    # VRU-Based Benchmarks
    # ----------------------------------

    def get_night_vru_records(
        self,
    ):

        return [
            record
            for record in self.records
            if (record.timeofday == "night" and self._contains_vru(record))
        ]

    def get_day_vru_records(
        self,
    ):

        return [
            record
            for record in self.records
            if (record.timeofday == "daytime" and self._contains_vru(record))
        ]

    def get_night_non_vru_records(
        self,
    ):

        return [
            record
            for record in self.records
            if (record.timeofday == "night" and not self._contains_vru(record))
        ]

    def get_day_non_vru_records(
        self,
    ):

        return [
            record
            for record in self.records
            if (record.timeofday == "daytime" and not self._contains_vru(record))
        ]

    def get_occluded_vru_records(
        self,
    ):

        return [
            record for record in self.records if self._contains_occluded_vru(record)
        ]

    # ----------------------------------
    # Occlusion-Based Benchmarks
    # ----------------------------------

    def get_day_occluded_records(
        self,
    ):

        return [
            record
            for record in self.records
            if (record.timeofday == "daytime" and self._has_occlusion(record))
        ]

    def get_night_occluded_records(
        self,
    ):

        return [
            record
            for record in self.records
            if (record.timeofday == "night" and self._has_occlusion(record))
        ]

    def get_day_non_occluded_records(
        self,
    ):

        return [
            record
            for record in self.records
            if (record.timeofday == "daytime" and not self._has_occlusion(record))
        ]

    def get_night_non_occluded_records(
        self,
    ):

        return [
            record
            for record in self.records
            if (record.timeofday == "night" and not self._has_occlusion(record))
        ]

    # ----------------------------------
    # Combined High-Difficulty
    # Benchmarks
    # ----------------------------------

    def get_night_occluded_vru_records(
        self,
    ):

        return [
            record
            for record in self.records
            if (record.timeofday == "night" and self._contains_occluded_vru(record))
        ]

    def get_day_occluded_vru_records(
        self,
    ):

        return [
            record
            for record in self.records
            if (record.timeofday == "daytime" and self._contains_occluded_vru(record))
        ]

    # ----------------------------------
    # Dense Scene Benchmarks
    # ----------------------------------

    def get_dense_scene_records(
        self,
    ):

        return [record for record in self.records if self._is_dense_scene(record)]

    # ----------------------------------
    # Benchmark Summary
    # ----------------------------------

    def get_summary(
        self,
    ):

        summary = {
            # VRU
            "night_vru": len(self.get_night_vru_records()),
            "day_vru": len(self.get_day_vru_records()),
            "night_non_vru": len(self.get_night_non_vru_records()),
            "day_non_vru": len(self.get_day_non_vru_records()),
            # Occlusion
            "day_occluded": len(self.get_day_occluded_records()),
            "night_occluded": len(self.get_night_occluded_records()),
            "day_non_occluded": len(self.get_day_non_occluded_records()),
            "night_non_occluded": len(self.get_night_non_occluded_records()),
            # Combined
            "night_occluded_vru": len(self.get_night_occluded_vru_records()),
            "day_occluded_vru": len(self.get_day_occluded_vru_records()),
            # Dense
            "dense_scenes": len(self.get_dense_scene_records()),
        }

        return summary
