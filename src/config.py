from dataclasses import dataclass

@dataclass
class Config:
    parquet_path: str = "data/patents_50k_green.parquet"

    text_col: str = "text"
    doc_id_col: str = "doc_id"
    split_col: str = "split"
    silver_label_col: str = "is_green_silver"

    train_split: str = "train_silver"
    pool_split: str = "pool_unlabeled"
    eval_split: str = "eval_silver"

    encoder_name: str = "AI-Growth-Lab/PatentSBERTa"
    max_length: int = 256
    embed_batch: int = 64
    seed: int = 42

CFG = Config()
