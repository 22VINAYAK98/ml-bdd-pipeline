"""
Main entry point for BDD100K pipeline.
"""

import cv2

from src.data.utils import draw_annotations

from src.data.loader import BDDDatasetLoader


def main():

    dataset = BDDDatasetLoader(
        image_dir="/app/data/raw/assignment_data_bdd/bdd100k_images_100k/bdd100k/images/100k/train",

        annotation_file="/app/data/raw/assignment_data_bdd/bdd100k_labels_release/bdd100k/labels/bdd100k_labels_images_train.json",
    )
    print(type(dataset.records))
    print(len(dataset.records))
    print(dataset.records[0])

    print(f"Total records: {len(dataset)}")

    sample = dataset[0]

    image = sample["image"]

    record = sample["record"]

    annotated_image = draw_annotations(image, record)

    cv2.imwrite(
        "outputs/sample_detection.jpg",
        annotated_image,
    )

    print("Annotated image saved successfully.")

    print(sample["image"].shape)
    print(len(sample["record"].annotations))
    print(sample["record"])


if __name__ == "__main__":
    main()