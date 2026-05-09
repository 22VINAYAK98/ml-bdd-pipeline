"""
Sanity test for quantitative
curriculum benchmarking.
"""

from pprint import pprint

from src.data.loader import (
    BDDDatasetLoader,
)

from src.evaluation.benchmark.curriculum_benchmark import (
    CurriculumBenchmark,
)

from src.evaluation.metrics.quantitative_evaluator import (
    QuantitativeEvaluator,
)


def main():

    dataset = BDDDatasetLoader(
            
        image_dir="data/raw/assignment_data_bdd/bdd100k_images_100k/bdd100k/images/100k/val",

        annotation_file="data/raw/assignment_data_bdd/bdd100k_labels_release/bdd100k/labels/bdd100k_labels_images_val.json",
    )

    benchmark = CurriculumBenchmark(
        dataset.records
    )

    evaluator = (
        QuantitativeEvaluator(

            model_path=(
                "outputs/"
                "yolo_training-3/"
                "weights/"
                "best.pt"
            ),

            output_dir=(
                "outputs/"
                "evaluation/"
                "metrics"
            ),
        )
    )

    easy_results = (
        evaluator.evaluate(

            records=(
                benchmark
                .get_easy_records()
            )[:50],

            scenario_name="easy",
        )
    )

    medium_results = (
        evaluator.evaluate(

            records=(
                benchmark
                .get_medium_records()
            )[:50],

            scenario_name="medium",
        )
    )

    hard_results = (
        evaluator.evaluate(

            records=(
                benchmark
                .get_hard_records()
            )[:50],

            scenario_name="hard",
        )
    )

    print("\nEasy:")
    pprint(easy_results)

    print("\nMedium:")
    pprint(medium_results)

    print("\nHard:")
    pprint(hard_results)


if __name__ == "__main__":
    main()