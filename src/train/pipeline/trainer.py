"""
Common training pipeline.

Responsible for orchestrating:
- curriculum loading
- dataset preparation
- model training
- evaluation
"""

from src.train.curriculum.curriculum_loader import CurriculumLoader


class TrainingPipeline:
    """
    Common model-agnostic
    training pipeline.
    """

    def __init__(
        self,
        records,
        strategy,
    ):

        self.records = records

        self.strategy = strategy

        self.curriculum_loader = CurriculumLoader(self.records)

    def run(
        self,
        curriculum_stage="easy",
    ):
        """
        Run training pipeline.

        Input:
            curriculum_stage:
                easy / medium / hard
        """

        staged_records = self.curriculum_loader.get_stage_records(curriculum_stage)

        records = [sample["record"] for sample in staged_records]

        self.strategy.prepare_dataset(records)

        self.strategy.build_model()

        self.strategy.train()

        self.strategy.evaluate()
