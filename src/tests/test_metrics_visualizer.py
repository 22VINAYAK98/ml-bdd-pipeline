"""
Sanity test for curriculum
metrics visualization.
"""

from src.evaluation.visualizer.metrics_visualizer import MetricsVisualizer


def main():

    visualizer = MetricsVisualizer(
        metrics_dir=("outputs/" "evaluation/" "metrics"),
        output_dir=("outputs/" "evaluation/" "plots"),
    )

    visualizer.plot_curriculum_metrics()


if __name__ == "__main__":
    main()
