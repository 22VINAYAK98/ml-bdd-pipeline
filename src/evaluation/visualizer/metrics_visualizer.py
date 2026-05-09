"""
Visualization utilities for
quantitative evaluation metrics.
"""

import json
import os

import matplotlib.pyplot as plt


class MetricsVisualizer:
    """
    Visualize quantitative
    benchmark metrics.
    """

    def __init__(
        self,
        metrics_dir,
        output_dir,
    ):

        self.metrics_dir = (
            metrics_dir
        )

        self.output_dir = (
            output_dir
        )

        os.makedirs(

            self.output_dir,

            exist_ok=True,
        )

    # ----------------------------------
    # Metric Loading
    # ----------------------------------

    def _load_metric_file(
        self,
        filename,
    ):

        file_path = os.path.join(

            self.metrics_dir,

            filename,
        )

        with open(

            file_path,

            "r",

            encoding="utf-8",
        ) as file:

            return json.load(
                file
            )

    # ----------------------------------
    # Curriculum Visualization
    # ----------------------------------

    def plot_curriculum_metrics(
        self,
    ):
        """
        Plot Easy vs Medium
        vs Hard metrics.
        """

        easy_metrics = (
            self._load_metric_file(
                "easy_metrics.json"
            )
        )

        medium_metrics = (
            self._load_metric_file(
                "medium_metrics.json"
            )
        )

        hard_metrics = (
            self._load_metric_file(
                "hard_metrics.json"
            )
        )

        categories = [
            "Easy",
            "Medium",
            "Hard",
        ]

        # ----------------------------------
        # mAP50 Comparison
        # ----------------------------------

        map50_values = [

            easy_metrics["mAP50"],

            medium_metrics["mAP50"],

            hard_metrics["mAP50"],
        ]

        plt.figure()

        plt.bar(
            categories,
            map50_values,
        )

        plt.ylabel(
            "mAP50"
        )

        plt.title(
            (
                "Curriculum Difficulty "
                "vs mAP50"
            )
        )

        plt.savefig(

            os.path.join(

                self.output_dir,

                (
                    "curriculum_"
                    "map50.png"
                ),
            )
        )

        plt.close()

        # ----------------------------------
        # Recall Comparison
        # ----------------------------------

        recall_values = [

            easy_metrics["recall"],

            medium_metrics["recall"],

            hard_metrics["recall"],
        ]

        plt.figure()

        plt.bar(
            categories,
            recall_values,
        )

        plt.ylabel(
            "Recall"
        )

        plt.title(
            (
                "Curriculum Difficulty "
                "vs Recall"
            )
        )

        plt.savefig(

            os.path.join(

                self.output_dir,

                (
                    "curriculum_"
                    "recall.png"
                ),
            )
        )

        plt.close()

        print(
            "Saved curriculum "
            "metric plots."
        )