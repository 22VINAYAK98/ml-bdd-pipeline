# ml-bdd-pipeline

A modular pipeline for BDD100K dataset analysis and model experimentation, packaged using Docker for reproducibility and easier deployment.

---

# Overview

This project focuses on building a reusable and structured pipeline for the BDD100K object detection dataset.

Instead of directly performing analysis from raw JSON files, the initial focus was to create a clean parsing and loading layer which can later be reused for:

* data analysis
* training
* evaluation
* visualization

Currently the implementation focuses only on the object detection task from BDD100K.
Annotations related to lane markings and drivable areas are filtered out during parsing since they are outside current assignment scope.

---

# Project Structure

```text
ml-bdd-pipeline/
├── src/
│   ├── data/
│   │   ├── categories.py      # supported BDD detection classes
│   │   ├── entities.py        # structured dataset entities
│   │   ├── filters.py         # annotation filtering logic
│   │   ├── parser.py          # JSON parsing utilities
│   │   ├── loader.py          # dataset/image loading
│   │   └── utils.py           # visualization utilities
│   │
│   ├── analysis/              # AnAlysis and statistics scripts
│   │   ├── environmental_analysis.py
│   │   ├── environmental_visualization.py
│   │   ├── object_analysis.py
│   │   └── object_visualization.py
│   │
│   ├── train/                 # training / validation pipeline
│   │
│   ├── tests/
│   │   ├── test_environmental_analysis.py
│   │   ├── test_environmental_visualization.py
│   │   ├── test_object_analysis.py
│   │   ├── test_object_visualization.py
│   │   └── test_data_pipeline.py
│   │
│   └── main.py
│
├── data/                      # local dataset (ignored by Git)
├── outputs/                   # generated outputs (ignored)
├── configs/                   # configuration files
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

---

# Data Pipeline Flow

```text
BDD JSON Labels + Images
            ↓
        Parser Layer
            ↓
    Annotation Filtering
            ↓
   Structured Entity Objects
            ↓
        Dataset Loader
            ↓
 Visualization / Analysis / Training
