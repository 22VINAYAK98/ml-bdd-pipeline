"""
Scene-based GT vs prediction
visualization for curriculum
benchmarking.
"""

from src.data.loader import BDDDatasetLoader
from src.evaluation.benchmark.curriculum_benchmark import CurriculumBenchmark
from src.evaluation.visualizer.gt_vs_prediction_visualizer import \
    GTVsPredictionVisualizer


def main():

    dataset = BDDDatasetLoader(
        image_dir="data/raw/assignment_data_bdd/bdd100k_images_100k/bdd100k/images/100k/val",
        annotation_file="data/raw/assignment_data_bdd/bdd100k_labels_release/bdd100k/labels/bdd100k_labels_images_val.json",
    )

    benchmark = CurriculumBenchmark(dataset.records)

    easy_records = (benchmark.get_easy_records())[:5]

    medium_records = (benchmark.get_medium_records())[:5]

    hard_records = (benchmark.get_hard_records())[:5]

    visualizer = GTVsPredictionVisualizer(
        model_path=("outputs/" "yolo_training-3/" "weights/" "best.pt"),
        output_dir=("outputs/" "gt_vs_prediction"),
    )

    visualizer.visualize(
        records=easy_records,
        scenario_name="easy",
    )

    visualizer.visualize(
        records=medium_records,
        scenario_name="medium",
    )

    visualizer.visualize(
        records=hard_records,
        scenario_name="hard",
    )


if __name__ == "__main__":
    main()
