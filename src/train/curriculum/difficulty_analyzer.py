"""
Difficulty analysis utilities for
curriculum-based ADAS training.

The objective of this module is to estimate
scene-level perception difficulty using
environmental and object-level signals.

The generated difficulty scores can later
be used for:
- curriculum learning
- staged training
- hard example mining
- perception-focused evaluation
"""

from src.data.categories import VRU_CLASSES


class DifficultyAnalyzer:
    """
    Analyze perception difficulty of an image
    record for curriculum-based training.
    """

    def __init__(self):

        # Difficulty weights can later
        # be externalized into config files.

        self.night_weight = 3.0

        self.occlusion_weight = 2.0

        self.vru_weight = 2.0

        self.dense_scene_weight = 2.0

        self.small_object_weight = 2.0

        self.dense_scene_threshold = 15

        self.small_bbox_area_threshold = 2500

    def analyze(self, record):
        """
        Compute difficulty score for a
        single ImageRecord.

        Input:
            record:
                Structured ImageRecord object.

        Output:
            Dictionary containing:
            - difficulty_score
            - difficulty_level
            - difficulty_breakdown
        """

        difficulty_score = 0.0

        difficulty_breakdown = {}

        # -------------------------------------------------
        # Nighttime Difficulty
        # -------------------------------------------------

        if record.timeofday == "night":

            difficulty_score += self.night_weight

            difficulty_breakdown["nighttime"] = self.night_weight

        # -------------------------------------------------
        # Occlusion Difficulty
        # -------------------------------------------------

        occluded_objects = 0

        for annotation in record.annotations:

            if annotation.occluded:

                occluded_objects += 1

        occlusion_score = occluded_objects * self.occlusion_weight

        difficulty_score += occlusion_score

        difficulty_breakdown["occlusion"] = occlusion_score

        # -------------------------------------------------
        # Vulnerable Road User Difficulty
        # -------------------------------------------------

        vru_count = 0

        for annotation in record.annotations:

            if annotation.category in VRU_CLASSES:

                vru_count += 1

        vru_score = vru_count * self.vru_weight

        difficulty_score += vru_score

        difficulty_breakdown["vru_presence"] = vru_score

        # -------------------------------------------------
        # Dense Scene Difficulty
        # -------------------------------------------------

        total_objects = len(record.annotations)

        if total_objects >= self.dense_scene_threshold:

            difficulty_score += self.dense_scene_weight

            difficulty_breakdown["dense_scene"] = self.dense_scene_weight

        # -------------------------------------------------
        # Small Object Difficulty
        # -------------------------------------------------

        small_objects = 0

        for annotation in record.annotations:

            bbox = annotation.bbox

            width = bbox.x2 - bbox.x1

            height = bbox.y2 - bbox.y1

            area = width * height

            if area <= self.small_bbox_area_threshold:

                small_objects += 1

        small_object_score = small_objects * self.small_object_weight

        difficulty_score += small_object_score

        difficulty_breakdown["small_objects"] = small_object_score

        # -------------------------------------------------
        # Difficulty Level Assignment
        # -------------------------------------------------

        if difficulty_score < 5:

            difficulty_level = "easy"

        elif difficulty_score < 15:

            difficulty_level = "medium"

        else:

            difficulty_level = "hard"

        return {
            "difficulty_score": difficulty_score,
            "difficulty_level": difficulty_level,
            "difficulty_breakdown": difficulty_breakdown,
        }
