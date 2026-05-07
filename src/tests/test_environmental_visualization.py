"""
Sanity test for environmental visualization.
"""

from src.data.loader import (
    BDDDatasetLoader,
)

from src.analysis.environmental_analysis import (
    EnvironmentalAnalyzer,
)

from src.analysis.environmental_visualization import (
    EnvironmentalVisualization,
)


def main():

    dataset = BDDDatasetLoader(
        image_dir="data/raw/assignment_data_bdd/bdd100k_images_100k/bdd100k/images/100k/train",

        annotation_file="data/raw/assignment_data_bdd/bdd100k_labels_release/bdd100k/labels/bdd100k_labels_images_train.json",
    )

    analysis_results = (
        EnvironmentalAnalyzer(
            dataset.records
        ).run()
    )

    visualizer = (
        EnvironmentalVisualization(
            analysis_results
        )
    )

    visualizer.run()

    print(
        "Environmental visualization completed."
    )


if __name__ == "__main__":
    main()