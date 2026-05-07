"""
Sanity test for object analysis visualization.
"""

from src.data.loader import (
    BDDDatasetLoader,
)

from src.analysis.object_analysis import (
    ObjectAnalysisPipeline,
)

from src.analysis.object_visualization import (
    ObjectVisualization,
)


def main():

    dataset = BDDDatasetLoader(
        image_dir="data/raw/assignment_data_bdd/bdd100k_images_100k/bdd100k/images/100k/train",

        annotation_file="data/raw/assignment_data_bdd/bdd100k_labels_release/bdd100k/labels/bdd100k_labels_images_train.json",
    )

    analysis_results = (
        ObjectAnalysisPipeline(
            dataset.records
        ).run()
    )

    visualizer = ObjectVisualization(
        analysis_results
    )

    visualizer.run()

    print(
        "Object visualization completed."
    )


if __name__ == "__main__":
    main()