"""
Entity definitions for BDD100K dataset records.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class BoundingBox:
    x1: float
    y1: float
    x2: float
    y2: float


@dataclass
class Annotation:
    label_id: int

    category: str
    bbox: BoundingBox

    occluded: bool
    truncated: bool


@dataclass
class ImageRecord:
    image_name: str
    image_path: str

    weather: str
    scene: str
    timeofday: str

    timestamp: int

    annotations: List[Annotation]