import numpy as np
from typing import List
from sentence_transformers import SentenceTransformer

def load_encoder(name: str):
    return SentenceTransformer(name)

def encode(encoder: SentenceTransformer, texts: List[str], batch_size: int = 64) -> np.ndarray:
    return encoder.encode(
        texts,
        batch_size=batch_size,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=False,
    )
