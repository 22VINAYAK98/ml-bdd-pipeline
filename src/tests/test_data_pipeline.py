"""
Sanity test for BDD100K data pipeline.

This script validates:
- JSON parsing
- detection filtering
- dataset loading
- image loading
- bounding box visualization
"""

import cv2

from src.data.loader import BDDDatasetLoader
from src.data.utils import draw_annotations


def main():

    dataset = BDDDatasetLoader(
        image_dir="data/raw/assignment_data_bdd/bdd100k_images_100k/bdd100k/images/100k/train",

        annotation_file="data/raw/assignment_data_bdd/bdd100k_labels_release/bdd100k/labels/bdd100k_labels_images_train.json",
    )

    print(f"Total records: {len(dataset)}")

    sample = dataset[0]

    image = sample["image"]

    record = sample["record"]

    print(record)

    annotated_image = draw_annotations(image, record)

    cv2.imwrite(
        "outputs/sample_detection.jpg",
        annotated_image,
    )

    print("Data pipeline validation completed successfully.")


if __name__ == "__main__":
    main()