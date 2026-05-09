"""
Sanity test for GT vs
prediction visualization.
"""

from src.data.loader import (
    BDDDatasetLoader,
)

from src.evaluation.benchmark.scene_benchmark import (
    SceneBenchmark,
)

from src.evaluation.visualizer.gt_vs_prediction_visualizer import (
    GTVsPredictionVisualizer,
)


def main():

    dataset = BDDDatasetLoader(
            
        image_dir="data/raw/assignment_data_bdd/bdd100k_images_100k/bdd100k/images/100k/val",

        annotation_file="data/raw/assignment_data_bdd/bdd100k_labels_release/bdd100k/labels/bdd100k_labels_images_val.json",
    )

    benchmark = SceneBenchmark(
        dataset.records
    )

    records = (
        benchmark
        .get_night_occluded_vru_records()
    )[:10]

    # the above scene record can be cganged to 
    # benchmark.get_night_vru_records()
    # benchmark.get_day_occluded_records()
    # benchmark.get_night_occluded_vru_records() etc 

    visualizer = (
        GTVsPredictionVisualizer(

            model_path=(
                "outputs/"
                "yolo_training-3/"
                "weights/"
                "best.pt"
            ),

            output_dir=(
                "outputs/"
                "gt_vs_prediction"
            ),
        )
    )

    visualizer.visualize(

        records=records,

        scenario_name=(
            "night_occluded_vru"
        ),
    )


if __name__ == "__main__":
    main()