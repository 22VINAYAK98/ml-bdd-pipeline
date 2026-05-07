"""
Sanity test for environmental analysis.
"""

from pprint import pprint

from src.data.loader import BDDDatasetLoader

from src.analysis.environmental_analysis import (
    EnvironmentalAnalyzer,
)


def main():

    dataset = BDDDatasetLoader(
        image_dir="data/raw/assignment_data_bdd/bdd100k_images_100k/bdd100k/images/100k/train",

        annotation_file="data/raw/assignment_data_bdd/bdd100k_labels_release/bdd100k/labels/bdd100k_labels_images_train.json",
    )

    analyzer = EnvironmentalAnalyzer(dataset.records)

    results = analyzer.run()

    pprint(results)


if __name__ == "__main__":
    main()