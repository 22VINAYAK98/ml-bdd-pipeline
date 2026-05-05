# ml-bdd-pipeline

A modular pipeline for BDD dataset analysis and model experimentation, packaged in Docker for reproducibility.

---

## Overview

* Parses BDD object detection labels (JSON)
* Runs basic data analysis (EDA)
* Provides scaffolding for training and validation
* Runs entirely inside a Docker container

---

## Project Structure

```
ml-bdd-pipeline/
├── src/
│   ├── data/         # loaders, parsers
│   ├── analysis/     # EDA scripts
│   ├── train/        # training / validation
│   └── main.py       # entry point
├── data/             # local dataset (ignored by Git)
├── outputs/          # results (ignored)
├── configs/          # config files
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Prerequisites

* Docker installed
* Git installed

---

## Setup and Run

1. Clone the repository

```
git clone https://github.com/22VINAYAK98/ml-bdd-pipeline.git
cd ml-bdd-pipeline
```

2. Add dataset locally

Place BDD data under:

```
data/raw/
```

Example:

```
data/raw/
├── images/
├── labels.json
```

3. Build Docker image

```
docker build -t bdd-pipeline .
```

4. Run pipeline

```
docker run -v $(pwd)/data:/app/data bdd-pipeline
```

---

## Notes on Data Handling

* The `data/` directory is excluded via `.gitignore`
* Dataset is mounted at runtime using Docker volumes

---


## Development Workflow

```
git add .
git commit -m "message"
git push
```

---

## Design Choices

* Modular structure to separate data, analysis, and training
* Docker to ensure consistent environment across systems
* Local data mounting to avoid committing large datasets

---


## Author

Vinayak Mahabaleshwar Boormane
