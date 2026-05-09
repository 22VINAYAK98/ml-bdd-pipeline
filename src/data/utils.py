"""
Visualization utilities for BDD100K dataset.
"""

import cv2


def draw_annotations(image, record):
    """
    Draw bounding boxes and category labels on image.
    """

    annotated_image = image.copy()

    for annotation in record.annotations:

        bbox = annotation.bbox

        x1 = int(bbox.x1)
        y1 = int(bbox.y1)
        x2 = int(bbox.x2)
        y2 = int(bbox.y2)

        category = annotation.category

        cv2.rectangle(
            annotated_image,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2,
        )

        cv2.putText(
            annotated_image,
            category,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            1,
        )

    return annotated_image
