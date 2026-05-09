"""
Curriculum-aware benchmarking
utilities for ADAS perception
evaluation.
"""

from src.train.curriculum.difficulty_analyzer import DifficultyAnalyzer


class CurriculumBenchmark:
    """
    Generate curriculum-based
    benchmark subsets.
    """

    def __init__(
        self,
        records,
    ):

        self.records = records

        self.analyzer = DifficultyAnalyzer()

    # ----------------------------------
    # Difficulty Analysis
    # ----------------------------------

    def _get_difficulty_analysis(
        self,
        record,
    ):
        """
        Run difficulty analysis
        for a single record.
        """

        return self.analyzer.analyze(record)

    def _get_difficulty_score(
        self,
        record,
    ):
        """
        Extract difficulty score.
        """

        analysis = self._get_difficulty_analysis(record)

        return analysis["difficulty_score"]

    def _get_difficulty_level(
        self,
        record,
    ):
        """
        Extract difficulty level.
        """

        analysis = self._get_difficulty_analysis(record)

        return analysis["difficulty_level"]

    # ----------------------------------
    # Curriculum Benchmark Groups
    # ----------------------------------

    def get_easy_records(
        self,
    ):

        return [
            record
            for record in self.records
            if (self._get_difficulty_level(record) == "easy")
        ]

    def get_medium_records(
        self,
    ):

        return [
            record
            for record in self.records
            if (self._get_difficulty_level(record) == "medium")
        ]

    def get_hard_records(
        self,
    ):

        return [
            record
            for record in self.records
            if (self._get_difficulty_level(record) == "hard")
        ]

    # ----------------------------------
    # Benchmark Summary
    # ----------------------------------

    def get_summary(
        self,
    ):

        summary = {
            "easy": len(self.get_easy_records()),
            "medium": len(self.get_medium_records()),
            "hard": len(self.get_hard_records()),
        }

        return summary