```

---

# File Responsibilities

## `src/data/categories.py`

Contains centralized definition of supported BDD100K object detection categories.

Example:

* car
* person
* traffic light
* rider

This was seperated intentionally so category handling remains consistent across the complete pipeline.

---

## `src/data/entities.py`

Defines structured data entities used internally in pipeline.

Main entities:

* `BoundingBox`
* `Annotation`
* `ImageRecord`

Instead of working with deeply nested raw dictionaries everywhere, the parser converts annotations into strongly structured objects.

---

## `src/data/filters.py`

Contains filtering utilities for annotation validation.

Currently used for:

* retaining only supported detection classes
* rejecting lane/drivable-area annotations
* validating presence of `box2d`

---

## `src/data/parser.py`

Responsible for parsing raw BDD100K JSON annotations.

Main responsibilities:

* loading raw JSON
* parsing image metadata
* parsing annotation objects
* converting raw labels into structured entities

The parser also handles filtering internally before constructing final records.

---

## `src/data/loader.py`

Dataset loading layer built on top of parser.

Responsibilities:

* loading image records
* lazy image loading using OpenCV
* providing dataset-like interface using:

  * `__len__`
  * `__getitem__`

This layer is intended to be reused later for:

* Data Ananlysis
* model training Pipeline 
* evaluation

---

## `src/data/utils.py`

Contains utility functions used across the pipeline.

Currently includes:

* annotation visualization utilities
* bounding box rendering helpers

---

## `src/tests/test_data_pipeline.py`

Sanity validation script for the complete data pipeline.

This script validates:

* JSON parsing
* filtering logic
* image loading
* annotation visualization
* bounding box alignment

The script also saves a sample annotated image into `outputs/`.

---

# Prerequisites

* Docker installed
* Git installed

---

# Setup

## Clone Repository

```bash
git clone https://github.com/22VINAYAK98/ml-bdd-pipeline.git
cd ml-bdd-pipeline
```

---

# Dataset Placement

Place downloaded BDD100K dataset under:

```text
data/raw/
```

Example:

```text
data/raw/
├── assignment_data_bdd/
```

---

# Build Docker Image

```bash
docker build -t ml-bdd-pipeline .
```

---

# Run Data Pipeline Validation

```bash
docker run --rm \
-v $(pwd)/data:/app/data \
-v $(pwd)/outputs:/app/outputs \
ml-bdd-pipeline \
python -m src.tests.test_data_pipeline
```

---

# Outputs

Generated outputs such as:

* annotated sample images
* plots
* evaluation artifacts

will be saved under:

```text
outputs/
```

---

# Notes on Data Handling

* `data/` directory is excluded using `.gitignore`
* dataset is mounted dynamically using Docker volumes
* large datasets are intentionally not stored inside Docker image with help of .dockerignore

---

# Design Choices

* Modular structure to separate parsing, loading, analysis and training
* Structured entity objects instead of raw nested dictionaries
* Docker based execution for reproducibility
* Filtering abstraction to isolate object detection task cleanly
* Local dataset mounting to avoid committing large files

---

# ADAS-Oriented Dataset Analysis Approach

ADAS perception systems have very different expectations compared to general-purpose computer vision systems.
Because of this, the dataset analysis was intentionally designed from an autonomous driving perception perspective rather than performing only generic dataset EDA.

The analysis was mainly divided into two major groups:

---

# 1. Environmental Analysis

Environmental analysis focuses on understanding operational driving conditions under which the perception system is expected to work.

Current environmental analysis includes:

* weather distribution
* scene distribution
* time-of-day distribution

This analysis helps understand:

* environmental robustness
* operational domain coverage
* illumination variability
* driving condition imbalance

---

# 2. Object-Level Analysis

Object-level analysis focuses on perception difficulty and safety-critical object understanding.

Current object analysis includes:

* object class distribution
* bounding box area distribution
* object density analysis
* occlusion statistics
* truncation statistics
* class distribution across time-of-day
* vulnerable road user (VRU) risk analysis

This analysis helps understand:

* perception complexity
* long-range detection difficulty
* nighttime perception challenges
* vulnerable road user visibility
* safety-critical perception scenarios

The overall objective was to structure analysis around realistic autonomous driving perception challenges instead of only generating generic dataset statistics.

---

# Analysis Pipeline Architecture

```text
BDD Dataset
     ↓
Parser Layer
     ↓
Filtering Layer
     ↓
Structured Entities
     ↓
Analysis Pipelines
     ↓
Visualization Layer
     ↓
