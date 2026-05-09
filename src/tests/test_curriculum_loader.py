"""
Sanity test for curriculum
learning pipeline.
"""

from pprint import pprint

from src.data.loader import BDDDatasetLoader
from src.train.curriculum.curriculum_loader import CurriculumLoader


def main():

    dataset = BDDDatasetLoader(
        image_dir="data/raw/assignment_data_bdd/bdd100k_images_100k/bdd100k/images/100k/train",
        annotation_file="data/raw/assignment_data_bdd/bdd100k_labels_release/bdd100k/labels/bdd100k_labels_images_train.json",
    )

    curriculum_loader = CurriculumLoader(dataset.records)

    print("\nCurriculum Summary:\n")

    pprint(curriculum_loader.get_stage_summary())

    print("\nEasy Samples:\n")

    easy_samples = curriculum_loader.get_stage_records("easy")[:3]

    for sample in easy_samples:

        pprint(sample)


if __name__ == "__main__":
    main()
