"""
Filtering utilities for BDD100K object detection annotations.

This module filters raw dataset annotations to retain only object detection
labels relevant to the assignment. Non-detection annotations such as lane
markings or drivable-area labels are excluded during parsing.
"""

# from .categories import DETECTION_CLASSES


# def is_valid_detection(label: dict) -> bool:
#     """
#     @brief Validate whether an annotation is a supported BDD100K object detection label.

#     @input
#     label (dict):
#         Annotation dictionary extracted from BDD100K JSON labels.

#     @output
#     bool:
#         True if:
#         - category belongs to supported detection classes
#         - annotation contains valid 2D bounding box data

#         False otherwise.
#     """

#     category = label.get("category")

#     if category not in DETECTION_CLASSES:
#         return False

#     if "box2d" not in label:
#         return False

#     return True


from .categories import DETECTION_CLASSES


def is_valid_detection(label: dict) -> bool:
    """
    @brief Validate whether an annotation is a supported BDD100K object detection label.

    @input
    label (dict):
        Annotation dictionary extracted from BDD100K JSON labels.

    @output
    bool:
        True if:
        - category belongs to supported detection classes
        - annotation contains valid 2D bounding box data

        False otherwise.
    """

    category = label.get("category")

    if category not in DETECTION_CLASSES:
        return False

    box2d = label.get("box2d")

    if not isinstance(box2d, dict):
        return False

    return True
