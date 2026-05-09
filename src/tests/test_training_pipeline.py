"""
Sanity test for training pipeline.
"""

from src.data.loader import BDDDatasetLoader
from src.train.pipeline.trainer import TrainingPipeline
from src.train.strategies.yolo_strategy import YOLOTrainingStrategy


def main():

    dataset = BDDDatasetLoader(
        image_dir="data/raw/assignment_data_bdd/bdd100k_images_100k/bdd100k/images/100k/train",
        annotation_file="data/raw/assignment_data_bdd/bdd100k_labels_release/bdd100k/labels/bdd100k_labels_images_train.json",
    )

    strategy = YOLOTrainingStrategy()

    pipeline = TrainingPipeline(
        dataset.records[:500],  # temporarily restricting dataset to only 100 samples
        strategy,
    )

    pipeline.run(curriculum_stage="medium")


if __name__ == "__main__":
    main()
