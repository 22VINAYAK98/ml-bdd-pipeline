"""
Quantitative evaluation utilities
for ADAS perception benchmarking.
"""

import json
import os

from ultralytics import YOLO

from src.train.utils.dataset_converter import YOLODatasetConverter


class QuantitativeEvaluator:
    """
    Perform quantitative evaluation
    for benchmark subsets.
    """

    def __init__(
        self,
        model_path,
        output_dir,
    ):

        self.model = YOLO(model_path)

        self.output_dir = output_dir

        os.makedirs(
            self.output_dir,
            exist_ok=True,
        )

    def evaluate(
        self,
        records,
        scenario_name,
    ):
        """
        Evaluate benchmark subset.
        """

        dataset_output_dir = os.path.join(
            self.output_dir,
            scenario_name,
        )

        converter = YOLODatasetConverter(dataset_output_dir)

        converter.convert_records(records)

        data_yaml_path = os.path.join(
            dataset_output_dir,
            "dataset.yaml",
        )

        metrics = self.model.val(
            data=data_yaml_path,
            split="val",
            verbose=False,
        )

        results = {
            "precision": float(metrics.box.mp),
            "recall": float(metrics.box.mr),
            "mAP50": float(metrics.box.map50),
            "mAP50_95": float(metrics.box.map),
        }

        self._save_results(
            scenario_name,
            results,
        )

        return results

    def _save_results(
        self,
        scenario_name,
        results,
    ):
        """
        Save evaluation metrics.
        """

        output_path = os.path.join(
            self.output_dir,
            (f"{scenario_name}" f"_metrics.json"),
        )

        with open(
            output_path,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                results,
                file,
                indent=4,
            )

        print(f"Saved metrics: " f"{output_path}")
