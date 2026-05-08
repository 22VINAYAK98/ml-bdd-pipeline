"""
Curriculum-aware dataset loader.
"""

from src.train.curriculum.curriculum_scheduler import (
    CurriculumScheduler,
)


class CurriculumLoader:
    """
    Provide curriculum-based staged
    dataset access.
    """

    def __init__(self, records):

        self.records = records

        self.scheduler = (
            CurriculumScheduler(
                self.records
            )
        )

        self.curriculum = (
            self.scheduler.build_curriculum()
        )

    def get_stage_records(
        self,
        stage,
    ):
        """
        Retrieve records for a
        curriculum stage.

        Input:
            stage:
                easy / medium / hard

        Output:
            List of staged records.
        """

        if stage not in self.curriculum:

            raise ValueError(
                f"Invalid stage: {stage}"
            )

        return self.curriculum[stage]

    def get_stage_summary(self):
        """
        Return curriculum summary.
        """

        summary = {}

        for stage, records in (
            self.curriculum.items()
        ):

            summary[stage] = len(records)

        return summary