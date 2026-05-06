"""
BDD100K dataset parser utilities.
"""

import json
from pathlib import Path

from .entities import (
    BoundingBox,
    Annotation,
    ImageRecord,
)

from .filters import is_valid_detection


class BDDParser:
    """
    Parser for BDD100K object detection annotations.
    """

    def __init__(self, image_dir: str, annotation_file: str):

        self.image_dir = Path(image_dir)
        self.annotation_file = Path(annotation_file)

    def load_json(self):

        with open(self.annotation_file, "r") as file:
            return json.load(file)

    def parse_annotation(self, label: dict) -> Annotation:

        box = label["box2d"]

        bbox = BoundingBox(
            x1=box["x1"],
            y1=box["y1"],
            x2=box["x2"],
            y2=box["y2"],
        )

        attributes = label.get("attributes", {})

        return Annotation(
            label_id=label.get("id", -1),

            category=label["category"],
            bbox=bbox,

            occluded=attributes.get("occluded", False),
            truncated=attributes.get("truncated", False),
            )

    def parse_image_record(self, item: dict) -> ImageRecord:

        image_name = item["name"]

        attributes = item.get("attributes", {})

        annotations = []

        for label in item.get("labels", []):

            if not is_valid_detection(label):
                continue

            annotation = self.parse_annotation(label)

            annotations.append(annotation)

        return ImageRecord(
            image_name=image_name,
            image_path=str(self.image_dir / image_name),

            weather=attributes.get("weather", "unknown"),
            scene=attributes.get("scene", "unknown"),
            timeofday=attributes.get("timeofday", "unknown"),

            timestamp=item.get("timestamp", -1),

            annotations=annotations,
        )

    def parse(self):

        raw_data = self.load_json()

        records = []

        for item in raw_data:

            record = self.parse_image_record(item)

            records.append(record)

        return records