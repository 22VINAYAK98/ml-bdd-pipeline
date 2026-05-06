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
│   ├── train/                 # training / validation pipeline
│   │
│   ├── tests/
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

# Development Workflow

```bash
git add .
git commit -m "message"
git push
```

---

# Author

Vinayak Mahabaleshwar Boormane
