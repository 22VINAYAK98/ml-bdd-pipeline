"""
Prediction visualization utilities.
"""

import os

from ultralytics import YOLO


class PredictionVisualizer:
    """
    Visualize YOLO predictions.
    """

    def __init__(
        self,
        model_path,
        output_dir,
    ):

        self.model = YOLO(
            model_path
        )

        self.output_dir = output_dir

        os.makedirs(
            self.output_dir,
            exist_ok=True,
        )

    def visualize_predictions(
        self,
        image_paths,
    ):
        """
        Run inference and save
        prediction visualizations.
        """

        for image_path in image_paths:

            self._visualize_single_image(
                image_path
            )

    def _visualize_single_image(
        self,
        image_path,
    ):
        """
        Visualize predictions for
        a single image.
        """

        self.model.predict(

            source=image_path,

            conf=0.01,

            save=True,

            project="/app/outputs",

            name="prediction_visualizations",

            exist_ok=True,
        )

        print(
            f"Processed: {image_path}"
        )