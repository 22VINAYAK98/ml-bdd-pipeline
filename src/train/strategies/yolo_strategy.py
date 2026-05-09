"""
YOLO training strategy.
"""

from ultralytics import YOLO

from src.train.strategies.base_strategy import (
    BaseTrainingStrategy,
)

from src.train.utils.dataset_converter import (
    YOLODatasetConverter,
)


class YOLOTrainingStrategy(
    BaseTrainingStrategy
):
    """
    YOLO-specific training logic.
    """

    def __init__(
        self,
        output_dir="outputs/yolo_dataset",
    ):

        self.records = None

        self.output_dir = output_dir

        self.converter = (
            YOLODatasetConverter(
                self.output_dir
            )
        )

        self.model = None

    def prepare_dataset(
        self,
        records,
    ):

        self.records = records

        print(
            f"Preparing YOLO dataset "
            f"with {len(records)} records."
        )

        self.converter.convert_records(
            records
        )

    def build_model(self):

        print(
            "Loading YOLO model."
        )

        self.model = YOLO(
            "yolov8n.pt"
        )

    def train(self):

        print(
            "Starting YOLO training."
        )

        self.model.train(

            data=(
                f"{self.output_dir}"
                f"/dataset.yaml"
            ),

            epochs=200,

            imgsz=640,

            batch=4,

            project="/app/outputs",

            name="yolo_training",
        )

    def evaluate(self):

        print(
            "Evaluating YOLO model."
        )

        metrics = self.model.val()

        print(metrics) 