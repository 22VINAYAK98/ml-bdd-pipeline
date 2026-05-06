"""
Dataset loader utilities for BDD100K.
"""

import cv2

from .parser import BDDParser


class BDDDatasetLoader:
    """
    Dataset loader for BDD100K object detection data.
    """

    def __init__(self, image_dir: str, annotation_file: str):

        parser = BDDParser(
            image_dir=image_dir,
            annotation_file=annotation_file,
        )

        self.records = parser.parse()

    def __len__(self):

        return len(self.records)

    def __getitem__(self, index):

        record = self.records[index]

        image = cv2.imread(record.image_path)

        return {
            "image": image,
            "record": record,
        }