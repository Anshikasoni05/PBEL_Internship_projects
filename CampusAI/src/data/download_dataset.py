from datasets import load_dataset
import pandas as pd
from pathlib import Path


# Project Root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Output Folder
OUTPUT_DIR = PROJECT_ROOT / "dataset" / "raw"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


print("Downloading dataset...")

# Mozilla Smart Intent Dataset
dataset = load_dataset("Mozilla/smart_intent_dataset")

print("\nAvailable Splits:")
print(dataset)

# Convert train split to pandas
train_df = dataset["train"].to_pandas()

print("\nFirst 5 Rows:")
print(train_df.head())

print(f"\nTotal Training Rows : {len(train_df)}")

# Save CSV
csv_path = OUTPUT_DIR / "mozilla_smart_intent_train.csv"
train_df.to_csv(csv_path, index=False)

print("\nDataset Saved Successfully!")
print(csv_path)