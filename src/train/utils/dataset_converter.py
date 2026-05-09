"""
Dataset conversion utilities.

Responsible for converting internal
dataset representation into
model-specific training formats.
"""

import os
import shutil

import yaml

from src.data.categories import CLASS_TO_ID


class YOLODatasetConverter:
    """
    Convert dataset into YOLO format.
    """

    def __init__(
        self,
        output_dir,
    ):

        self.output_dir = output_dir

        self.image_output_dir = os.path.join(
            self.output_dir,
            "images",
        )

        self.label_output_dir = os.path.join(
            self.output_dir,
            "labels",
        )

        os.makedirs(
            self.image_output_dir,
            exist_ok=True,
        )

        os.makedirs(
            self.label_output_dir,
            exist_ok=True,
        )

    def convert_records(
        self,
        records,
    ):
        """
        Convert ImageRecords into
        YOLO dataset format.
        """

        for record in records:

            self._copy_image(record)

            self._write_label_file(record)

        self._generate_yaml()

    def _write_label_file(
        self,
        record,
    ):
        """
        Generate YOLO annotation file.
        """

        label_file_name = record.image_name.replace(".jpg", ".txt")

        label_path = os.path.join(
            self.label_output_dir,
            label_file_name,
        )

        image_width = record.image_width

        image_height = record.image_height

        with open(
            label_path,
            "w",
        ) as file:

            for annotation in record.annotations:

                category = annotation.category

                if category not in CLASS_TO_ID:

                    continue

                class_id = CLASS_TO_ID[category]

                bbox = annotation.bbox

                x_center = ((bbox.x1 + bbox.x2) / 2) / image_width

                y_center = ((bbox.y1 + bbox.y2) / 2) / image_height

                width = (bbox.x2 - bbox.x1) / image_width

                height = (bbox.y2 - bbox.y1) / image_height

                file.write(
                    f"{class_id} "
                    f"{x_center} "
                    f"{y_center} "
                    f"{width} "
                    f"{height}\n"
                )

    def _copy_image(
        self,
        record,
    ):
        """
        Copy image into YOLO
        dataset image directory.
        """

        destination_path = os.path.join(
            self.image_output_dir,
            record.image_name,
        )

        shutil.copy(
            record.image_path,
            destination_path,
        )

    def _generate_yaml(self):
        """
        Generate YOLO dataset YAML.
        """

        yaml_path = os.path.join(
            self.output_dir,
            "dataset.yaml",
        )

        class_names = list(CLASS_TO_ID.keys())

        yaml_data = {
            "path": self.output_dir,
            "train": "images",
            "val": "images",
            "names": class_names,
        }

        with open(
            yaml_path,
            "w",
        ) as file:

            yaml.dump(
                yaml_data,
                file,
                sort_keys=False,
            )