ADAS-Oriented Insights
```

---

# Analysis File Responsibilities

## `environmental_analysis.py`

Responsible for operational driving condition analysis.

Current analysis:

* weather distribution
* scene distribution
* time-of-day distribution

---

## `environmental_visualization.py`

Responsible for visualizing environmental statistics.

Generated plots:

* weather distribution
* scene distribution
* time-of-day distribution

---

## `object_analysis.py`

Responsible for object-level perception analysis.

Current analysis:

* object class distribution
* bounding box statistics
* object density
* occlusion statistics
* truncation statistics
* class distribution across time-of-day
* vulnerable road user analysis

---

## `object_visualization.py`

Responsible for visualizing perception-oriented object statistics.

Generated plots:

* object class distribution
* bbox area distribution
* occlusion distribution
* class distribution across time-of-day
* VRU perception risk analysis

---

# Running Analysis Pipelines

## Run Environmental Analysis

```bash
docker run --rm \
-v $(pwd)/data:/app/data \
-v $(pwd)/outputs:/app/outputs \
ml-bdd-pipeline \
python -m src.tests.test_environmental_analysis
```

---

## Run Environmental Visualization

```bash
docker run --rm \
-v $(pwd)/data:/app/data \
-v $(pwd)/outputs:/app/outputs \
ml-bdd-pipeline \
python -m src.tests.test_environmental_visualization
```

---

## Run Object Analysis

```bash
docker run --rm \
-v $(pwd)/data:/app/data \
-v $(pwd)/outputs:/app/outputs \
ml-bdd-pipeline \
python -m src.tests.test_object_analysis
```

---

## Run Object Visualization

```bash
docker run --rm \
-v $(pwd)/data:/app/data \
-v $(pwd)/outputs:/app/outputs \
ml-bdd-pipeline \
python -m src.tests.test_object_visualization
```

---

# Environmental Analysis Results

## Weather Distribution

![Weather Distribution](outputs/weather_distribution.png)

### Observation

Clear weather dominates the dataset significantly while adverse conditions such as foggy and snowy weather are comparatively underrepresented.

### ADAS Significance

Perception systems trained mostly on clear-weather data may show reduced robustness under degraded visibility conditions.

---

## Scene Distribution

![Scene Distribution](outputs/scene_distribution.png)

### Observation

City street scenes dominate the dataset followed by highway and residential scenarios.

### ADAS Significance

The dataset appears strongly urban-focused, which is useful for dense traffic perception analysis but may underrepresent uncommon operational domains.

---

## Time Of Day Distribution

![Time Of Day Distribution](outputs/timeofday_distribution.png)

### Observation

Daytime scenes dominate the dataset while dawn/dusk scenarios are comparatively limited.

### ADAS Significance

Heavy daytime dominance may reduce perception robustness under low-illumination driving conditions.

---

# Object Analysis Results

## Object Class Distribution

![Object Class Distribution](outputs/class_distribution.png)

### Observation

Cars dominate the dataset significantly while vulnerable road users such as riders and motorcycles appear comparatively less frequent.

### ADAS Significance

Heavy class imbalance may bias object detectors toward dominant vehicle classes while reducing robustness for safety-critical vulnerable road users.

---

## Bounding Box Area Distribution

![Bounding Box Area Distribution](outputs/bbox_area_distribution.png)

### Observation

The bounding box area distribution is heavily right-skewed, indicating a large concentration of very small objects.

### ADAS Significance

Small bounding boxes often correspond to distant traffic participants or infrastructure, making long-range perception significantly more difficult.

---

## Occlusion Distribution

![Occlusion Distribution](outputs/occlusion_distribution.png)

### Observation

Approximately 47% of objects appear partially occluded.

### ADAS Significance

High occlusion ratios indicate realistic urban driving complexity and increased perception difficulty for detection and tracking systems.

---

## Class Distribution Across Time Of Day

![Class Distribution Across Time Of Day](outputs/timeofday_class_distribution.png)

### Observation

Object visibility distribution changes noticeably across daytime, nighttime and dawn/dusk conditions.

### ADAS Significance

Illumination conditions significantly affect perception robustness and may impact detector reliability during nighttime driving.

---

## VRU Perception Risk Analysis

![VRU Perception Risk Analysis](outputs/vru_perception_risk_analysis.png)

### Observation

Nighttime occluded vulnerable road users form a comparatively smaller but highly important subset of perception scenarios.

### ADAS Significance

Night + occlusion + vulnerable road users represent one of the most safety-critical and difficult perception conditions for autonomous driving systems.

---

# Key Findings

* Nearly half of the detected objects are partially occluded, indicating realistic urban driving complexity.
* The dataset is strongly dominated by daytime and clear-weather scenarios.
* Vulnerable road users are comparatively less represented than vehicle classes.
* Small object dominance suggests substantial long-range perception challenges.
* Nighttime occluded VRUs represent highly safety-critical perception scenarios.


# Development Workflow

```bash
git add .
git commit -m "message"
git push
```

---

# Author

Vinayak Mahabaleshwar Boormane
