from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Dataset Paths
RAW_DATASET = PROJECT_ROOT / "dataset" / "raw"
PROCESSED_DATASET = PROJECT_ROOT / "dataset" / "processed"
GENERATED_DATASET = PROJECT_ROOT / "dataset" / "generated"
KNOWLEDGE_BASE = PROJECT_ROOT / "dataset" / "knowledge_base"

# Model Path
MODEL_PATH = PROJECT_ROOT / "models"