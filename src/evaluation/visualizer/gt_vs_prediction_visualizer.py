"""
Ground truth vs prediction
visualization utilities.
"""

import os

import cv2

from ultralytics import YOLO


class GTVsPredictionVisualizer:
    """
    Compare ground truth and
    predicted detections.
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

    def visualize(
        self,
        records,
        scenario_name,
    ):
        """
        Visualize GT vs predictions
        for a benchmark scenario.
        """

        for record in records:

            self._visualize_record(

                record,

                scenario_name,
            )

    def _visualize_record(
        self,
        record,
        scenario_name,
    ):
        """
        Generate comparison image.
        """

        image = cv2.imread(
            record.image_path
        )

        results = self.model.predict(

            source=record.image_path,

            conf=0.25,

            verbose=False,
        )

        result = results[0]

        # ----------------------------------
        # Draw Ground Truth
        # ----------------------------------

        for annotation in (
            record.annotations
        ):

            bbox = annotation.bbox

            x1 = int(bbox.x1)
            y1 = int(bbox.y1)

            x2 = int(bbox.x2)
            y2 = int(bbox.y2)

            category = (
                annotation.category
            )

            cv2.rectangle(

                image,

                (x1, y1),

                (x2, y2),

                (0, 255, 0),

                2,
            )

            cv2.putText(

                image,

                f"GT: {category}",

                (x1, y1 - 10),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.5,

                (0, 255, 0),

                2,
            )

        # ----------------------------------
        # Draw Predictions
        # ----------------------------------

        for box in result.boxes:

            x1, y1, x2, y2 = (
                box.xyxy[0]
                .cpu()
                .numpy()
            )

            class_id = int(
                box.cls[0]
            )

            confidence = float(
                box.conf[0]
            )

            class_name = (
                result.names[class_id]
            )

            cv2.rectangle(

                image,

                (int(x1), int(y1)),

                (int(x2), int(y2)),

                (0, 0, 255),

                2,
            )

            cv2.putText(

                image,

                (
                    f"PRED: "
                    f"{class_name} "
                    f"{confidence:.2f}"
                ),

                (
                    int(x1),
                    int(y1) - 10,
                ),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.5,

                (0, 0, 255),

                2,
            )

        # ----------------------------------
        # Scenario-specific folder
        # ----------------------------------

        scenario_dir = os.path.join(

            self.output_dir,

            scenario_name,
        )

        os.makedirs(

            scenario_dir,

            exist_ok=True,
        )

        output_filename = (

            f"{scenario_name}_"
            f"{record.image_name}"
        )

        output_path = os.path.join(

            scenario_dir,

            output_filename,
        )

        cv2.imwrite(
            output_path,
            image,
        )

        print(
            f"Saved: {output_path}"
        )