"""
Sanity test for prediction
visualization pipeline.
"""

from src.data.loader import BDDDatasetLoader
from src.evaluation.visualizer.prediction_visualizer import \
    PredictionVisualizer


def main():

    dataset = BDDDatasetLoader(
        image_dir="data/raw/assignment_data_bdd/bdd100k_images_100k/bdd100k/images/100k/val",
        annotation_file="data/raw/assignment_data_bdd/bdd100k_labels_release/bdd100k/labels/bdd100k_labels_images_val.json",
    )

    sample_records = dataset.records[:5]

    image_paths = [record.image_path for record in sample_records]

    visualizer = PredictionVisualizer(
        model_path=("outputs/" "yolo_training-3/" "weights/" "best.pt"),
        output_dir=("outputs/" "prediction_visualizations"),
    )

    visualizer.visualize_predictions(image_paths)


if __name__ == "__main__":
    main()
