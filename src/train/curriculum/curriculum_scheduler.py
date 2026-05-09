"""
Curriculum scheduling utilities.

Responsible for organizing dataset
samples based on perception difficulty.
"""

from collections import defaultdict

from src.train.curriculum.difficulty_analyzer import DifficultyAnalyzer


class CurriculumScheduler:
    """
    Organize dataset into curriculum
    learning stages.
    """

    def __init__(self, records):

        self.records = records

        self.analyzer = DifficultyAnalyzer()

    def build_curriculum(self):
        """
        Build staged curriculum groups.

        Output:
            {
                "easy": [...],
                "medium": [...],
                "hard": [...]
            }
        """

        curriculum = defaultdict(list)

        for record in self.records:

            result = self.analyzer.analyze(record)

            difficulty_level = result["difficulty_level"]

            curriculum[difficulty_level].append(
                {
                    "record": record,
                    "difficulty_score": result["difficulty_score"],
                    "difficulty_breakdown": result["difficulty_breakdown"],
                }
            )

        return dict(curriculum)
