"""
Different Category of Objects/ laabels of objects  Present and label mappings for BDD100K object detection.
Keeps category handling consistent across parsing, analysis, training, and evaluation pipelines.
"""

DETECTION_CLASSES = {
    "person",
    "rider",
    "car",
    "truck",
    "bus",
    "train",
    "motor",
    "bike",
    "traffic light",
    "traffic sign",
}


CLASS_TO_ID = {
    "pedestrian": 0,
    "rider": 1,
    "car": 2,
    "truck": 3,
    "bus": 4,
    "train": 5,
    "motorcycle": 6,
    "bicycle": 7,
    "traffic light": 8,
    "traffic sign": 9,
}


VRU_CLASSES = [
    "person",
    "rider",
    "bike",
    "motor",
]
