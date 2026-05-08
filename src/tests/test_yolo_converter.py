"""
Sanity test for YOLO
dataset conversion.
"""

from src.data.loader import (
    BDDDatasetLoader,
)

from src.train.utils.dataset_converter import (
    YOLODatasetConverter,
)


def main():

    dataset = BDDDatasetLoader(
        image_dir="data/raw/assignment_data_bdd/bdd100k_images_100k/bdd100k/images/100k/train",

        annotation_file="data/raw/assignment_data_bdd/bdd100k_labels_release/bdd100k/labels/bdd100k_labels_images_train.json",
    )

    converter = (
        YOLODatasetConverter(
            output_dir="outputs/yolo_dataset"
        )
    )

    records = dataset.records[:10]

    converter.convert_records(
        records
    )

    print(
        "YOLO dataset conversion completed."
    )


if __name__ == "__main__":
    main()