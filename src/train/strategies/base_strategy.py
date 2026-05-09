"""
Base interface for all
training strategies.
"""

from abc import ABC, abstractmethod


class BaseTrainingStrategy(ABC):
    """
    Abstract base class for all
    model training strategies.
    """

    @abstractmethod
    def prepare_dataset(
        self,
        records,
    ):
        """
        Prepare dataset for training.

        Input:
            records:
                Curriculum-selected records.
        """

        pass

    @abstractmethod
    def build_model(self):
        """
        Initialize model architecture.
        """

        pass

    @abstractmethod
    def train(self):
        """
        Execute training process.
        """

        pass

    @abstractmethod
    def evaluate(self):
        """
        Evaluate trained model.
        """

        pass
