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


VRU_CLASSES = [
    "person",
    "rider",
    "bike",
    "motor",
]