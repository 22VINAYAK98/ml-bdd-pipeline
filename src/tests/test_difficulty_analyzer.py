"""
Sanity test for curriculum
difficulty analyzer.
"""

from pprint import pprint

from src.data.loader import (
    BDDDatasetLoader,
)

from src.train.curriculum.difficulty_analyzer import (
    DifficultyAnalyzer,
)


def main():

    dataset = BDDDatasetLoader(
        image_dir="data/raw/assignment_data_bdd/bdd100k_images_100k/bdd100k/images/100k/train",

        annotation_file="data/raw/assignment_data_bdd/bdd100k_labels_release/bdd100k/labels/bdd100k_labels_images_train.json",
    )

    analyzer = DifficultyAnalyzer()

    sample_count = 5

    for index in range(sample_count):

        record = dataset.records[index]

        result = analyzer.analyze(
            record
        )

        print("\n")
        print(
            f"Image: {record.image_name}"
        )

        pprint(result)


if __name__ == "__main__":
    main()