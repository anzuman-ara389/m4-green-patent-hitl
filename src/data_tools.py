import os
import pandas as pd
from .config import CFG

def load_parquet_or_dummy(path: str = None) -> pd.DataFrame:
    path = path or CFG.parquet_path
    if os.path.exists(path):
        return pd.read_parquet(path)

    # Tiny dummy dataset (for testing only)
    rows = []
    for i in range(200):
        rows.append({"doc_id": f"train_{i}", "text": f"Claim about solar panel efficiency {i}.", "is_green_silver": 1, "split": "train_silver"})
    for i in range(200, 350):
        rows.append({"doc_id": f"pool_{i}", "text": f"Claim about manufacturing process {i}.", "is_green_silver": 0, "split": "pool_unlabeled"})
    for i in range(350, 450):
        rows.append({"doc_id": f"eval_{i}", "text": f"Claim about battery recycling {i}.", "is_green_silver": 1, "split": "eval_silver"})
    return pd.DataFrame(rows)
