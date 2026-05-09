"""
Sanity test for scene-aware
benchmarking pipeline.
"""

from pprint import pprint

from src.data.loader import BDDDatasetLoader
from src.evaluation.benchmark.scene_benchmark import SceneBenchmark


def main():

    dataset = BDDDatasetLoader(
        image_dir="data/raw/assignment_data_bdd/bdd100k_images_100k/bdd100k/images/100k/val",
        annotation_file="data/raw/assignment_data_bdd/bdd100k_labels_release/bdd100k/labels/bdd100k_labels_images_val.json",
    )

    benchmark = SceneBenchmark(dataset.records)

    summary = benchmark.get_summary()

    pprint(summary)


if __name__ == "__main__":
    main()
